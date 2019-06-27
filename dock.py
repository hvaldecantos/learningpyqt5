from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import QFile, QRegExp, Qt

class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)
        self.setCentralWidget(QTextEdit())

        self.docked = QDockWidget("Dockable", self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.docked)
        self.dockedWidget = QWidget(self)
        self.docked.setWidget(self.dockedWidget)
        self.setWindowTitle("Dock demo")
        self.dockedWidget.setLayout(QVBoxLayout())
        for i in range(5):
            self.dockedWidget.layout().addWidget(QPushButton("{}".format(i)))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = DockDemo()
    ex.show()
    sys.exit(app.exec_())
