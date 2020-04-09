import text
import audio
import video

import sys
import getopt

def main():
    options, files = getargs(sys.argv[1:])
    #check options
    if not options:
        usage()
        return 
    if len(files) < 3:
        print("Requires at least 3 non-option arguments: 2 files to mix together, a 3rd as output.", file=sys.stderr)          
        return (0, 0)
    m_flag, v_flag, f_flag, c_flag = False, False, False, False
    for ind, i in enumerate(options):
        if i[0] == 'h':
            usage()
            return
        if i[0] == '-c':
            c_flag = True
            modeindex = ind
        if i[0] == '-f':
            f_flag = True
            modeindex = ind
        if i[0] == '-m':
            m_flag = True
        if i[0] == '-v':
            v_flag = True
    #make sure we have exactly 1 of '-c' or '-f'
    if (c_flag and f_flag) or (not (c_flag or f_flag)):
        print("Specify exactly one of '-c' or '-f'", file=sys.stderr)  
    elif not (m_flag or v_flag):
        content = []
        #content gets all files except last -- since last is save file
        for i in files[:-1]:
            content.append(text.scanfile(i))
        content = text.stringsplit(content)
        text.selectmode(content, files[-1], int(options[modeindex][1]), c_flag)
        print("Done, output saved at %s" % files[-1])
        
    elif m_flag and v_flag:
        print("Specify exactly one or zero of '-m' or '-v'", file=sys.stderr)
        
    elif m_flag:
        segments = audio.createsegments(files[:-1])
        #assume length is specified in seconds -- modify to microseconds for pydub
        length = int(options[modeindex][1]) * 1000
        audio.selectmode(segments, files[-1], length, c_flag)
        print("Done, output saved at %s" % files[-1])

    elif v_flag:
        segments = video.createsegments(files[:-1])
        length = int(options[modeindex][1])
        video.selectmode(segments, files[-1], length, c_flag)
        for i in segments:
            i.close()

def getargs(arglist):
    """
    Returns a tuple of options and files to operate on. 
    """
    args = getopt.getopt(arglist, "c:f:hmv")
    #here options is set to a list of option value pairs [(o, v), (o, v)...]
    options = args[0]
    #alphabetise based on option name
    options.sort(key=lambda x: x[0])
    #second element of args is all non-option arguments: in this case files.
    files = args[1]
    return (options, files)

def usage():
    print(
            """
            Usage: 
            control.py [-mh][-f num] [-c num] file1.docx file2.docx ... fileN.docx output.docx

            Where either -f or -c must be used. 

            -c num: implements the 'cutup' method. num signifies the max length possible for a cut. i.e. if num=10, you will end up with continuous lines of text between 1 and 10 from each text.  

            -f num: implements the 'foldin' method. num signifies how many words to read from one text before 'folding in' the next.

            -h: prints help.

            -m: optional flag, specifies that you are mixing audio files.

            In all cases, specify at least 3 files: 2 to mix together, and the 3rd as output. The output file need not already exist. You can mix as many files as you like, however the wordcount of the output will be as long as that of the shortest.

            When mixing text, please use .docx or .doc files. 

            When mixing audio, you *should* be able to use any format supported by pydub/ffmpeg and the script will pick up the format from the file extension. You can mix any number of formats into any output format -- when specifying output, make sure to add the extension you want.
            """
                        )

    


if __name__ == '__main__':
    main()