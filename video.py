from moviepy.editor import VideoFileClip, VideoClip, concatenate_videoclips
import random

def createsegments(filelist):
    "take a list of paths and produce a list of videoclips"
    clips = []
    for i in filelist:
        clips.append(VideoFileClip(i))
    return clips

def foldin(cliplist, length):
    a = 0
    duration = min(cliplist, key=lambda x: x.duration).duration
    print(duration)
    result = VideoClip(duration=0)
    result.size=(0,0)
    while result.duration < duration:
        for i in cliplist:
            if (a < i.duration and a + length < i.duration):
                seg = i.subclip(a, a+length)
                result = concatenate_videoclips([result, seg])
    return result

def cutup(cliplist, length):
    segments = []
    result = VideoClip(duration=0)
    result.size=(0,0)

    #use size max and sizemin in this loop to ensure an even distribution of segments
    #also used so final output is only as long as the shortest
    sizemax = max(cliplist, key=lambda x: x.duration).duration
    sizemin = min(cliplist, key=lambda x: x.duration).duration
    a = 0; b = 0
    while b < sizemin:
        c = random.randrange(1, length)
        b += c
        for i in cliplist:
            if (a < i.duration and b < i.duration):
                segments.append(i.subclip(a, b))
        a = b
    random.shuffle(segments)
    result = concatenate_videoclips(segments)
    result = result.subclip(0, sizemin)
    return result

def selectmode(segmentlist, savedir, length, cut):
    if cut:
        result = cutup(segmentlist, length)
        result.write_videofile(savedir)
    else:
        result = foldin(segmentlist, length)
        result.write_videofile(savedir)
