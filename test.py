import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTableWidget Horizontal Center Alignment")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self.central_widget)

        # Create QTableWidget
        table_widget = QTableWidget(self)
        table_widget.setColumnCount(3)
        table_widget.setRowCount(5)

        # Set alignment for the second column to be horizontally centered
        for row in range(table_widget.rowCount()):
            item = QTableWidgetItem("Text in Row {}, Col 1".format(row))
            item.setTextAlignment(Qt.AlignHCenter)
            table_widget.setItem(row, 1, item)

        layout.addWidget(table_widget)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()