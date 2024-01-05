import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QTextEdit, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a button
        button = QPushButton('Show Dialog', self)
        button.clicked.connect(self.showDialog)

        # Set up the main window
        layout = QVBoxLayout()
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('PyQt5 Dialog Example')
        self.setGeometry(100, 100, 400, 300)

    def showDialog(self):
        # Create a larger dialog
        dialog = QDialog(self)
        dialog.setWindowTitle('Dialog with Text Edit')
        dialog.setGeometry(100, 100, 500, 400)  # Set the size of the dialog

        # Create a text edit box
        text_edit = QTextEdit(dialog)
        text_edit.setGeometry(10, 10, 480, 300)

        # Add Save button to close the dialog
        save_button = QPushButton('Save', dialog)
        save_button.clicked.connect(lambda: self.onSaveClicked(dialog, text_edit.toPlainText()))

        # Set up the layout
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(text_edit)
        dialog_layout.addWidget(save_button)

        dialog.setLayout(dialog_layout)

        # Show the dialog
        dialog.exec_()

    def onSaveClicked(self, dialog, text):
        lines = text.splitlines()
        print("Text lines:")
        for line in lines:
            print(line)
        dialog.accept()  # Close the dialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())