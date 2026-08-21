#!/usr/bin/env python3
"""Build per-cell street-network extracts from an OSM PBF.

Output: cells/c{lat100}_{lon100}.json.gz on a 0.05-degree grid, each holding
{source, timestamp, nodes:[{id,lat,lon}], ways:[{id,nodes,tags}]} for every
highway-tagged way whose bbox touches the cell (nodes deduped per cell).
The app merges cells and dedupes by id — duplication across cells is by design.

License: extracts are derivative databases of OpenStreetMap data, ODbL 1.0.
(c) OpenStreetMap contributors.
"""
import gzip
import json
import math
import os
import sys
import time

import osmium

STEP = 0.05
# Coverage regions (name, s, w, n, e). Owner's priority list 2026-08-21.
# The NCR box supersedes the original Metro Manila bounds (14.20, 120.85,
# 14.95, 121.25) and takes in the wider NCR + Calabarzon.
REGIONS = [
    ("ncr-calabarzon",   13.50, 120.60, 15.10, 121.80),
    ("metro-cebu",       10.20, 123.70, 10.55, 124.05),
    ("metro-davao",       6.95, 125.30,  7.35, 125.75),
    ("baguio",           16.30, 120.50, 16.50, 120.70),
    ("iloilo",           10.60, 122.40, 10.85, 122.70),
    ("cagayan-de-oro",    8.35, 124.50,  8.60, 124.80),
    ("bacolod",          10.55, 122.85, 10.80, 123.10),
    ("legazpi",          13.05, 123.65, 13.30, 123.85),
    ("naga",             13.50, 123.05, 13.70, 123.30),
    ("puerto-princesa",   9.65, 118.60,  9.90, 118.85),
    ("dumaguete",         9.20, 123.20,  9.45, 123.40),
    ("tuguegarao",       17.50, 121.60, 17.75, 121.85),
    ("subic-olongapo",   14.70, 120.15, 14.95, 120.40),
    ("clark-angeles",    15.05, 120.45, 15.30, 120.75),
]


class WayPass(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.ways = []
        self.node_ids = set()

    def way(self, w):
        if 'highway' not in w.tags:
            return
        refs = [n.ref for n in w.nodes]
        if len(refs) < 2:
            return
        self.ways.append((w.id, refs, {t.k: t.v for t in w.tags}))
        self.node_ids.update(refs)


class NodePass(osmium.SimpleHandler):
    def __init__(self, wanted):
        super().__init__()
        self.wanted = wanted
        self.coords = {}

    def node(self, n):
        if n.id in self.wanted:
            self.coords[n.id] = (n.location.lat, n.location.lon)


def cell_of(lat, lon):
    return (math.floor(lat / STEP), math.floor(lon / STEP))


def cell_name(ci):
    la, lo = ci
    return f"c{round(la * STEP * 100)}_{round(lo * STEP * 100)}"


def main(pbf_path, out_dir, source_label):
    t0 = time.time()
    wp = WayPass()
    wp.apply_file(pbf_path)
    print(f"ways with highway: {len(wp.ways)}; nodes referenced: {len(wp.node_ids)} "
          f"({time.time()-t0:.0f}s)")
    np_ = NodePass(wp.node_ids)
    np_.apply_file(pbf_path)
    print(f"node coords resolved: {len(np_.coords)} ({time.time()-t0:.0f}s)")

    cells = {}  # ci -> {"nodes": {id:(lat,lon)}, "ways": []}
    for wid, refs, tags in wp.ways:
        pts = [np_.coords[r] for r in refs if r in np_.coords]
        if len(pts) < 2:
            continue
        lats = [p[0] for p in pts]
        lons = [p[1] for p in pts]
        # Union of cell ranges across every region the way touches, so
        # overlapping regions never duplicate a way within one cell.
        touched = set()
        for _, s, w_, n, e in REGIONS:
            if max(lats) < s or min(lats) > n or max(lons) < w_ or min(lons) > e:
                continue
            c0 = cell_of(max(min(lats), s), max(min(lons), w_))
            c1 = cell_of(min(max(lats), n), min(max(lons), e))
            for la in range(c0[0], c1[0] + 1):
                for lo in range(c0[1], c1[1] + 1):
                    touched.add((la, lo))
        for ci in touched:
            cell = cells.setdefault(ci, {"nodes": {}, "ways": []})
            cell["ways"].append({"id": wid, "nodes": refs, "tags": tags})
            for r in refs:
                if r in np_.coords:
                    cell["nodes"][r] = np_.coords[r]

    os.makedirs(out_dir, exist_ok=True)
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    index = {"generated": ts, "source": source_label, "step_deg": STEP,
             "regions": [{"name": r[0], "bounds": list(r[1:])} for r in REGIONS],
             "cells": []}
    for ci, cell in sorted(cells.items()):
        name = cell_name(ci)
        payload = {
            "source": source_label,
            "timestamp": ts,
            "nodes": [{"id": i, "lat": la, "lon": lo}
                      for i, (la, lo) in cell["nodes"].items()],
            "ways": cell["ways"],
        }
        raw = json.dumps(payload, separators=(",", ":")).encode()
        with gzip.open(os.path.join(out_dir, f"{name}.json.gz"), "wb",
                       compresslevel=9) as f:
            f.write(raw)
        index["cells"].append({"name": name, "ways": len(cell["ways"]),
                               "bytes_raw": len(raw)})
    with open(os.path.join(out_dir, "index.json"), "w") as f:
        json.dump(index, f)
    total = sum(os.path.getsize(os.path.join(out_dir, fn))
                for fn in os.listdir(out_dir))
    print(f"cells: {len(cells)}; total compressed: {total/1e6:.1f} MB "
          f"({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2],
         sys.argv[3] if len(sys.argv) > 3 else "geofabrik-philippines")
