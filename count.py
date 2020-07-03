# -*- coding: utf-8 -*-
import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox, QFileDialog
import datetime

class countDown(QMainWindow):
    def __init__(self):
        super(countDown, self).__init__()
        uic.loadUi('countdown.ui', self)
        self.setupUi()
        self.setMenu()

        #======================================================================    
    def setupUi(self):        
        #set up initial responses
        self.today = datetime.date.today()
        ty = str(self.today).split('-')[0]
        tm = str(self.today).split('-')[1]
        td = str(self.today).split('-')[2]
        
        self.todayYear.setText(ty)
        self.todayYear.setToolTip(self.todayYear.text())
        self.todayMonth.setText(tm)
        self.todayMonth.setText(self.todayMonth.text())
        self.todayDay.setText(td)
        self.todayDay.setToolTip(self.todayDay.text())
        
        self.endYear.setText('2020')
        self.endYear.setToolTip('Input timebox ending Year')
        self.endMonth.setText('12')
        self.endMonth.setToolTip('Input timebox ending Month')
        self.endDay.setText('31')
        self.endDay.setToolTip('Input timebox ending Day')
        
        self.cal.setText('Calculate remaining days')
        self.cal.setToolTip("Remaining")
        self.cal.setStyleSheet("border: 1px solid grey; border-radius: 3px;")
        self.cal.setMinimumSize(200, 20)
        self.cal.released.connect(self.calc)
        
        self.calc()
        
        # self.endYear.textChanged.connect(self.calc)
        # self.endMonth.textChanged.connect(self.calc)
        # self.endDay.textChanged.connect(self.calc)
        
        #======================================================================
    def setMenu(self):
        #set up windows menubar
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False) #needed for mac
        
        fileMenu = mainMenu.addMenu('File')
        
        calc = QAction("Count the days", self)
        calc.setShortcut("Ctrl+R")
        calc.setStatusTip("Click to show days left")
        fileMenu.addAction(calc)
        calc.triggered.connect(self.calc) 
        
        quit = QAction("Quit", self)
        quit.setShortcut("Ctrl+Q")
        quit.setStatusTip("Click to Exit")
        fileMenu.addAction(quit)
        quit.triggered.connect(self.close)   
        
        self.show()
            
        #======================================================================
    def close (self):
        choice = QMessageBox.question(self, 'Close',
                                            "Do you want to quit the application?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Session closed")
            sys.exit()
        else:
            pass
        
        #======================================================================    
    def calc (self):
        def numOfDays(date1, date2): 
            return (date2-date1).days 
        
        date1 = datetime.datetime.strptime(self.todayYear.text() + '-' + self.todayMonth.text() + '-' + self.todayDay.text(), "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(self.endYear.text() + '-' + self.endMonth.text() + '-' + self.endDay.text(), "%Y-%m-%d").date()
        days = numOfDays(date1, date2)
        
        if date2 < date1:
            QtWidgets.QMessageBox.information(self, 'Timebox', 'End date prior to todays date - so no more waiting')
            return
        else:
            pass
        
        self.lcdNumber.display(days)
        
#======================================================================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = countDown()
    window.show()
    sys.exit(app.exec_())