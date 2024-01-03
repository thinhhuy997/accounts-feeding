import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog, QWidget

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.setWindowTitle('Dialog with Two Buttons')

        # Create layout
        layout = QVBoxLayout()

        # Create buttons
        button1 = QPushButton('Button 1', self)
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton('Button 2', self)
        button2.clicked.connect(self.button2_clicked)

        # Add buttons to layout
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Set the layout for the dialog
        self.setLayout(layout)

    def button1_clicked(self):
        print('Button 1 clicked')

    def button2_clicked(self):
        print('Button 2 clicked')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Main Window')

        # Create layout
        layout = QVBoxLayout()

        # Create button to open the dialog
        open_dialog_button = QPushButton('Open Dialog', self)
        open_dialog_button.clicked.connect(self.open_dialog)

        # Add button to layout
        layout.addWidget(open_dialog_button)

        # Set the layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_dialog(self):
        dialog = MyDialog(self)

        # Get the global position of the open_dialog_button
        button_pos = self.sender().mapToGlobal(self.sender().pos())

        # Adjust the position of the dialog
        dialog.move(button_pos.x() + 20, button_pos.y() + 20)

        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())