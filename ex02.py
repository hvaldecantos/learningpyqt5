import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    # QWidget widget is the base class of all user interface objects in PyQt5
    # it has a default constructor and has no parent.
    # a widget with no parent is a windows
    w = QWidget()

    w.resize(250, 150)
    w.move(1300, 800)
    w.setWindowTitle('Simple')
    w.show()
    
    # for x in range(200):
    # 	 w.move(1300, x)

    sys.exit(app.exec_())
