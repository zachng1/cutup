# Cutup

## A William S. Burroughs emulator
Okay, maybe Burroughs didn't invent the technique. But he perfected it.

## Usage
`cutup.py [-f num] [-c num] file1.docx file2.docx ... fileN.docx output.docx`

Where either `-f` or `-c` must be used. 

-c num: implements the 'cutup' method, whereby Burroughs would randomly cut pages and shuffle them about. num here signifies the max length possible for a cut. i.e. if num=10, you will end up with continuous lines of text between 1 and 10 from each text  

-f num: implements the 'foldin' method, whereby Burroughs would fold two pages in half and layer them down the middle. num here signifies how many words to read from one text before 'folding in' the next.

In both cases, specify at least 3 .docx files: 2 to mix together, and the 3rd as output. The output file need not already exist. You can mix as many files as you like, however the wordcount of the output will be as long as that of the shortest.
