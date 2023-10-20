from PySide6.QtWidgets import QApplication, QWidget
from workerui_code import Ui_Form
import sys
import time

class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.hard_worker1)
        self.pushButton_2.clicked.connect(self.hard_worker2)

    def hard_worker1(self):
        for i in range(5):
            print(i)
            time.sleep(i)
        self.label.setText('clicado1')

    def hard_worker2(self):
        for i in range(5):
            print(i)
            time.sleep(i)
        self.label_2.setText('clicado2')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    mywidget.show()

    app.exec()
