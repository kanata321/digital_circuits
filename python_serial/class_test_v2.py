#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import glob
import serial
import serial.tools.list_ports
import threading
import time

from prettytable import PrettyTable

class SerialManeger :

    bps_default = [9600, 19200, 38400, 57600, 115200, 230400]

    # クラスの初期化処理
    def __init__(self,port,bps,timeout=1):
        self.port = port
        self.bps = bps
        self.timeout = timeout

        # シリアルコントローラを作成
        self.ser_ctlr = serial.Serial(port,bps,timeout=timeout)
        if(self.ser_ctlr) :
            print("%s is Opening..."%(self.port))


    # シリアルポートの検索
    @classmethod
    def find_ports(cls):
        ports = serial.tools.list_ports.comports()
        return ports

    @classmethod
    def find_ports_table(cls,keys=["device"]):
        ports = cls.find_ports()
        if len(ports) > 0 :
            table = PrettyTable(keys)
            for i in ports :
                row_vals = []
                for j in keys :
                    row_vals.append(vars(i)[j])
                table.add_row(row_vals)
            return table

    @classmethod
    def find_ports_list(cls):
        ports = cls.find_ports()
        devices = []
        if ports :
            for i in ports :
                devices.append(i.device)
        return devices

    # シリアル通信部
    def read_forever(self):
        while True:
            reading = self.ser_ctlr.readline()
            if len(reading) > 0 :
                data = reading.decode('utf-8').split('\r\n')[0]
                print(data)

    # 別スレッドで読み込み
    def read_forever_async(self):
        thread = threading.Thread(target=self.read_forever)
        thread.start()
