# Miliastra Workshop: From Scene to Adventure

A nine-lesson English tutorial series following one woodland from a first scene through a playable native-node challenge and one supported Blender prop conversion.

**[Watch the series on YouTube](https://www.youtube.com/playlist?list=PLLfS04BK3lXo)**

**[Download all viewer resources](https://github.com/breadtitor/miliastra-workshop-tutorials/releases/latest/download/Miliastra_Workshop_Viewer_Resources.zip)** · [Release notes](https://github.com/breadtitor/miliastra-workshop-tutorials/releases)

The download is about 46 MB. Extract the whole ZIP before opening the illustrated guides. The episode folders here contain the same guide/resource files for browsing; HTML guides are designed to open locally with their neighbouring Guide images. All game/editor pictures are genuine captures. Main-course logic uses native tools and node graphs, without Lua.

## Watch the series

All nine lessons are now public. Start with Episode 01 and follow the episode numbers in the playlist.

| Episode | Lesson | Video | Guide |
|---|---|---|---|
| 01 | Open the editor and build your first scene | [Watch](https://youtu.be/N1nxsRfl1ic) | [Guide](EP01/EP01_Follow_Along_EN.md) |
| 02 | Build a scenic woodland | [Watch](https://youtu.be/-zKzMCAJatI) | [Guide](EP02/EP02_Follow_Along_EN.html) |
| 03 | Save, export and import | [Watch](https://youtu.be/QTfudcR40Uw) | [Guide](EP03/EP03_Follow_Along_EN.html) |
| 04 | Collect coins with native node graphs | [Watch](https://youtu.be/ddoFuHP8dpA) | [Guide](EP04/EP04_Follow_Along_EN.html) |
| 05 | Bind a live progress bar | [Watch](https://youtu.be/Ko8-pqRldas) | [Guide](EP05/EP05_Follow_Along_EN.html) |
| 06 | Start and finish a two-minute challenge | [Watch](https://youtu.be/B2L9fElFT6Q) | [Guide](EP06/EP06_Follow_Along_EN.html) |
| 07 | Configure ordinary and Ultimate achievements | [Watch](https://youtu.be/4KEup2TveAs) | [Guide](EP07/EP07_Follow_Along_EN.html) |
| 08 | Diagnose a binding fault and verify a restored save | [Watch](https://youtu.be/242Nbm00q-w) | [Guide](EP08/EP08_Follow_Along_EN.html) |
| 09 | Convert a supported Blender box prop | [Watch](https://youtu.be/8TBHKgbapNI) | [Guide](EP09/EP09_Follow_Along_EN.html) |

## Follow along

- Start with your own separate lesson save and preserve the previous working version. Example scenery coordinates and sizes are design choices, not values you must copy.
- `.gil` is a whole-save export: use Local Save → Import Save and distinguish the new card.
- `.gia` contains native assets: use Manage Asset Import Export → Import and Transfer. Graph-only assets may require Player/coin variables, trigger components or layouts explained in the guide.
- Read the README and resource identity file in each Resources folder. Native import, structural readback, private play and full natural settlement checks have different scopes.
- EP09's supplied starter uses eight explicit axis-aligned boxes. Read [its detailed instructions](EP09/Resources/README_EN.txt) and keep the [complete converter source](EP09/Resources/Primitive_Kit) together with its template. General textured/rigged mesh import is outside this example.

## Included material and verification

The release contains illustrated English guides, subtitles, supplied lesson saves/assets, Blender starter/final projects and the exact corresponding conversion source and licenses. It excludes videos, raw recordings, editing projects, internal logs and private evidence.

EP08's exact whole-save export was separately imported and completed a natural120-second Victory/5 Coins test. EP09's Final and Placed GIA assets were actually imported and inspected; its final whole-save GIL was exported but was not separately reimported. No multiplayer, permanent-account award or public gameplay acceptance is implied by these private lesson checks.

## Attribution and code licensing

- Game/editor imagery is captured from Genshin Impact/Miliastra Wonderland. This is an independent tutorial, not an official HoYoverse course.
- The course layout credits and licenses are included with the guides. Their original images are the author's game captures.
- EP09's converter contains GPL3 source from [Ayn1631/Miliastra-Tools](https://github.com/Ayn1631/Miliastra-Tools), with full [license](EP09/Resources/Primitive_Kit/License.txt) and [exact-source/local-update notice](EP09/Resources/Primitive_Kit/SOURCE_NOTICE.json). The exporter and wrapper source are supplied under GPL-3.0-or-later.
- Code licenses apply to the identified code. They do not relicense game imagery/assets or third-party material. Follow each included notice when redistributing.

## Integrity

Release ZIP SHA256:

```
4386133b01339c8dd28fd29ac08318da9bbe58a00586986f13628aa536a12f26  Miliastra_Workshop_Viewer_Resources.zip
```

[RESOURCE_MANIFEST.json](RESOURCE_MANIFEST.json) records the individual resource files. The tutorial video descriptions link here so viewers can obtain the exact provided materials.
