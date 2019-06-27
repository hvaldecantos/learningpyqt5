import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
# import os

class Example(QWidget):
    
    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        # self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'web256.png'))
        # self.setWindowIcon(QIcon("/home/hav2082/Work/python/qt5/web256.png"))
        self.setWindowIcon(QIcon('web256.png'))
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
