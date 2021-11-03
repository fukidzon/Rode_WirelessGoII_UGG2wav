# Rode_WirelessGoII_UGG2wav

Converting UGG files from Rode Wireless Go II transmitters (uncompressed recordings) to WAV format

## Story
I backuped the .ugg and .egg files from the Wireless Go II transmitters before next recording and I needed to export audio from those files. It was not possible to copy it back to the TX to let it export in the Rode Central app (the error is something like the usb mass storage device is protected). 

The possible solution is to contact Rode customer service and support, upload the files to Wetransfer, send the link and they converted the files to WAV in approx 24hours.

I wanted to be able to do it by myself but there was no existing solution. So I looked into the UGG file and I spotted the 'OggS' - but unfortunately the format of the UGG file doesn't conform really the Ogg file specification (https://en.wikipedia.org/wiki/Ogg#Page_structure) but after some effort comparing the converted WAV file and the original UGG file and some trial and error I was able to extract the 24bit PCM data from the files and save it to WAV file

## USAGE
Python is needed, and installing the wave library (`pip install wave`)

then convert the files with `python ugg2wav.py REC00032.UGG`

Enjoy! :)
