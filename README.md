# Cutup

## A William S. Burroughs emulator
Okay, maybe Burroughs didn't invent the technique. But he ~~perfected~~popularised it (by nature, the cutup is imperfectible). My first python script emulates this powerful tool for disruption of the "One God Universe". It mixes fictions together, with potentially reality-altering results. 

I also assume it is a lot faster than it was in the 60s, and requires less glue and scissors.

## Requirements
Python 3.x
docx for Python: https://python-docx.readthedocs.io/en/latest/user/install.html

## Usage
`cutup.py [-f num] [-c num] file1.docx file2.docx ... fileN.docx output.docx`

Where either `-f` or `-c` must be used. 

-c num: implements the 'cutup' method, whereby Burroughs would randomly cut pages and shuffle them about. num here signifies the max length possible for a cut. i.e. if num=10, you will end up with continuous lines of text between 1 and 10 from each text  

-f num: implements the 'foldin' method, whereby Burroughs would fold two pages in half and layer them down the middle. num here signifies how many words to read from one text before 'folding in' the next.

In both cases, specify at least 3 .docx files: 2 to mix together, and the 3rd as output. The output file need not already exist. You can mix as many files as you like, however the wordcount of the output will be as long as that of the shortest.

## Todo
I plan to add a simple GUI (currently learning c++ so I can do this in Qt) down the line, as well as adding an audio option (Burroughs used the technique on both text and magnetic tape). 

