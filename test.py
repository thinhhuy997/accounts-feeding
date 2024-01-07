import sys
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QStandardItemModel, QStandardItem

class MyTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a QTableView and a QStandardItemModel
        table_view = QTableView()
        model = QStandardItemModel(self)

        # Set the column and row count for the model
        model.setColumnCount(3)
        model.setRowCount(4)

        # Populate the model with data
        for row in range(4):
            for col in range(3):
                item = QStandardItem(f"Row {row + 1}, Col {col + 1}")
                model.setItem(row, col, item)

        # Set the model for the QTableView
        table_view.setModel(model)

        # Create a layout and set the QTableView as its central widget
        layout = QVBoxLayout()
        layout.addWidget(table_view)
        self.setLayout(layout)

        self.setWindowTitle('QTableView Example')
        self.setGeometry(100, 100, 600, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyTableWidget()
    sys.exit(app.exec_())