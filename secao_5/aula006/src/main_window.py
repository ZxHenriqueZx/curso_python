import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from window import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.change_text)

    def change_text(self):
        text = self.lineEdit.text()
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    app.exec()
