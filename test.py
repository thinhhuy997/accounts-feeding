from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QItemSelectionModel
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a table widget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

        # Populate the table with some data
        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem(f"Row {row}, Col {col}")
                self.tableWidget.setItem(row, col, item)

        # Create a button
        self.button = QPushButton("Show Selected Indices", self)
        self.button.clicked.connect(self.showSelectedIndices)

        # Set up the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Connect to selection model's selectionChanged signal
        selection_model = self.tableWidget.selectionModel()
        selection_model.selectionChanged.connect(self.selectionChanged)

    def selectionChanged(self, selected, deselected):
        selected_rows = set(index.row() for index in selected.indexes())

        # Check if entire rows are selected
        if all(self.tableWidget.selectionModel().rowSpan(index.row()) == self.tableWidget.columnCount() for index in selected.indexes()):
            print("Entire Rows Selected:", selected_rows)
        else:
            print("Partial Rows Selected")

    def showSelectedIndices(self):
        # Get selected items
        selected_items = self.tableWidget.selectedItems()

        # Extract row indices from selected items
        selected_rows = set(item.row() for item in selected_items)

        # Display the selected indices
        print("Selected Indices:", selected_rows)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec_()