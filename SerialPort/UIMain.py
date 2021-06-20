import serial
import serial.tools.list_ports
import sys
import time
import datetime
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog, QGraphicsScene
from PyQt5.QtCore import QThread, pyqtSignal
from myui import Ui_MyUI
import binascii

import os
from pandas import DataFrame
from pandas import read_excel

data = []
display = ['-1'] * 17
manulSaveFlag = False


class MainWindow(QDialog, Ui_MyUI):
    """
    UI界面，主窗口
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.spThread = ""
        self.autoSaveThread = ""
        self.upDateFlag = False
        self.serialPort = ""

        self.start.clicked.connect(self.start_sample)
        self.save.clicked.connect(self.save_manul)

    def start_sample(self):
        saveCount = self.saveCount.currentText()
        try:
            saveCount = int(saveCount)
        except:
            msg_box = QMessageBox()
            msg_box.warning(self, "提示", "请填入整数", QMessageBox.Ok)
            return 0

        try:
            if not self.spThread.isRunning():
                self.serialPort = open_port()
                if not self.serialPort:
                    msg_box = QMessageBox()
                    msg_box.warning(self, "提示", "打开串口失败", QMessageBox.Ok)
                    return 0
                self.spThread = SerialPortThread(self.serialPort, 1)
                self.spThread.start()

                self.autoSaveThread = SaveThread('', saveCount)
                self.autoSaveThread.save_error_flag.connect(self.save_error_box)
                self.autoSaveThread.start()
        except:
            if self.serialPort == "" or self.serialPort is False:
                self.serialPort = open_port()
            elif not self.serialPort.is_open:
                self.serialPort = open_port()
            if not self.serialPort:
                msg_box = QMessageBox()
                msg_box.warning(self, "提示", "打开串口失败.", QMessageBox.Ok)
                return 0
            self.spThread = SerialPortThread(self.serialPort, 1)
            self.autoSaveThread = SaveThread('', saveCount)
            self.autoSaveThread.save_error_flag.connect(self.save_error_box)
            self.spThread.start()
            self.autoSaveThread.start()

        self.spThread.get_data_signal.connect(self.updateData)
        self.spThread.sampleFlag = True
        self.autoSaveThread.sampleFlag = True
        print("采样开始：", self.spThread.isRunning())

    def updateData(self):
        global display
        if len(data) != 0:
            display = data[-1]
        self.time.setText(display[0])
        self.lineEdit0.setText(display[1] + '  mV')
        self.lineEdit1.setText(display[2] + '  mV')
        self.lineEdit2.setText(display[3] + '  mV')
        self.lineEdit3.setText(display[4] + '  mV')
        self.lineEdit4.setText(display[5] + '  mV')
        self.lineEdit5.setText(display[6] + '  mV')
        self.lineEdit6.setText(display[7] + '  mV')
        self.lineEdit7.setText(display[8] + '  mV')
        self.lineEdit8.setText(display[9] + '  mV')
        self.lineEdit9.setText(display[10] + '  mV')
        self.lineEdit10.setText(display[11] + '  mV')
        self.lineEdit11.setText(display[12] + '  mV')
        self.lineEdit12.setText(display[13] + '  mV')
        self.lineEdit13.setText(display[14] + '  mV')
        self.lineEdit14.setText(display[15] + '  mV')
        self.lineEdit15.setText(display[16] + '  mV')

    def save_manul(self):
        try:
            self.autoSaveThread.manulSaveFlag = True
        except:
            msg_box = QMessageBox()
            msg_box.warning(self, "提示", "保存错误，请先开始采样", QMessageBox.Ok)

    def save_error_box(self):
        msg_box = QMessageBox()
        msg_box.warning(self, "提示", "保存错误，检查保存路径文件是否损坏或被占用", QMessageBox.Ok)


class SerialPortThread(QThread):
    get_data_signal = pyqtSignal()

    def __init__(self, sp, sampleTime):
        """
        串口数据采集线程
        :param sampleTime: 采样时间
        :param sp: 打开的串口类
        """
        super(SerialPortThread, self).__init__()
        self.sampleTime = sampleTime
        self.sp = sp
        self.sampleFlag = False

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
            if self.sampleFlag:
                error = time_delta(old_datetime)
                if error >= self.sampleTime:
                    old_datetime = old_datetime + datetime.timedelta(seconds=self.sampleTime)
                    now_time = datetime.datetime.strftime(old_datetime, '%Y-%m-%d %H:%M:%S')
                    if voltage == -1:
                        data.append([now_time] + ['-1'] * 16)
                    else:
                        voltage = receive(sp=self.sp)
                        voltage_str = []
                        for i in voltage:
                            voltage_str.append(str(i))
                        data.append([now_time] + voltage_str)
                        print([now_time] + voltage_str)
                    self.get_data_signal.emit()


class SaveThread(QThread):
    save_error_flag = pyqtSignal()

    def __init__(self, path, saveCount=20):
        """
        数据保存线程
        :param path: 保存路劲
        :param saveCount: 自动保存间隔数据数
        """
        super(SaveThread, self).__init__()
        self.path = path
        self.saveCount = saveCount
        self.sampleFlag = False
        self.quitFlag = False
        self.manulSaveFlag = False

    def run(self):
        global data
        while True:
            if self.sampleFlag:
                try:
                    if len(data) > self.saveCount:
                        saveDataList = data
                        data = []
                        save_data(self.path, saveDataList)
                except:
                    print("save error")
                    self.save_error_flag.emit()

            if self.manulSaveFlag:
                try:
                    saveDataList = data
                    data = []
                    save_data(self.path, saveDataList)
                except:
                    print("error")
                    self.save_error_flag.emit()
                self.manulSaveFlag = False


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
                for i in range(8):
                    voltage[2 * i], voltage[2 * i + 1] = voltage[2 * i + 1], voltage[2 * i]
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


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
