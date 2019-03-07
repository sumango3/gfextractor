# gfextractor
girl's frontline image extractor
need [unitypack]: https://github.com/HearthSim/UnityPack with [ETC, ETC2 support]: https://github.com/HearthSim/UnityPack/pull/52

## Usage
run following script with python3

python3 gfextractor.py AssetbundlePath ExtractPath PatchPath

You should provide 3 paths to run extractor properly.

AssetbundlePath is path where Assetbundle locate.
You can copy assetbundle folder from your device.
Default path of game is /sdcard/Android/data/id of game/files/New

ExtractPath is path where images will be extracted.
This program will extract all images from Assetbundles.

PatchPath is path where patched images will be saved.
Girls Frontline separate RGB information and Alpha information, so this program will merge them.
