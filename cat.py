#!/usr/bin/env python
# coding: utf-8

import sys
import fileinput
from pathlib import Path

def cat(fn):
    if Path(fn).exists():
        for n, line in enumerate(fileinput.input()):
            line = line.replace('\n', '')
            print('{0}：{1}'.format(n, line))
    else:
        print("ファイル名が間違っています")
        
args = sys.argv

if 2 <= len(args):
    for i in range(1,len(args)):
        cat(args[i])
else:
    print('ファイル名を入力してください')
