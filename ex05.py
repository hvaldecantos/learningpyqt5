import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):
    
    def __init__(self):
        super(QWidget, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        container = QPushButton('cont', self) 
        container.resize(100,100)
        container.move(50,50)

        qbtn = QPushButton('Quit', container) # a button inside a button
        # qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.clicked.connect(self.close)
        # qbtn.resize(qbtn.sizeHint())
        qbtn.resize(50,50)
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
