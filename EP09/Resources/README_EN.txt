EP09 supported Blender box prop workflow

Start: Woodland_Arch_Start.blend (Beam X dimension4.4).
Edited model: Woodland_Arch_Final.blend (Beam X dimension4.8).
All eight objects are explicit native boxes. Object rotation must be zero, dimensions positive, box mesh centred, no parent/modifiers. No arbitrary FBX/GLB, materials, textures, rigs or animation import is claimed.

BLENDER4.2 LTS
File > Open the starter. Object Mode > select EP09_Beam. Inspect Transform > Dimensions. Edit the width if useful; exact shown numbers are examples. File > Save As a distinct.blend.
Scripting > select embedded EXPORT_Miliastra_Boxes.py > review > Run Script once. File > Export > Miliastra Boxes(.json). Choose a fresh filename and useful Game Origin.
Position mapping is (x,y,z) > (x,z,-y)+GameOrigin; dimensions(X,Y,Z) > (X,Z,Y). One Blender unit is represented as one native box scale unit; no metre-size equivalence is asserted. Simple opaque RGB object colours map to native display colour; no shader import.

CONVERTER / WINDOWS POWERSHELL
Install Python3.14 if needed: https://www.python.org/downloads/windows/
Extract Resources. Open a terminal in Primitive_Kit (the folder with convert_boxes.py, requirements.txt, Template and miliastra_core). Run each following command as one complete line:
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe convert_boxes.py ..\Woodland_Arch_Placed.json My_Arch.gia

Replace the JSON path for your own export. Choose a new output filename. A successful run writes My_Arch.gia, My_Arch.objects.json and My_Arch.readback.json. The source kit is relative-path based; keep its folders together. A local virtual environment was created from scratch and successfully reproduced all eight object records with Python3.14/protobuf6.33.6. It does not install a game-side script or modify global Python packages.

IMPORT IN THE GAME
First use an empty Beyond Mode practice save. System Menu > Manage Asset Import Export > Import and Transfer > Load External Assets > choose.gia. Select the intended Asset Pack and read/confirm Transfer Assets, including the undo-history notice. Assets Exporting > Entity should list8 EP09 objects. Use private Test Play and inspect front, side, orientation, colours and useful placement at player height.

EXACT NATIVE CHECKS
Woodland_Arch_Final.gia: origin(8,0,16), eight objects imported/listed in empty Woodland EP09 Asset Sandbox; visible complete prop, approach and orbit. The same placement overlapped a tree in a separate woodland candidate.
Woodland_Arch_Placed.gia: origin(16,0,16), same geometry/colour in fresh Woodland Workshop EP09 R01 Final. Actual private-play approach/orbit showed arch clear of tree while original path/pavilion/coins/HUD remained visible. F not pressed. These coordinates are examples.
The final whole-save Woodland_EP09_R01_Final.gil is included, but that exact.gil has NOT been separately reimported. Its save and its private-play evidence are distinct from an export reimport check.
Collision and climbing are disabled in conversion/readback. No collision traversal acceptance, new natural timed result, public release or multiplayer test is claimed here.

LICENSE / SOURCE
Miliastra-Tools by Ayn1631: https://github.com/Ayn1631/Miliastra-Tools
GPL3 license, exact corresponding source and local-update notice are included under Primitive_Kit. Exporter and wrapper source are supplied under GPL-3.0-or-later. The source notice identifies copied writer bytes; the historical base commit alone does not identify pre-existing updates.
