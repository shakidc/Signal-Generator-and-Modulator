#SGMv2.py
#A simple program to generate, modulate, and demodulate data signal using ASK, PSK, or FSK method
#usage: python SGMv2.py
#for educational purpose
#choose 1 from 3 given options:
##ASK
##PSK
##FSK
#check 1 from 2 options:
##modulate
##demodulate
#input the required parameters
#check one of the given scales for amplitude, frequency1, and frequency2
#turn the dial to get the desired value, keyboard cursor up and down can be used to get a more precise value
#frequencies should be given in Hz unit
#data list should be given in list format. ex: [1,0,1,0,0,0,1,1]
#Shaki S. Putra|18-12-21

import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import array,linspace,zeros,sin,pi,flip,concatenate

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1283, 921)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.centralwidget.setObjectName("centralwidget")
        self.TITLE = QtWidgets.QLabel(self.centralwidget)
        self.TITLE.setGeometry(QtCore.QRect(280, 20, 781, 41))
        self.TITLE.setStyleSheet("font: 87 26pt \"Segoe UI Black\";\n"
"color: rgb(244, 244, 244);")
        self.TITLE.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE.setWordWrap(False)
        self.TITLE.setObjectName("TITLE")
        self.CR = QtWidgets.QLabel(self.centralwidget)
        self.CR.setGeometry(QtCore.QRect(1190, 70, 91, 21))
        self.CR.setStyleSheet("color: rgb(0, 255, 0);\n"
"font: 75 8pt \"Times New Roman\";")
        self.CR.setTextFormat(QtCore.Qt.AutoText)
        self.CR.setObjectName("CR")
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_2.setGeometry(QtCore.QRect(10, 100, 295, 781))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.modelayout = QtWidgets.QGroupBox(self.verticalWidget_2)
        self.modelayout.setFlat(True)
        self.modelayout.setObjectName("modelayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.modelayout)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ASK = QtWidgets.QRadioButton(self.modelayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ASK.sizePolicy().hasHeightForWidth())
        self.ASK.setSizePolicy(sizePolicy)
        self.ASK.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(18, 18, 18);")
        self.ASK.setObjectName("ASK")
        self.verticalLayout_5.addWidget(self.ASK)
        self.PSK = QtWidgets.QRadioButton(self.modelayout)
        self.PSK.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(18, 18, 18);")
        self.PSK.setObjectName("PSK")
        self.verticalLayout_5.addWidget(self.PSK)
        self.FSK = QtWidgets.QRadioButton(self.modelayout)
        self.FSK.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(18, 18, 18);")
        self.FSK.setObjectName("FSK")
        self.verticalLayout_5.addWidget(self.FSK)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.MODULATE = QtWidgets.QCheckBox(self.modelayout)
        self.MODULATE.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(18, 18, 18);")
        self.MODULATE.setObjectName("MODULATE")
        self.verticalLayout_6.addWidget(self.MODULATE)
        self.DEMODULATE = QtWidgets.QCheckBox(self.modelayout)
        self.DEMODULATE.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(18, 18, 18);")
        self.DEMODULATE.setObjectName("DEMODULATE")
        self.verticalLayout_6.addWidget(self.DEMODULATE)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout.addWidget(self.modelayout)
        self.amplayout = QtWidgets.QGroupBox(self.verticalWidget_2)
        self.amplayout.setFlat(True)
        self.amplayout.setObjectName("amplayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.amplayout)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.amplayout)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(23, 23, 23);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.AMPVAL = QtWidgets.QLabel(self.widget)
        self.AMPVAL.setStyleSheet("font: 14pt \"Seven Segment\";\n"
"color: rgb(0, 255, 0);")
        self.AMPVAL.setObjectName("AMPVAL")
        self.horizontalLayout.addWidget(self.AMPVAL)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget1 = QtWidgets.QWidget(self.amplayout)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.AMPX1 = QtWidgets.QRadioButton(self.widget1)
        self.AMPX1.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.AMPX1.setObjectName("AMPX1")
        self.verticalLayout_7.addWidget(self.AMPX1)
        self.AMPX1K = QtWidgets.QRadioButton(self.widget1)
        self.AMPX1K.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.AMPX1K.setObjectName("AMPX1K")
        self.verticalLayout_7.addWidget(self.AMPX1K)
        self.AMPX1M = QtWidgets.QRadioButton(self.widget1)
        self.AMPX1M.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.AMPX1M.setObjectName("AMPX1M")
        self.verticalLayout_7.addWidget(self.AMPX1M)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setStyleSheet("font: 75 12pt \"Segoe UI\" bold;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.AMP = QtWidgets.QDial(self.widget1)
        self.AMP.setMaximum(10000)
        self.AMP.setObjectName("AMP")
        self.horizontalLayout_7.addWidget(self.AMP)
        self.verticalLayout_3.addWidget(self.widget1)
        self.verticalLayout.addWidget(self.amplayout)
        self.f1layout = QtWidgets.QGroupBox(self.verticalWidget_2)
        self.f1layout.setFlat(True)
        self.f1layout.setObjectName("f1layout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.f1layout)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget2 = QtWidgets.QWidget(self.f1layout)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(25, 25, 25);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.F1VAL = QtWidgets.QLabel(self.widget2)
        self.F1VAL.setStyleSheet("font: 14pt \"Seven Segment\";\n"
"color: rgb(0, 255, 0);")
        self.F1VAL.setObjectName("F1VAL")
        self.horizontalLayout_2.addWidget(self.F1VAL)
        self.verticalLayout_13.addWidget(self.widget2)
        self.widget3 = QtWidgets.QWidget(self.f1layout)
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.F1X1 = QtWidgets.QRadioButton(self.widget3)
        self.F1X1.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.F1X1.setObjectName("F1X1")
        self.verticalLayout_8.addWidget(self.F1X1)
        self.F1X1K = QtWidgets.QRadioButton(self.widget3)
        self.F1X1K.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.F1X1K.setObjectName("F1X1K")
        self.verticalLayout_8.addWidget(self.F1X1K)
        self.F1X1M = QtWidgets.QRadioButton(self.widget3)
        self.F1X1M.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.F1X1M.setObjectName("F1X1M")
        self.verticalLayout_8.addWidget(self.F1X1M)
        self.F1X1G = QtWidgets.QRadioButton(self.widget3)
        self.F1X1G.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.F1X1G.setObjectName("F1X1G")
        self.verticalLayout_8.addWidget(self.F1X1G)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.F1 = QtWidgets.QDial(self.widget3)
        self.F1.setMinimum(1)
        self.F1.setMaximum(10000)
        self.F1.setObjectName("F1")
        self.horizontalLayout_8.addWidget(self.F1)
        self.verticalLayout_13.addWidget(self.widget3)
        self.verticalLayout.addWidget(self.f1layout)
        self.f2layout = QtWidgets.QGroupBox(self.verticalWidget_2)
        self.f2layout.setFlat(True)
        self.f2layout.setObjectName("f2layout")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.f2layout)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.widget4 = QtWidgets.QWidget(self.f2layout)
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget4)
        self.label_4.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(28, 28, 28);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.F2VAL = QtWidgets.QLabel(self.widget4)
        self.F2VAL.setStyleSheet("font: 14pt \"Seven Segment\";\n"
"color: rgb(0, 255, 0);")
        self.F2VAL.setObjectName("F2VAL")
        self.horizontalLayout_3.addWidget(self.F2VAL)
        self.verticalLayout_14.addWidget(self.widget4)
        self.widget5 = QtWidgets.QWidget(self.f2layout)
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.F2X1 = QtWidgets.QRadioButton(self.widget5)
        self.F2X1.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.F2X1.setObjectName("F2X1")
        self.verticalLayout_9.addWidget(self.F2X1)
        self.F2X1K = QtWidgets.QRadioButton(self.widget5)
        self.F2X1K.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.F2X1K.setObjectName("F2X1K")
        self.verticalLayout_9.addWidget(self.F2X1K)
        self.F2X1M = QtWidgets.QRadioButton(self.widget5)
        self.F2X1M.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.F2X1M.setObjectName("F2X1M")
        self.verticalLayout_9.addWidget(self.F2X1M)
        self.F2X1G = QtWidgets.QRadioButton(self.widget5)
        self.F2X1G.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(20, 20, 20);")
        self.F2X1G.setObjectName("F2X1G")
        self.verticalLayout_9.addWidget(self.F2X1G)
        self.horizontalLayout_10.addLayout(self.verticalLayout_9)
        self.F2 = QtWidgets.QDial(self.widget5)
        self.F2.setMinimum(1)
        self.F2.setMaximum(10000)
        self.F2.setObjectName("F2")
        self.horizontalLayout_10.addWidget(self.F2)
        self.verticalLayout_14.addWidget(self.widget5)
        self.verticalLayout.addWidget(self.f2layout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.START = QtWidgets.QPushButton(self.verticalWidget_2)
        self.START.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(0, 170, 0);")
        self.START.setObjectName("START")
        self.horizontalLayout_4.addWidget(self.START)
        self.STOP = QtWidgets.QPushButton(self.verticalWidget_2)
        self.STOP.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(255, 0, 0);")
        self.STOP.setObjectName("STOP")
        self.horizontalLayout_4.addWidget(self.STOP)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_5.setGeometry(QtCore.QRect(310, 760, 961, 122))
        self.horizontalWidget_5.setObjectName("horizontalWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalWidget_5)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(35, 35, 35);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.DATAIN = QtWidgets.QPlainTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DATAIN.sizePolicy().hasHeightForWidth())
        self.DATAIN.setSizePolicy(sizePolicy)
        self.DATAIN.setStyleSheet("color: rgb(0, 255, 0);\n"
"font: 75 10pt \"Segoe UI\" bold;\n"
"border-color: rgb(35, 35, 35);")
        self.DATAIN.setPlainText("")
        self.DATAIN.setObjectName("DATAIN")
        self.verticalLayout_2.addWidget(self.DATAIN)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.groupBox1 = QtWidgets.QGroupBox(self.horizontalWidget_5)
        self.groupBox1.setObjectName("groupBox1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox1)
        self.label_8.setStyleSheet("color: rgb(168, 168, 168);\n"
"font: 75 12pt \"Segoe UI\" bold;\n"
"background-color: rgb(35, 35, 35);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.DATAOUT = QtWidgets.QPlainTextEdit(self.groupBox1)
        self.DATAOUT.setStyleSheet("color: rgb(0, 255, 0);\n"
"font: 75 10pt \"Segoe UI\" bold;\n"
"border-color: rgb(35, 35, 35);")
        self.DATAOUT.setObjectName("DATAOUT")
        self.verticalLayout_4.addWidget(self.DATAOUT)
        self.horizontalLayout_5.addWidget(self.groupBox1)
        self.GRAPH = pg.PlotWidget(self.centralwidget)
        self.GRAPH.setGeometry(QtCore.QRect(310, 100, 961, 651))
        self.GRAPH.setObjectName("GRAPH")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pen = pg.mkPen(color=(0, 255, 0))
        self.pend = pg.mkPen(color=(0, 0, 0), width=0, style=QtCore.Qt.DotLine)
        self.styles = {"color":"#0f0", "font-size":"20px"}
        self.GRAPH.setLabel("left", "Amplitude", **self.styles)
        self.GRAPH.setLabel("bottom", "Time (s)", **self.styles)
        self.START.clicked.connect(self.mulai)
        self.STOP.clicked.connect(self.berhenti)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.proses)
        self.timer.setInterval(500)

    def berhenti(self):
        self.timer.stop()
    
    def mulai(self):
        self.timer.start()
        
    def proses(self):
        self.GRAPH.clear()
        
        bb = 0
        ba = 1
        if self.AMPX1.isChecked():
            a = self.AMP.value()/100
        elif self.AMPX1K.isChecked():
            a = (self.AMP.value()/100) * 1000
        elif self.AMPX1M.isChecked():
            a = (self.AMP.value()/100) * 1000000
        else:
            a = self.AMP.value()
        self.AMPVAL.setText(str(a))
        if self.F1X1.isChecked():
            fc0 = self.F1.value()/100
        elif self.F1X1K.isChecked():
            fc0 = (self.F1.value()/100) * 1000
        elif self.F1X1M.isChecked():
            fc0 = (self.F1.value()/100) * 1000000
        elif self.F1X1G.isChecked():
            fc0 = (self.F1.value()/100) * 1000000000
        else:
            fc0 = self.F1.value()
        self.F1VAL.setText(str(fc0))
        if self.F2X1.isChecked():
            fc1 = self.F2.value()/100
        elif self.F2X1K.isChecked():
            fc1 = (self.F2.value()/100) * 1000
        elif self.F2X1M.isChecked():
            fc1 = (self.F2.value()/100) * 1000000
        elif self.F2X1G.isChecked():
            fc1 = (self.F2.value()/100) * 1000000000
        else:
            fc1 = self.F2.value()
        self.F2VAL.setText(str(fc1))
        t = linspace(bb,ba,100*fc0)
        d0 = list(zeros((len(t),), dtype=float))
        d1 = a*sin(2*pi*fc0*t)
        d1f = flip(a*sin(2*pi*fc0*t))
        d2 = a*sin(2*pi*fc1*t)
        d = eval(self.DATAIN.toPlainText())

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
                self.GRAPH.plot(tA,dmA,pen=self.pen)
                self.DATAOUT.setPlainText(str(dmA.tolist()))
            
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
                self.GRAPH.plot(tdA,ddA,pen=self.pend,symbol='o', symbolSize=30, symbolBrush=('g'))
                self.DATAOUT.setPlainText(str(ddA))
            
            else:
                pass

        elif self.PSK.isChecked():
            
            if self.MODULATE.isChecked():
                tP = array([])
                dmP = array([])
                for i in range(0,len(d)):
                    tP = concatenate((tP,t+i))
                    if d[i] == 0: #add 0 values to modulated data list
                        dmP = concatenate((dmP,d1f))
                    elif d[i] == 1: #add a sine wave values with defined frequency to modulated data list
                        dmP = concatenate((dmP,d1))
                self.GRAPH.showGrid(x=True, y=True)
                self.GRAPH.plot(tP,dmP,pen=self.pen)
                self.DATAOUT.setPlainText(str(dmP.tolist()))
            
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
                self.GRAPH.plot(tdP,ddP,pen=self.pend,symbol='o', symbolSize=30, symbolBrush=('g'))
                self.DATAOUT.setPlainText(str(ddP))
            
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
                self.GRAPH.plot(tF,dmF,pen=self.pen)
                self.DATAOUT.setPlainText(str(dmF.tolist()))
            
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
                self.GRAPH.plot(tdF,ddF,pen=self.pend,symbol='o', symbolSize=30, symbolBrush=('g'))
                self.DATAOUT.setPlainText(str(ddF))

            else:
                pass

        else:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal Modulator & Generator v2.0"))
        self.TITLE.setText(_translate("MainWindow", "SIGNAL GENERATOR & MODULATOR"))
        self.CR.setText(_translate("MainWindow", "©ShakiDC 2021"))
        self.ASK.setText(_translate("MainWindow", "ASK "))
        self.PSK.setText(_translate("MainWindow", "PSK"))
        self.FSK.setText(_translate("MainWindow", "FSK"))
        self.MODULATE.setText(_translate("MainWindow", "MODULATE"))
        self.DEMODULATE.setText(_translate("MainWindow", "DEMODULATE"))
        self.label_2.setText(_translate("MainWindow", "AMPLITUDE   "))
        self.AMPVAL.setText(_translate("MainWindow", "............................."))
        self.AMPX1.setText(_translate("MainWindow", "X 1"))
        self.AMPX1K.setText(_translate("MainWindow", "X 1K"))
        self.AMPX1M.setText(_translate("MainWindow", "X 1M"))
        self.label_3.setText(_translate("MainWindow", "FREQUENCY 1"))
        self.F1VAL.setText(_translate("MainWindow", "............................"))
        self.F1X1.setText(_translate("MainWindow", "X 1"))
        self.F1X1K.setText(_translate("MainWindow", "X 1K"))
        self.F1X1M.setText(_translate("MainWindow", "X 1M"))
        self.F1X1G.setText(_translate("MainWindow", "X 1G"))
        self.label_4.setText(_translate("MainWindow", "FREQUENCY 2"))
        self.F2VAL.setText(_translate("MainWindow", "............................"))
        self.F2X1.setText(_translate("MainWindow", "X 1"))
        self.F2X1K.setText(_translate("MainWindow", "X 1K"))
        self.F2X1M.setText(_translate("MainWindow", "X 1M"))
        self.F2X1G.setText(_translate("MainWindow", "X 1G"))
        self.START.setText(_translate("MainWindow", "START"))
        self.STOP.setText(_translate("MainWindow", "STOP"))
        self.label_7.setText(_translate("MainWindow", "IN"))
        self.label_8.setText(_translate("MainWindow", "OUT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#enigma@origin