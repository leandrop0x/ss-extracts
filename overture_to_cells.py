#!/usr/bin/env python3
"""EXPERIMENTAL: build the same cell format from Overture Maps transportation
segments (alternate source when OSM/Overpass paths are unavailable).

Overture segments carry their own geometry and reference shared 'connectors';
we synthesize OSM-style topology: every connector becomes a shared node id, and
interior geometry points become unique filler nodes. Road class maps onto the
OSM highway= vocabulary the engine's spec rules expect.

Overture data: (c) Overture Maps Foundation; OSM-derived portions ODbL.
"""
import gzip
import hashlib
import json
import math
import os
import sys
import time

STEP = 0.05
BOUNDS = (14.20, 120.85, 14.95, 121.25)

CLASS_MAP = {
    "motorway": "motorway", "trunk": "trunk", "primary": "primary",
    "secondary": "secondary", "tertiary": "tertiary",
    "residential": "residential", "living_street": "living_street",
    "unclassified": "unclassified", "service": "service",
}


def hid(s):
    return int.from_bytes(hashlib.blake2b(s.encode(), digest_size=7).digest(), "big")


def cell_of(lat, lon):
    return (math.floor(lat / STEP), math.floor(lon / STEP))


def cell_name(ci):
    la, lo = ci
    return f"c{round(la * STEP * 100)}_{round(lo * STEP * 100)}"


def main(geojson_path, out_dir):
    t0 = time.time()
    cells = {}
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    n_seg = 0
    with open(geojson_path) as f:
        for line in f:
            line = line.strip().rstrip(",")
            if '"Feature"' not in line:
                continue
            try:
                ft = json.loads(line)
            except json.JSONDecodeError:
                continue
            props = ft.get("properties", {})
            klass = CLASS_MAP.get(props.get("class") or props.get("road_class"))
            if klass is None or ft["geometry"]["type"] != "LineString":
                continue
            coords = ft["geometry"]["coordinates"]
            if len(coords) < 2:
                continue
            seg_id = hid(str(ft.get("id") or props.get("id") or json.dumps(coords[:2])))
            connectors = props.get("connectors") or props.get("connector_ids") or []
            # node ids: endpoints from connectors when present (shared topology),
            # interior points unique to this segment
            refs, nodes = [], {}
            for i, (lon, lat) in enumerate(coords):
                if i == 0 and len(connectors) > 0:
                    nid = hid(str(connectors[0].get("connector_id", connectors[0])
                                  if isinstance(connectors[0], dict) else connectors[0]))
                elif i == len(coords) - 1 and len(connectors) > 1:
                    last = connectors[-1]
                    nid = hid(str(last.get("connector_id", last)
                                  if isinstance(last, dict) else last))
                else:
                    nid = hid(f"{seg_id}:{i}")
                refs.append(nid)
                nodes[nid] = (lat, lon)
            tags = {"highway": klass}
            ar = props.get("access_restrictions") or []
            if any((a.get("access_type") == "denied") for a in ar if isinstance(a, dict)):
                tags["access"] = "private"
            n_seg += 1
            lats = [c[1] for c in coords]
            lons = [c[0] for c in coords]
            s, w_, n, e = BOUNDS
            if max(lats) < s or min(lats) > n or max(lons) < w_ or min(lons) > e:
                continue
            c0 = cell_of(max(min(lats), s), max(min(lons), w_))
            c1 = cell_of(min(max(lats), n), min(max(lons), e))
            for la in range(c0[0], c1[0] + 1):
                for lo in range(c0[1], c1[1] + 1):
                    cell = cells.setdefault((la, lo), {"nodes": {}, "ways": []})
                    cell["ways"].append({"id": seg_id, "nodes": refs, "tags": tags})
                    cell["nodes"].update(nodes)

    os.makedirs(out_dir, exist_ok=True)
    index = {"generated": ts, "source": "overture-transportation",
             "step_deg": STEP, "bounds": BOUNDS, "cells": []}
    for ci, cell in sorted(cells.items()):
        name = cell_name(ci)
        payload = {"source": "overture-transportation", "timestamp": ts,
                   "nodes": [{"id": i, "lat": la, "lon": lo}
                             for i, (la, lo) in cell["nodes"].items()],
                   "ways": cell["ways"]}
        with gzip.open(os.path.join(out_dir, f"{name}.json.gz"), "wb",
                       compresslevel=9) as f:
            f.write(json.dumps(payload, separators=(",", ":")).encode())
        index["cells"].append({"name": name, "ways": len(cell["ways"])})
    with open(os.path.join(out_dir, "index.json"), "w") as f:
        json.dump(index, f)
    print(f"overture segments used: {n_seg}; cells: {len(cells)} ({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
