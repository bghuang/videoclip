#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Huang, Baogui'

import os
import argparse

def cut(filename, start, end, cuttype):
    assert os.path.exists(filename) is True, "The source file is ont exists."
    videoname = "./" + filename.split(".")[0] + "_clip.mp4"
    if cuttype == 'exact':
        cmd = "ffmpeg -ss {}  -i {}   -c:v libx264 -c:a aac  -strict experimental -to {} {}".format(start,filename, end, videoname)
    elif cuttype == 'fast':
        cmd = "ffmpeg -ss {} -accurate_seek -i {} -c copy -to {} -avoid_negative_ts 1 -copyts {}".format(start, filename, end, videoname)
    elif cuttype == 'fastwithoutcarekeyframe':
        cmd = "ffmpeg -i {} -ss {} -c copy -to {} -copyts {}".format(filename, start, end, videoname)
    else:
        print("截取类型必须是: fast, fastwithoutcarekeyframe 或者 exact")
        print("Cut type must be fast, fastwithoutcarekeyframe or exact")
        return
    os.system(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This tool used to cut vidoe fiile. Author: Huang, Baogui ")
    parser.add_argument("videoname")
    args = parser.parse_args()
    file = os.path.basename(args.videoname)
    print("作者 Author: 黄宝贵 Huang, BAogui; 邮件 Email: bghuang@foxmail.com")
    print("开始裁剪视频文件(Start cut vidoe file):  %s" % (file))

    start = input("起始时间 Start Time (HH:MM:SS): ")
    end = input("结束时间 End Time (HH:MM:SS): ")
    cuttype = input("截取方式 cut type（exact,fast,fastwithoutcarekeyframe):")
    cut(file, start, end, cuttype)
