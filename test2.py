import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the background color using a style sheet
        self.setStyleSheet("background-color: lightblue;")

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Background Color Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())