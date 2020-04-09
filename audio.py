from pydub import AudioSegment
import random

def createsegments(filelist):
    """Take a list of paths and produce a list of audiosegments"""
    segments = []
    for i in filelist:
        f_format = i[i.rfind('.')+1:].rstrip()
        file = AudioSegment.from_file(i, format=f_format)
        segments.append(file)
    return segments

def foldin(segmentlist, segmentlength):
    result = AudioSegment.empty()
    size = len(min(segmentlist, key=len))
    a = 0; b = a + segmentlength
    while len(result) < size:
        for i in segmentlist:
            result += i[a:b]
            a = b
            b += segmentlength
    return result
    
def cutup(segmentlist, length):
    segments = []
    resultlength = 0
    result = AudioSegment.empty()

    #use size max and sizemin in this loop to ensure an even distribution of segments
    #also used so final output is only as long as the shortest
    sizemax = len(max(segmentlist, key=len))
    sizemin = len(min(segmentlist, key=len))
    a = 0; b = 0
    while b < sizemax:
        c = random.randrange(1, length)
        b += c
        for i in segmentlist:
            segments.append(i[a:b])
            resultlength += c
        a = b
    random.shuffle(segments)
    for i in segments:
        result += i

        #this saves time -- otherwise result too long
        resultlength += len(i)
        if resultlength > sizemin:
            break
    return result

def selectmode(segmentlist, savedir, length, cut):
    if cut:
        result = cutup(segmentlist, length)
        f_format = savedir[savedir.rfind('.')+1:].rstrip()
        result.export(savedir, format=f_format)
    else:
        result = foldin(segmentlist, length)
        f_format = savedir[savedir.rfind('.')+1:].rstrip()
        result.export(savedir, format=f_format)
