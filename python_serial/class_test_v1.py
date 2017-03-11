#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import glob
import serial
import serial.tools.list_ports
import threading
import time

import traceback

class SerialManeger :

    bps_default = [9600, 19200, 38400, 57600, 115200, 230400]

    # クラスの初期化処理
    def __init__(self,port,bps,timeout=1):
        self.devices = self.find_ports()
        self.ser_ctl = self.set_ser_ctl(port,bps,timeout)

    # シリアルポートの検索
    def find_ports(self):
        ports = serial.tools.list_ports.comports()
        devices = []
        if ports :
            for i in ports :
                devices.append(i.device)
        return devices

    # シリアルオブジェクトを取得
    def set_ser_ctl(self,port,bps,timeout):
        if port in self.devices : #and bps in self.bps_default :
            ser_ctl = serial.Serial(port,bps,timeout=timeout)
            return ser_ctl
        else :
            self.error(port,bps)
            #return False

    # シリアル通信部
    # def read(self):
    #     while True:
    #         # 1行(\nまで)読み取り
    #         reading = self.ser_ctl.readline()
    #         if len(reading) > 0 :
    #             #print(reading)
    #             data = reading.decode('utf-8').split('\r\n')[0]
    #             print(data)

    # 別スレッドで読み込み
    def read_async(self):
        thread = threading.Thread(target=self.read)
        thread.start()

    # エラー処理
    def error(self,port,bps):
        try:
            raise Exception("\nError occurred!\n")
        except:
            traceback.print_exc()
        #sys.stderr.write("\nError occurred!\n")
        if not (port in self.devices) :
            if port == "" :
                sys.stderr.write("Please write a SerialPort\'s name.\r\n")
            else :
                sys.stderr.write("This SerialPort\'s name could not find ( port : %s ).\n" % (port))

        if not (bps in self.bps_default):
            sys.stderr.write("This BaudRate\'s value does not exists ( baudrate : %i bps ).\n" % (bps))
