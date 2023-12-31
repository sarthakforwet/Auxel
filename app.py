# -*- coding: utf-8 -*-
import sys

# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRunnable, QThreadPool, pyqtSlot

# Multiprocessing
from multiprocessing import Process

# Utility Script
from auxel_app import Auxel

import langchain

# Threading Class
class Worker(QRunnable):
    
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        out = self.fn(*self.args, **self.kwargs)

    def stop(self):
        self.mutex.lock()
        self.terminate_flag = True
        self.mutex.unlock()


class Ui_MainWindow(object):
    def __init__(self):
        self.threadpool = QThreadPool()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 301, 131))
        self.label_2.setStyleSheet("background-image: url(:/img/Trello_Background.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/img/Trello_Background.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(10, 0, 461, 571))
        self.prompt.setTextFormat(QtCore.Qt.RichText)
        self.prompt.setAlignment(QtCore.Qt.AlignCenter)
        self.prompt.setWordWrap(True)
        self.prompt.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard)
        self.prompt.setObjectName("prompt")
        self.auxel_label = QtWidgets.QLabel(self.centralwidget)
        self.auxel_label.setGeometry(QtCore.QRect(210, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.auxel_label.setFont(font)
        self.auxel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.auxel_label.setObjectName("auxel_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.prompt.keyPressEvent = self.keyPressEvent
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.prompt.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Hello!</span></p></body></html>"))
        self.auxel_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff55ff;\">Auxel</span></p></body></html>"))
    
    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Return:
            try:
                worker = Worker(bot.listen)
                self.threadpool.start(worker)

            except Exception as e:
                # Unable to call it.
                worker.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    bot = Auxel()
    sys.exit(app.exec_())