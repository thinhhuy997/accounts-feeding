import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5 import QtWidgets
import json

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        btn_export_json = QPushButton('Export to JSON', self)
        btn_export_json.clicked.connect(self.exportToJson)
        layout.addWidget(btn_export_json)

        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Export to JSON Example')
        self.show()

    def exportToJson(self):
        data_to_export = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save JSON File", "", "JSON Files (*.json)")

        if file_name:
            with open(file_name, 'w') as json_file:
                json.dump(data_to_export, json_file, indent=4)
            print(f"Data exported to {file_name}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())