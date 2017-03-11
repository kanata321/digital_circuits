#!/usr/bin/python
# -*- coding: utf-8 -*-

# 使用するライブラリ
import os
import csv
import datetime

# 保存するフォルダの名前を指定、指定されていない場合には直下に保存
dirname = "log"

# このプログラムのあるフォルダのパスを取得
path = os.path.abspath(os.path.dirname(__file__)) + "/" + dirname + "/"

# プログラムを起動した時刻の取得
ctime = datetime.datetime.today().strftime("%Y-%m-%d_%H.%M.%S")

# csvファイル名を指定 ここではフルパス(ex,~/path/to/project/test.csv)
fname = path + ctime + ".csv"

# ヘッダー要素
hlist = ["test1","test2"]

# csvの初期化
def csv_init(fname,hlist=None):
    # ヘッダーの書き込みを行う ファイルが存在する場合には追記モードで開く
    if not os.path.isfile(fname) :
        f = open(fname,"a")
        h_str = map(str,hlist)
        h = ",".join(hlist)
        f.write(h+"\n")
        f.close()
    else :
        f = open(fname,"a")
    return f

# csvへの追記
def csv_append(f,elements):
    f = open(f.name,"a")
    e_str = map(str,elements)
    e = ",".join(e_str)
    f.write(e+"\n")
    f.close()
    return f

# メイン関数
if __name__ == "__main__":

    # csvファイルの初期化
    csvfile = csv_init(fname,hlist)
    print(csvfile)

    # ここではcsvに10回書き込みを行なっている
    for i in range(10) :
        # 配列で書き込みたい要素を送る
        csv_append(csvfile,[i,i*2])
