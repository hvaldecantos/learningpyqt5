import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def format(color, style=''):
    """Return a QTextCharFormat with the given attributes."""
    _color = QColor()
    _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


STYLES = {
    'keyword': format('magenta'),
    'comment': format('green', 'italic'),
    'javadocs': format('blue'),
    'numbers': format('brown'),
    'string': format('red'),
    'self': format('darkMagenta', 'italic'),
    'operator': format('red'),
}


class PythonHighlighter (QSyntaxHighlighter):
    java_keywords = """abstract 	continue 	for 	new 	switch
    assert 	default 	goto 	package 	synchronized
    boolean 	do 	if 	private 	this
    break 	double 	implements 	protected 	throw
    byte 	else 	import 	public 	throws
    case 	enum 	instanceof 	return 	transient
    catch 	extends 	int 	short 	try
    char 	final 	interface 	static 	void
    class 	finally 	long 	strictfp 	volatile
    const 	float 	native 	super 	while true false null"""
    keywords = []
    for word in java_keywords.split():
        keywords.append(word)
    operators = [
               '=',
        # Comparison
               '==', '!=', '<', '<=', '>', '>=',
        # Arithmetic
               '\+', '-', '\*', '/', '//', '\%', '\*\*',
        # In-place
               '\+=', '-=', '\*=', '/=', '\%=',
        # Bitwise
               '\^', '\|', '\&', '\~', '>>', '<<',
        ]

# https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        rules = []
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                  for w in PythonHighlighter.keywords]
        rules += [(r'%s' % o, 0, STYLES['operator'])
                  for o in PythonHighlighter.operators]

        self.title = 'Code Comprehension'
        self.left = 500
        self.top = 150
        self.width = 1000
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.hlayout = QHBoxLayout(self.centralWidget)

        self.label = QLabel()
        self.label.setStyleSheet("""
                    QLabel {
                        border: 1px solid black;
                        border-radius: 1px;
                        background-color: rgb(255, 255, 255);
                        }
                    """)
        self.label.setAlignment(Qt.AlignTop)

        self.scroller = QScrollArea(self.centralWidget)
        self.scroller.setFrameShape(QFrame.Box)
        self.scroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroller.setWidgetResizable(True)
        self.scroller.setWidget(self.label)

        self.buttons = QWidget()
        self.buttons_layout = QVBoxLayout(self.buttons)
        self.files = []
        self.filenames = []
        self.lambdas = []
        i = 0
        for filename in os.listdir('C:/Users/harri/CS211 Labs/217_hklein2_P5'):
            self.filenames.append(filename)
            self.files.append(QPushButton(self.filenames[i]))
            self.lambdas.append(self.build_lambda(self.files[i]))
            self.files[i].clicked.connect(self.lambdas[i])
            self.buttons_layout.addWidget(self.files[i])
            i += 1

        self.hlayout.addWidget(self.buttons, 1)
        self.hlayout.addWidget(self.scroller, 4)

        self.show()

    def change_file(self, button):
        self.label.setText(open('C:/Users/harri/CS211 Labs/217_hklein2_P5/' + self.filenames[self.files.index(button)], "r").read())

    def build_lambda(self, button):
        return lambda: self.change_file(button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())