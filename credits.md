# SpaceSyntaxApp — Credits and licences

_Last updated: 17 October 2026_

SpaceSyntaxApp stands on four decades of space syntax research and on the open-source software and open data
that research produced. This page names the people and works behind it. Errors and simplifications in the app
are ours, not theirs.

## The theory the app puts to work

- **Bill Hillier and Julienne Hanson**: *The Social Logic of Space* (1984), the founding work of space syntax;
  and Bill Hillier, *Space is the Machine* (1996): configuration, natural movement, centrality.
- **Alasdair Turner**: angular segment analysis (2001) and the "tulip" bin approximation that the app's engine
  follows (1,024 bins).
- **Bill Hillier, Tao Yang and Alasdair Turner**: "Normalising least angle choice in Depthmap" (*Journal of
  Space Syntax*, 2012), the source of the NACH and NAIN measures the app reports.

## How street networks are prepared

- **Ioanna Kolovou, Jorge Gil, Kayvan Karimi, Stephen Law and Lucas Versluis**: road-centre-line simplification
  principles for angular segment analysis (Space Syntax Symposium 11, 2017), the basis of the app's automatic
  clean-up rules; and their work on "edge effects" in street-network analysis (*Environment and Planning B*, 2017),
  which is why every study is computed on a buffered network (twice the largest radius).
- **Space Syntax Ltd**: the open model of Great Britain, whose conventions guide the app's validation.
- **QGIS Space Syntax Toolkit** (SpaceGroupUCL/qgisSpaceSyntaxToolkit): Jorge Gil and contributors, with the
  road-centre-line cleaner and network segmenter by Ioanna Kolovou (Space Syntax Ltd). The app's duplicate-removal
  and endpoint-healing rules follow that cleaner.

## depthmapX, the software the app's engine is ported from

The app's analysis engine is a port, written in Rust, of the angular segment analysis in **depthmapX**: its
radius-bounded traversal follows salalib's `segmtulip.cpp`, with the same queue, coverage rules and tie-breaks,
so that the app computes the same numbers the field publishes. Every result the app reports is checked against
depthmapX.

- **Alasdair Turner** created UCL Depthmap (© 2000–2010 University College London).
- **Tasos Varoudis** has maintained it since 2011 as the open-source **depthmapX** and holds copyright on most of
  its analysis library, salalib, including `segmtulip.cpp`. He took on an academic program that had stopped,
  opened it up and has kept it alive for fifteen years. Without his work there would be nothing to check against.
- **Petros Koutsolampros and Christian Sailer** built the modern depthmapX: the refactor that made salalib
  legible, and `depthmapXcli`, the command-line build the app's validation runs against.
- With contributors at the **UCL Space Syntax Laboratory**.

depthmapX is free software under the **GNU General Public License, version 3**:
https://github.com/SpaceGroupUCL/depthmapX

## What the maps are made of

- **Street networks** © **OpenStreetMap contributors**, under the Open Database License (ODbL):
  https://www.openstreetmap.org/copyright. Data exported from the app is ODbL open data.
- **Geofabrik**: the OpenStreetMap extracts behind the app's ready-made Philippine network cells.
- **Satellite imagery** © **Esri** World Imagery, with Maxar, Earthstar Geographics and the GIS User Community.

## Contact

Leandro Nicholas R. Poco: bydesign@consilio.ltd

Privacy: see the [privacy policy](privacy-policy.md).
