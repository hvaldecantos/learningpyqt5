
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
# from other_window import Example

class MainWindow(QMainWindow):
    
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.title = 'Experiment runner'

        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480

        self.initUI()
    
    def centerOnScreen (self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2)) 
        print(resolution.height())
        print(resolution.width())

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.centerOnScreen()
        
        self.setupExperimentMenu() # it does not increment the height
        self.show()

    def setupExperimentMenu(self):
        experimentMenu = QMenu("&Experiment", self)
        self.menuBar().addMenu(experimentMenu)

        experimentMenu.addAction("&Start...", self.startExperiment, "Ctrl+S")
        experimentMenu.addAction("&Open experiment...", self.openFile, "Ctrl+O")
        experimentMenu.addAction("Save and E&xit", self.exitExperiment, "Ctrl+Q")

    def startExperiment(self):
        print("startExperiment")
        self.switch_window.emit("Comes from main window")
        self.hide()
    def openFile(self):
        print("openExperiment")
    def exitExperiment(self):
        print("exitExperiment")
        QApplication.instance().quit()


class StartWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Start Window')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.switch)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit()
        self.hide()

class Controller:

    def __init__(self):
        pass

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_start)
        # self.start.close()
        self.window.show()

        # self.window_three.show()

    def show_start(self, text):
        self.start = StartWindow(text)
        self.start.switch_window.connect(self.show_main)
        # self.window.hide()
        self.start.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Controller()
    c.show_main()
    sys.exit(app.exec_())
