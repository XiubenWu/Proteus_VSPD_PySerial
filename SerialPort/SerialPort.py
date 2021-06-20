import serial
import serial.tools.list_ports
import binascii
import time
import datetime
import os
from pandas import DataFrame
from pandas import read_excel
import threading

data = []


class GetDataThread(threading.Thread):
    def __init__(self, sp, sampleTime):
        threading.Thread.__init__(self)
        self.sp = sp
        self.sampleTime = sampleTime

    def run(self):
        global data
        old_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        old_datetime = datetime.datetime.strptime(old_time, '%Y-%m-%d %H:%M:%S')
        voltage = receive(sp=self.sp)
        assert voltage != -1
        voltage_str = []
        for i in voltage:
            voltage_str.append(str(i))
        data.append([old_time] + voltage_str)
        while True:
            error = time_delta(old_datetime)
            if error >= self.sampleTime:
                old_datetime = old_datetime + datetime.timedelta(seconds=self.sampleTime)
                now_time = datetime.datetime.strftime(old_datetime, '%Y-%m-%d %H:%M:%S')
                if voltage == -1:
                    data.append([now_time] + ['-1' for _ in range(16)])
                else:
                    voltage = receive(sp=self.sp)
                    voltage_str = []
                    for i in voltage:
                        voltage_str.append(str(i))
                    data.append([now_time] + voltage_str)
                    print([now_time] + voltage_str)


class SaveThread(threading.Thread):
    def __init__(self, path="", saveCount=20):
        threading.Thread.__init__(self)
        self.path = path
        self.saveCount = saveCount

    def run(self):
        global data
        save_data(self.path, [])
        while True:
            try:
                if len(data) > self.saveCount:
                    saveDataList = data
                    data = []
                    save_data(self.path, saveDataList)
            except:
                print("save error")


def time_delta(old_time):
    """
    :param old_time: 上次采样时间
    :return: 据上次采样时间差值 ms
    """
    new_time = datetime.datetime.now()
    error = new_time - old_time
    return error.total_seconds() * 1000


def open_port(com=1, baudrate=9600):
    """
    :param com: serial port name, this pc use com3
    :param baudrate: baudrate
    :return: a serial port which can operate
    """
    splist = list(serial.tools.list_ports.comports())
    comList = [r"VSBC\\DEVICES\\0000", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"]
    # if len(splist) == 0:
    #     raise IOError("未找到端口")
    sp = serial.Serial('COM1', baudrate, timeout=0.5)
    return sp


def receive(sp):
    """
    :param sp: serial port
    :return: concentration v
    """
    voltage = -1
    try:
        while True:
            data = sp.readline()
            # print(data)
            data = binascii.b2a_hex(data)
            # print(data)
            if data[0:2] != b'00' or data[-6:] != b'ff0d0a':
                time.sleep(0.01)
                continue
            else:
                data_resize = data[2:-6]
                voltage = [0.] * 16
                for i in range(16):
                    voltage[i] = round(int(data_resize[2 * i:2 * i + 2], 16) / 255 * 10, 4)  # 单位mv
                break
    except:
        pass

    return voltage


def save_data(path, newData):
    """
    :param path: path+file name
    :param newData: new data as [[time,data...],[time,data...]]
    :return: none
    """
    header = ["Time", "Channel0", "Channel1", "Channel2", "Channel3", "Channel4", "Channel5", "Channel6", "Channel7",
              "Channel8", "Channel9", "Channel10", "Channel11", "Channel12", "Channel13", "Channel14", "Channel15"]
    if path == "":
        path = "G:"
    path = path + r"\data.xlsx"
    if not os.path.exists(path):
        df = DataFrame(columns=header)
        df.to_excel(path, index=False)
    else:
        df = read_excel(path)
    newDf = DataFrame(newData, columns=header)
    df = df.append(newDf, ignore_index=False)
    df.to_excel(path, index=False)
    print("excel write successfully")


if __name__ == '__main__':
    sp = open_port(baudrate=9600)
    print(receive(sp))
    sp.close()
    sp.open()

    # 创建新线程
    thread1 = GetDataThread(sp, 1)
    thread2 = SaveThread()

    # 开启新线程
    thread1.start()
    thread2.start()
