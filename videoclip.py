#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def cut(filename, start, end, cuttype):
    assert os.path.exists(filename) is True, "The source file is ont exists."
    videoname = "./" + filename.split(".")[0] + "_clip.mp4"
    print(videoname)
    if cuttype == 'exact':
        cmd = "ffmpeg -ss {}  -i {}   -c:v libx264 -c:a aac  -strict experimental -to {} {}".format(start,filename, end, videoname)
    if cuttype == 'fast':
        cmd = "ffmpeg -ss {} -accurate_seek -i {} -c copy -to {} -avoid_negative_ts 1 -copyts {}".format(start, filename, end, videoname)
    if cuttype == 'fastwithoutcarekeyframe':
        cmd = "ffmpeg -i {} -ss {} -c copy -to {} -copyts {}".format(filename, start, end, videoname)

    os.system(cmd)


if __name__ == "__main__":
    file = input("需要截取的视频： ")
    start = input("起始时间(HH:MM:SS): ")
    end = input("结束时间(HH:MM:SS): ")
    cuttype = input("截取方式（exact,fast,fastwithoutcarekeyframe):")
    cut(file, start, end, cuttype)
