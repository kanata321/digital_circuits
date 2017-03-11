#!/usr/bin/python
# -*- coding: utf-8 -*-

# 使用するライブラリ
import sys
import os
import glob
import serial
import serial.tools.list_ports

# シリアル通信設定
# シリアルポート名
sPORT = ""
# シリアル通信速度
sBPS  = 9600

# シリアルポートの検索
def serial_ports():
    ports = serial.tools.list_ports.comports()
    devices = []
    if ports :
        for i in ports :
            devices.append(i.device)
            print(i.device)
    return devices

# シリアル通信部
def serial_readline(ser):
    while True:
        reading = ser.readline()
        if len(reading) > 0 :
            data = reading.decode('utf-8')

# メイン関数
if __name__ == '__main__':

    devices = serial_ports()

    ser = serial.Serial(sPORT, sBPS, timeout=1)
    serial_readline(ser)
