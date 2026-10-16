# SpaceSyntaxApp — Privacy Policy

_Last updated: 17 October 2026_

SpaceSyntaxApp is a space syntax analysis tool for street networks. It is
made by Leandro Nicholas R. Poco (Consilio Operazioni Inc., Metro Manila,
Philippines).

**The short version: no accounts, no advertising, no tracking, and we run no
servers. Your studies stay on your device unless you send or sync them
yourself. Two parts of the Android app, its update check and its QR-code
scanner, send the technical details described below to their makers.**

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

If you turn on Drive sync, a study's pin — a place you chose on the map — is
kept in your own Google Drive, as described under "Sync between your own
devices".

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
- **The Android app's update check (Shorebird).** When the Android app starts,
  it asks Shorebird, the service that delivers its updates, whether a newer
  version exists. It sends the app's identifier and version, the phone's
  platform and processor type, the update it currently has, and a random
  install number that Shorebird uses to count installations. It sends nothing
  about you, your location or your studies.
- **The QR-code scanner (Google ML Kit), when you receive a study by
  scanning.** The code is read on the device; the camera picture never leaves
  it. Google's scanning component sends Google technical diagnostics: the
  device's make, model and OS version, the app's name and version, and how fast
  scanning ran. Google says it does not pass this to third parties. On iPhone,
  iPad and Mac, scanning uses Apple's built-in vision and sends nothing.
- **Google Drive, only if you turn on "Sync pins with Google Drive"**
  (Android). See "Sync between your own devices".

These services have their own privacy practices, which we do not control. The
map, imagery and search requests carry the map area you are working in —
which, if you used the location button or started the tutorial from where you
are, is derived from where you were standing.

| | Android | iPhone / iPad | Mac |
|---|---|---|---|
| Map and street data (GitHub extracts, Overpass) | yes | yes | yes |
| Satellite imagery (Esri) | yes | yes | yes |
| Apple map search (only when you type) | no | yes | yes |
| Sync of a study's setup | Google Drive, if you turn it on | iCloud, if you use iCloud | iCloud, if you use iCloud |
| Update check | Shorebird, at launch | no (App Store / TestFlight) | GitHub, daily |
| QR scanner diagnostics (only when you scan) | Google ML Kit | no | no |
| Nearby transfer | local network only | local network only | local network only |

Nothing else leaves the device. The street networks you analyse, the results,
your manual corrections and your notes are written to the app's private
storage on the device.

## Sync between your own devices

On Apple devices, the app can copy a study's *setup* — its pin, radii, name
and your manual corrections, around two kilobytes — through your own private
iCloud account. On Android, if you turn on **Sync pins with Google Drive** (off
unless you turn it on), the same setup is kept in a hidden app folder in **your
own Google Drive**, which only this app can read. The app asks Google for
access to that folder alone, not to your other files. In both cases the data
sits in your account, not with us, and we cannot see it. Results are never
synced. Turning sync off stops it and deletes nothing. To remove the copies,
delete the app's hidden data in Google Drive (Settings → Manage apps →
SpaceSyntaxApp → Delete hidden app data) or in iCloud settings. iCloud and
Google Drive do not sync with each other.

## Sending a study to a nearby device

*Send to another device → Nearby* sends a finished study straight to your
other device over the same Wi-Fi or a phone hotspot. It never goes over the
internet, and nothing passes through us or anyone else. The sending device
shows a code that works once, for one download, for at most ten minutes; the
receiving device refuses anything not on the local network. The camera is used
only to read that code, on the device. iPhone and iPad ask once for permission
to use the local network.

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

Leandro Nicholas R. Poco — bydesign@consilio.ltd

---

Street network data © OpenStreetMap contributors, licensed under the Open
Database License (ODbL). Imagery © Esri and its data providers.
