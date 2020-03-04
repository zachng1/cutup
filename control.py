import text
import audio
import sys
import getopt

def main():
    options, files = getargs(sys.argv[1:])
    #check options
    if not options:
        usage()
        return 
    m_flag, f_flag, c_flag = False, False, False
    for ind, i in enumerate(options):
        if i[0] == '-c':
            c_flag = True
            modeindex = ind
        if i[0] == '-f':
            f_flag = True
            modeindex = ind
        if i[0] == '-m':
            m_flag = True
    #make sure we have exactly 1 of '-c' or '-f'
    if (c_flag and f_flag) or (not (c_flag or f_flag)):
        print("Specify exactly one of '-c' or '-f'", file=sys.stderr)

    if not m_flag:
        content = []
        #content gets all files except last -- since last is save file
        for i in files[:-1]:
            content.append(text.scanfile(i))
        content = text.stringsplit(content)
        text.selectmode(content, files[-1], int(options[modeindex][1]), c_flag)
        print("Done, output saved at %s" % files[-1])
    
    else:
        segments = audio.createsegments(files[:-1])
        #assume length is specified in seconds -- modify to microseconds for pydub
        length = int(options[modeindex][1]) * 1000
        audio.selectmode(segments, files[-1], length, c_flag)
        print("Done, output saved at %s" % files[-1])



def getargs(arglist):
    """
    Returns a tuple of options and files to operate on. 
    """
    args = getopt.getopt(arglist, "c:f:hm")
    #here options is set to a list of option value pairs [(o, v), (o, v)...]
    options = args[0]
    #alphabetise based on option name
    options.sort(key=lambda x: x[0])
    #check for help option
    for i in options:
        if '-h' in i:
            usage()
            return (0, 0)
    #second element of args is all non-option arguments: in this case files.
    files = args[1]
    if len(files) < 3:
        print("Requires at least 3 non-option arguments: 2 files to mix together, a 3rd as output.", file=sys.stderr)          
        return (0, 0)
    return (options, files)

def usage():
    print(
            """Usage: 
            -c num implements the 'cutup' method, whereby Burroughs would randomly cut pages and shuffle them about. num here signifies the max length possible for a cut. 
            -f num implements the 'foldin' method, whereby Burroughs would fold two pages in half and layer them down the middle. num here signifies how many words to read from one text before 'folding in' the next.
            In both cases, specify at least 3 .docx files: 2 to mix together, and the 3rd as output. The output file need not already exist.
            You can mix as many files as you like, however the output will be as long as the shortest"""
            )

    


if __name__ == '__main__':
    main()