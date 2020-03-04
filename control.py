import text
import sys

def main():
    paths = text.getargs(sys.argv[1:])
    if not paths:
        return
    elif paths[0][0] == '-c':
        x = True
    else:
        x = False
    documents = []
    for i in paths[1][:-1]:
        documents.append(text.scanfile(i))
    documents = text.stringsplit(documents)
    text.choose(documents, paths[1][-1], length=int(paths[0][1]), cut=x)
    print("Done, output saved at %s" % paths[1][-1])

    


if __name__ == '__main__':
    main()