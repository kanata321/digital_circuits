#!/usr/bin/python
# -*- coding: utf-8 -*-

# 使用するライブラリ
#from class_test_v1 import SerialManeger
from class_test_v2 import SerialManeger

#----- シリアル通信設定 -----#
# シリアルポート名
sPORT = ""
# シリアル通信速度(bps)
sBPS  = 9600
# シリアル通信タイムアウト(s)
sTIMEOUT = 1

# メイン関数
if __name__ == '__main__':

    print(SerialManeger.find_ports_table())

    Serial = SerialManeger(sPORT, sBPS, sTIMEOUT)

    Serial.read_forever_async()
