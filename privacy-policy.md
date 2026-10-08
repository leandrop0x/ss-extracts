# SpaceSyntaxApp — Privacy Policy

_Last updated: 8 October 2026_

SpaceSyntaxApp is a space syntax analysis tool for street networks. It is
made by Leandro Nicholas R. Poco (Consilio Operazioni Inc., Metro Manila,
Philippines).

**The short version: the app has no accounts, no analytics, no advertising and
no tracking of any kind. Your studies stay on your device.**

This policy covers the SpaceSyntaxApp apps for Android, iPhone and iPad, and
Mac. Where a platform differs, the text says so; the table at the end of
"What leaves your device" gathers it in one place.

## What the app does with your location

If you tap the location button on the pin screen or the map-region screen, or
choose to start the tutorial from where you are, the app asks Android or iOS
for your current position and uses it to centre the map (for the tutorial, to
place a small first study there). That coordinate is used on the device to choose which part of the world
to analyse. It is not stored by us, not attached to any identity, and not sent
to us — we operate no servers and receive nothing.

You never have to use it. You can type coordinates or pan the map instead, and
the app works identically; the tutorial runs on a sample study included with
the app instead.

## What leaves your device

To draw a map and analyse a street network, the app requests data from public
services, exactly as any map application does. Those requests necessarily
reveal your device's IP address and the map area being requested to the
service concerned:

- **OpenStreetMap road-centre-line data**, from pre-built extracts hosted on
  GitHub and, where no extract exists, from public Overpass API servers
  (currently four public instances: overpass-api.de, overpass.kumi.systems,
  maps.mail.ru and overpass.private.coffee; the app tries them in turn and the
  list may change). The request names the area
  being studied.
- **Satellite imagery tiles**, from Esri's World Imagery service.
- **Apple's map search, only if you type in the search field** (iPhone, iPad
  and Mac). What you type, together with the area the map is showing so that
  suggestions are nearby ones, is sent to Apple's map search. Street and
  square names from the maps already on your device are searched on the
  device and never sent; nothing goes to Apple unless you type. The Android
  app has no Apple search.
- **The Mac app's update check.** Once a day at most, the Mac app checks a
  small file on GitHub to see whether a newer build exists. It sends nothing
  about you or your studies.

These services have their own privacy practices, which we do not control. The
map, imagery and search requests carry the map area you are working in —
which, if you used the location button or started the tutorial from where you
are, is derived from where you were standing.

| | Android | iPhone / iPad | Mac |
|---|---|---|---|
| Map and street data (GitHub extracts, Overpass) | yes | yes | yes |
| Satellite imagery (Esri) | yes | yes | yes |
| Apple map search (only when you type) | no | yes | yes |
| iCloud copy of a study's setup | no | yes, if you use iCloud | yes, if you use iCloud |
| Daily update check (GitHub) | no | no (updates come through the App Store / TestFlight) | yes |

Nothing else leaves the device. The street networks you analyse, the results,
your manual corrections and your notes are written to the app's private
storage on the device.

## Sync between your own devices

On Apple devices, the app can copy a study's *setup* — its pin, radii and your
manual corrections, around two kilobytes — through your own private iCloud
account, so the same study appears on your other Apple devices. That data is
held in your iCloud account, not by us, and we cannot see it. Results are
never synced. This feature does not exist on Android, where studies remain
local to the device. It is optional and works only if you are signed in to
iCloud with the app allowed to use it.

## Exports

Exported files — analysis bundles, atlas PDFs, snapshots — are written to your
device. They go somewhere else only when you deliberately share them.

## Children

The app is a professional research tool and is not directed at children.

## Deletion

Deleting a study inside the app deletes it from the device. Uninstalling the
app removes everything it stored. As we hold no data about you, there is
nothing for you to request from us.

## Changes

If this policy changes, the revised version will be published at this address
with a new date at the top.

## Contact

Leandro Nicholas R. Poco — leandro.poco@gmail.com

---

Street network data © OpenStreetMap contributors, licensed under the Open
Database License (ODbL). Imagery © Esri and its data providers.
