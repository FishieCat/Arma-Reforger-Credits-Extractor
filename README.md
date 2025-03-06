# Arma-Reforger-Credits-Extractor
Extracts Arma Reforger credits from credits.conf into Mobygames import format-ish

# Requirements

* Python 3 must be installed
* You need to know how to open a console in a folder in Windows (shift+rightclick on the white background of a folder, then open console or powershell or cmd or maybe you have [git](https://git-scm.com/downloads/win) bash installed (highly recommended for least amount of bullshit) or something)

#  How to extract and convert credits from Arma Reforger

1. Download [PakEntpacker](https://github.com/Rendszerguru/PakEntpacker/releases/tag/PakEntpacker) and extract it into `Arma Reforger\addons\data`
2. Double-click `PakEntpacker.exe` go do stuff till it finishes - maybe 5-20 minutes?
3. Continue working in `Arma Reforger\addons\data\data005\Configs\Credits` or copy `Arma Reforger\addons\data\data005\Configs\Credits\credits.conf` to a working folder
4. Download the `armareforger2moby.py` file from this repository next to `credits.conf`
5. Open a console and run `python armareforger2moby.py credits.conf`
6. Do a little dance 🕺💃 because now you don't have to manually type czech accents/diacritics yourself or make lots of typos
7. Manually cleanup role titles in `credits.conf_moby_wip.txt`, maybe add groups
8. The legal notices are in `Arma Reforger\addons\data\data005\Language\localization.en_us.conf` but watch out, at least one has a similar but different string. You have ok CTRL+F skills, as in searching multiple times and then comparing the text using your eyes, right? right.

# Screenshot proof

1. Use [JDownloader](https://jdownloader.org/download/index) or anything that currently works to download a video of the credits or record one with OBS
2. Play the video back in [mpv](https://mpv.io/installation/) and take screenshots IN CORRECT ORDER by pressing 's'. This creates jpg files on the Desktop called `mpv-shot0001.jpg` etc.
3. Move these jpgs to a working folder (do not work on the desktop unless you want to fuck up all files in all folders there - you have been warned)
4. Have [imagemagick](https://imagemagick.org/) installed
5. Open a bash console in the screenshot working folder
6. Run `mkdir -p box; for i in *jpg *png; do magick convert $i -gravity east -crop 640x800+0+0 -colors 8 box/$i.png;done`
7. Now you should have readable-ish, 65ish in number, less than 2MBish in total size, cropped-ish screenshots of the credits area of each screenshot you took in the `box` folder
8. Ignore the copyright notice at the bottom center, it's included on the last page of the credits—in my version at least
