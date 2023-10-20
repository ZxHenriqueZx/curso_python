from PySide6.QtWidgets import QApplication, QWidget
from workerui_code import Ui_Form
import sys

class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    mywidget.show()

    app.exec()
