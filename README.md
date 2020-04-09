# Cutup

## A William S. Burroughs emulator
Okay, maybe Burroughs didn't invent the technique. But he ~~perfected~~popularised it (by nature, the cutup is imperfectible). My first python script emulates this powerful tool for disruption of the "One God Universe". It mixes fictions together, with potentially reality-altering results. 

I also assume it is a lot faster than it was in the 60s, and requires less glue and scissors.

## Requirements
Python 3.x: https://www.python.org/downloads/

docx for Python: https://python-docx.readthedocs.io/en/latest/user/install.html

pydub for Python: https://github.com/jiaaro/pydub#installation

ffmpeg (for pydub and non-wav audio files): https://www.ffmpeg.org/download.html

moviepy for Python: https://zulko.github.io/moviepy/install.html
## Usage
`control.py [-mvh][-f num] [-c num] file1.ext file2.ext ... fileN.ext output.ext`

Where either `-f` or `-c` must be used. 

`-c num`: implements the 'cutup' method, whereby Burroughs would randomly cut pages and shuffle them about. num here signifies the max length possible for a cut. i.e. if num=10, you will end up with continuous lines of text between 1 and 10 from each text  

`-f num`: implements the 'foldin' method, whereby Burroughs would fold two pages in half and layer them down the middle. num here signifies how many words to read from one text before 'folding in' the next.

`-h`: prints help.

`-m`: optional flag, specifies that you are mixing audio files.

`-v`: optional flag, specifies that you are mixing video files.

In all cases, specify at least 3 files: 2 to mix together, and the 3rd as output. The output file need not already exist. You can mix as many files as you like, however the wordcount of the output will be as long as that of the shortest.

When mixing text, please use .docx or .doc files. 

When mixing audio, you *should* be able to use any format supported by pydub/ffmpeg and the script will pick up the format from the file extension. You can mix any number of formats into any output format -- when specifying output, make sure to add the extension you want.

### Text example
`$python3 control.py -f10 path/to/text1.docx path/to/text2.docx path/to/text3.docx path/to/output.docx`

`Done. Output saved at path/to/output.docx`

### Music example
`$python3 control.py -m -f5 path/to/track1.mp3 path/to/track2.wav path/to/track3.flv path/to/output.mp3`

`Done. Output saved at path/to/output.mp3`

### Video example
`$python3 control.py -v -c2 'path/to/video1.mp4' 'path/to/video2.mp4' 'output.mp4`

`Moviepy - Building video output.mp4.
MoviePy - Writing audio in outputTEMP_MPY_wvf_snd.mp3
MoviePy - Done.
Moviepy - Writing video output.mp4
Moviepy - Done !
Moviepy - video ready output.mp4`