import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog
import json

class MyTable(QTableWidget):
    def __init__(self):
        super().__init__()

    def save_to_json(self, filename):
        table_data = []

        for row in range(self.rowCount()):
            row_data = {}
            for column in range(self.columnCount()):
                item = self.item(row, column)
                if item is not None:
                    row_data[self.horizontalHeaderItem(column).text()] = item.text()
            table_data.append(row_data)

        with open(filename, 'w') as file:
            json.dump(table_data, file, indent=2)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            json_data = json.load(file)

        self.setRowCount(0)
        for row_data in json_data:
            row_position = self.rowCount()
            self.insertRow(row_position)

            for key, value in row_data.items():
                item = QTableWidgetItem(str(value))
                self.setItem(row_position, self.horizontalHeader().indexOf(key), item)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = MyTable()
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.table)

        save_button = QPushButton("Save to JSON", self)
        save_button.clicked.connect(self.save_to_json)
        layout.addWidget(save_button)

        load_button = QPushButton("Load from JSON", self)
        load_button.clicked.connect(self.load_from_json)
        layout.addWidget(load_button)

        self.setCentralWidget(central_widget)

    def save_to_json(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save to JSON", "", "JSON Files (*.json)")
        if filename:
            self.table.save_to_json(filename)

    def load_from_json(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load from JSON", "", "JSON Files (*.json)")
        if filename:
            self.table.load_from_json(filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setGeometry(100, 100, 800, 600)
    main_window.show()
    sys.exit(app.exec_())