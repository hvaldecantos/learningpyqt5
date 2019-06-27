import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QVBoxLayout, QPushButton, QListWidget, QMenuBar, QMenu, QAction
from PyQt5 import QtCore

class Example(QWidget):
    
    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):               
        
        # Windows size and position
        self.setFixedSize(640, 480)
        self.center()
        self.createMenu()

        qbtn = QPushButton('Quit', self) # a button inside a button
        qbtn.clicked.connect(QApplication.instance().quit)
        # qbtn.resize(qbtn.sizeHint())
        qbtn.resize(50,50)
        qbtn.move(250, 50)
        

        listWidget = QListWidget(self)
        listWidget.show()
        ls = ['test0', 'test1', 'test2', 'test3', 'test4']
        listWidget.addItems(ls)
        listWidget.resize(100, 480)

        # listWidget.itemClicked()
        listWidget.itemClicked.connect(self.onItemClickOnList)

        # self.setWindowTitle('Center')
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint )

        self.show()

    def createMenu(self):
        self.myQMenuBar = QMenuBar(self)
        exitMenu = self.myQMenuBar.addMenu('File')
        exitAction = QAction('Exit', self)        
        exitAction.triggered.connect(QApplication.instance().quit)
        exitMenu.addAction(exitAction)

        # self.menuBar = QMenuBar(self)

        # self.fileMenu = QMenu("&File", self)
        # self.exitAction = self.fileMenu.addAction("E&xit")
        # self.menuBar.addMenu(self.fileMenu)

        # self.exitAction.triggered.connect(QApplication.instance().quit)      
    
    def onItemClickOnList(self, l):
        print(l.text())

    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def moveEvent(self, event):
        self.center()
        #widget.move(x, y)
        # self.move(self.height() - self.height())
        # #if you want the widgets width equal to window width:
        # self.bottom_widget.setWidth(self.width())

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
