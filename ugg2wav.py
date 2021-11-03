# Converting UGG files from Rode Wireless Go II transmitters (unsompressed recordings) to WAV format
# Author: Jan Mazanec, https://github.com/fukidzon, jmazanec@gmail.com
# 3.11.2021
# needed libraries: wave (install as `pip install wave`)

# usage: `python ugg2wav.py REC00032.UGG`
# created WAV file is then REC00032.UGG.wav

import sys
import wave

# get filename and read the lines
if not len(sys.argv) > 1:
    sys.exit("provide a filename")
filename = sys.argv[1] 
try:
    with open(filename, 'rb') as f:
        s = f.read()
except IOError as e:
    sys.exit("Couldn't open file {}.".format(e))

def get_data_from_frame(frame):
    if frame[5]!=0:
        return []
    else:
        return frame[44:] # at byte 44 the data starts, hard to say what is the first 44bytes, because it doesn't really conform the Ogg stadard 

#print("length: ", len(s))

data = b''
data_list = []
    
frame_start = s.find(b'OggS',0) # The UGG format is similar to Ogg format, but not compatible. But in The UGG files, OggS marks new page of data 
while frame_start != -1:
    
    frame_end = s.find(b'OggS', frame_start + 4)
    frame_type = s[frame_start+5] # 2 is starting frame, 0 is frame with data, 4 is end frame
    if frame_type == 0:
        #data += get_data_from_frame(s[frame_start:frame_end]) # appending is slow, joining array is much faster
        data_list.append(get_data_from_frame(s[frame_start:frame_end]))
    #print(frame_start, frame_end, frame_end-frame_start, frame_type)
    # print progress
    #print("{:.1f}%".format(100*frame_start/len(s)))
    frame_start = frame_end

data = b''.join(data_list)

with wave.open(filename + ".wav", "w") as f:
    f.setnchannels(1)
    f.setsampwidth(3)
    f.setframerate(48000)
    f.writeframes(data)

