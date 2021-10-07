#!/usr/bin/env python
# coding: utf-8

import sys
from pathlib import Path

def cat(fn):
    if Path(fn).exists(): #ファイルが存在するなら
        f = open(fn,"r")
        for n, line in enumerate(f):
            line = line.replace('\n', '') #余計な改行の削除
            print('{0}：{1}'.format(n, line)) #行数とテキストの表示
        f.close()
    else:
        print("ファイル名が間違っています")
        
args = sys.argv #コマンドライン引数の受け取り

if 2 <= len(args): #引数が入力されていたら
    for i in range(1,len(args)):
        print(args[i]) #ファイル名表示
        cat(args[i])   #ファイルの内容を表示
        if i + 1 < len(args): #最後のファイルでなければ
            print()           #改行を挿入
else:
    print('ファイル名を入力してください')
