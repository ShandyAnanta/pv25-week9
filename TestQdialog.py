import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QInputDialog
)

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        self.list_button = QPushButton("Choose from list")
        self.list_button.clicked.connect(self.show_list_dialog)
        self.list_result = QLineEdit()
        row1.addWidget(self.list_button)
        row1.addWidget(self.list_result)
        main_layout.addLayout(row1)

        row2 = QHBoxLayout()
        self.name_button = QPushButton("get name")
        self.name_button.clicked.connect(self.show_name_dialog)
        self.name_result = QLineEdit()
        row2.addWidget(self.name_button)
        row2.addWidget(self.name_result)
        main_layout.addLayout(row2)

        row3 = QHBoxLayout()
        self.int_button = QPushButton("Enter an integer")
        self.int_button.clicked.connect(self.show_int_dialog)
        self.int_result = QLineEdit()
        row3.addWidget(self.int_button)
        row3.addWidget(self.int_result)
        main_layout.addLayout(row3)

        self.setLayout(main_layout)

    def show_list_dialog(self):
        items = ["C", "C++", "Java", "Python"]
        item, ok = QInputDialog.getItem(self, "select input dialog", "list of languages", items, 0, False)
        if ok and item:
            self.list_result.setText(item)

    def show_name_dialog(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.name_result.setText(text)

    def show_int_dialog(self):
        number, ok = QInputDialog.getInt(self, "integer input dialog", "enter a number")
        if ok:
            self.int_result.setText(str(number))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputDialogDemo()
    window.show()
    sys.exit(app.exec())
