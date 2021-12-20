#SGM.py
#A simple program to generate, modulate, and demodulate data signal using ASK, PSK, or FSK method
#usage: python SGM.py
#for educational purpose
#choose 1 from 3 given options:
##ASK
##PSK
##FSK
#check 1 from 2 options:
##modulate
##demodulate
#input the required parameters
#frequencies should be given in Hz unit
#data list should be given in list format. ex: [1,0,1,0,0,0,1,1]
#Shaki S. Putra|05-11-21

import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import array,linspace,zeros,sin,pi,flip,concatenate

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1283, 1000)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 98, 386, 751))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setStyleSheet("color: rgb(168, 168, 168);\n"
        "background-color: rgb(15, 15, 15);\n"
        "font: 75 12pt \"Segoe UI\" bold;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ASK = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ASK.sizePolicy().hasHeightForWidth())
        self.ASK.setSizePolicy(sizePolicy)
        self.ASK.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(18, 18, 18);")
        self.ASK.setObjectName("ASK")
        self.verticalLayout.addWidget(self.ASK)
        self.PSK = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.PSK.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(18, 18, 18);")
        self.PSK.setObjectName("PSK")
        self.verticalLayout.addWidget(self.PSK)
        self.FSK = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.FSK.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(18, 18, 18);")
        self.FSK.setObjectName("FSK")
        self.verticalLayout.addWidget(self.FSK)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.MODULATE = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.MODULATE.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(20, 20, 20);")
        self.MODULATE.setObjectName("MODULATE")
        self.horizontalLayout_7.addWidget(self.MODULATE)
        self.DEMODULATE = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.DEMODULATE.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(20, 20, 20);")
        self.DEMODULATE.setObjectName("DEMODULATE")
        self.horizontalLayout_7.addWidget(self.DEMODULATE)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(23, 23, 23);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.AMPLITUDE = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.AMPLITUDE.setStyleSheet("font: 16pt \"Seven Segment\";\n"
        "color: rgb(0, 255, 0);\n"
        "background-color: rgb(0, 0, 0);")
        self.AMPLITUDE.setMaximum(1000000000.0)
        self.AMPLITUDE.setSingleStep(0.1)
        self.AMPLITUDE.setObjectName("AMPLITUDE")
        self.horizontalLayout.addWidget(self.AMPLITUDE)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(25, 25, 25);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.FC1 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.FC1.setStyleSheet("font: 16pt \"Seven Segment\";\n"
        "color: rgb(0, 255, 0);\n"
        "background-color: rgb(0, 0, 0);")
        self.FC1.setMaximum(1000000000.0)
        self.FC1.setSingleStep(0.1)
        self.FC1.setObjectName("FC1")
        self.horizontalLayout_2.addWidget(self.FC1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(28, 28, 28);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.FC2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.FC2.setStyleSheet("font: 16pt \"Seven Segment\";\n"
        "color: rgb(0, 255, 0);\n"
        "background-color: rgb(0, 0, 0);")
        self.FC2.setMaximum(1000000000.0)
        self.FC2.setSingleStep(0.1)
        self.FC2.setObjectName("FC2")
        self.horizontalLayout_3.addWidget(self.FC2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(33, 33, 33);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(35, 35, 35);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.DATA = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DATA.sizePolicy().hasHeightForWidth())
        self.DATA.setSizePolicy(sizePolicy)
        self.DATA.setStyleSheet("color: rgb(0, 255, 0);\n"
        "font: 75 10pt \"Segoe UI\" bold;")
        self.DATA.setPlainText("")
        self.DATA.setObjectName("DATA")
        self.verticalLayout_3.addWidget(self.DATA)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setStyleSheet("color: rgb(168, 168, 168);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "background-color: rgb(35, 35, 35);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.DOUT = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        sizePolicy.setHeightForWidth(self.DOUT.sizePolicy().hasHeightForWidth())
        self.DOUT.setSizePolicy(sizePolicy)
        self.DOUT.setStyleSheet("color: rgb(0, 255, 0);\n"
        "font: 75 10pt \"Segoe UI\" bold;")
        self.DOUT.setPlainText("")
        self.DOUT.setObjectName("DOUT")
        self.verticalLayout_3.addWidget(self.DOUT)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.PROCESS = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.PROCESS.setEnabled(True)
        self.PROCESS.setStyleSheet("color: rgb(175, 175, 175);\n"
        "font: 75 12pt \"Segoe UI\" bold;\n"
        "border-radius: 20px;\n"
        "background-color: rgb(40, 40, 40);\n"
        "height: 50%;")
        self.PROCESS.setObjectName("PROCESS")
        self.verticalLayout_2.addWidget(self.PROCESS)
        self.GRAPH = pg.PlotWidget(self.centralwidget)
        self.GRAPH.setGeometry(QtCore.QRect(380, 100, 880, 831))
        self.GRAPH.setObjectName("GRAPH")
        self.TITLE = QtWidgets.QLabel(self.centralwidget)
        self.TITLE.setGeometry(QtCore.QRect(230, 20, 851, 41))
        self.TITLE.setStyleSheet("font: 87 28pt \"Segoe UI Black\";\n"
        "color: rgb(244, 244, 244);")
        self.TITLE.setObjectName("TITLE")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 870, 91, 21))
        self.label_6.setStyleSheet("color: rgb(0, 255, 0);\n"
        "font: 75 8pt \"Times New Roman\";")
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QtCore.QRect(0, 950, 90, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def proses(self):
        self.GRAPH.clear()
        pen = pg.mkPen(color=(0, 255, 0))
        pend = pg.mkPen(color=(0, 0, 0), width=0, style=QtCore.Qt.DotLine)
        styles = {"color":"#0f0", "font-size":"20px"}
        self.GRAPH.setLabel("left", "Amplitude", **styles)
        self.GRAPH.setLabel("bottom", "Time (s)", **styles)

        bb = 0
        ba = 1
        a = self.AMPLITUDE.value()
        fc0 = self.FC1.value()
        fc1 = self.FC2.value()
        t = linspace(bb,ba,100*fc0)
        d0 = list(zeros((len(t),), dtype=float))
        d1 = a*sin(2*pi*fc0*t)
        d1f = flip(a*sin(2*pi*fc0*t))
        d2 = a*sin(2*pi*fc1*t)
        d = eval(self.DATA.toPlainText())

        if self.ASK.isChecked():
    
            if self.MODULATE.isChecked():
                dmA = array([])
                tA = array([])
                for i in range(0,len(d)):
                    tA = concatenate((tA,t+i))
                    if d[i] == 0: #add 0 values to modulated data list
                        dmA = concatenate((dmA,d0))
                    elif d[i] == 1: #add a sine wave values with defined frequency to modulated data list
                        dmA = concatenate((dmA,d1))
                self.GRAPH.showGrid(x=True, y=True)
                self.GRAPH.plot(tA,dmA,pen=pen)
                self.DOUT.setPlainText(str(dmA.tolist()))
            
            elif self.DEMODULATE.isChecked():
                ddA = []
                tdA = []
                for i in range(0,int(len(d)/len(t))):
                    tdA.append(i+1)
                    if d[i*len(t)+1] == d1[1]:
                        ddA.append(1)
                    else:
                        ddA.append(0)
                self.GRAPH.showGrid(x=True, y=True)
                self.GRAPH.plot(tdA,ddA,pen=pend,symbol='o', symbolSize=30, symbolBrush=('g'))
                self.DOUT.setPlainText(str(list(ddA)))
            
            else:
                pass

        elif self.PSK.isChecked():
            
            if self.MODULATE.isChecked():
                tP = t
                dmP = array([])
                for i in range(0,len(d)):
                    if i > 0:
                        tP = concatenate((tP,t+i))
                    if d[i] == 0: #add 0 values to modulated data list
                        dmP = concatenate((dmP,d1f))
                    elif d[i] == 1: #add a sine wave values with defined frequency to modulated data list
                        dmP = concatenate((dmP,d1))
                self.GRAPH.showGrid(x=True, y=True)
                self.GRAPH.plot(tP,dmP,pen=pen)
                self.DOUT.setPlainText(str(dmP.tolist()))
            
            elif self.DEMODULATE.isChecked():
                ddP = []
                tdP = []
                for i in range(0,int(len(d)/len(t))):
                    tdP.append(i+1)
                    if d[i*len(t)+1] == d1[1]:
                        ddP.append(1)
                    else:
                        ddP.append(0)
                self.GRAPH.showGrid(x=True, y=True)
                self.GRAPH.plot(tdP,ddP,pen=pend,symbol='o', symbolSize=30, symbolBrush=('g'))
                self.DOUT.setPlainText(str(ddP))
            
            else:
                pass
        
        elif self.FSK.isChecked():

            if self.MODULATE.isChecked():
                dmF = array([])
                tF = array([])
                for i in range(0,len(d)):
                    tF = concatenate((tF,t+i))
                    if d[i] == 0:
                        dmF = concatenate((dmF,d1))
                    elif d[i] == 1:
                        dmF = concatenate((dmF,d2))
                self.GRAPH.showGrid(x=True, y=True)
                self.GRAPH.plot(tF,dmF,pen=pen)
                self.DOUT.setPlainText(str(dmF.tolist()))
            
            elif self.DEMODULATE.isChecked():
                tdF = []
                ddF = []
                for i in range(0,int(len(d)/len(t))):
                    tdF.append(i+1)
                    if d[i*len(t)+1] == d1[1]:
                        ddF.append(0)
                    elif d[i*len(t)+1] == d2[1]:
                        ddF.append(1)
                self.GRAPH.showGrid(x=True, y=True)
                self.GRAPH.plot(tdF,ddF,pen=pend,symbol='o', symbolSize=30, symbolBrush=('g'))
                self.DOUT.setPlainText(str(ddF))

            else:
                pass

        else:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal Modulator & Generator"))
        self.label.setText(_translate("MainWindow", "METHOD"))
        self.ASK.setText(_translate("MainWindow", "ASK "))
        self.PSK.setText(_translate("MainWindow", "PSK"))
        self.FSK.setText(_translate("MainWindow", "FSK"))
        self.MODULATE.setText(_translate("MainWindow", "MODULATE"))
        self.DEMODULATE.setText(_translate("MainWindow", "DEMODULATE"))
        self.label_2.setText(_translate("MainWindow", "AMPLITUDE       "))
        self.label_3.setText(_translate("MainWindow", "FREQUENCY 1"))
        self.label_4.setText(_translate("MainWindow", "FREQUENCY 2"))
        self.label_5.setText(_translate("MainWindow", "DATA"))
        self.label_7.setText(_translate("MainWindow", "IN"))
        self.label_8.setText(_translate("MainWindow", "OUT"))
        self.PROCESS.setText(_translate("MainWindow", "PROCESS!"))
        self.TITLE.setText(_translate("MainWindow", "SIGNAL GENERATOR & MODULATOR"))
        self.label_6.setText(_translate("MainWindow", "©ShakiDC 2021"))
        self.PROCESS.clicked.connect(self.proses)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#enigma@origin