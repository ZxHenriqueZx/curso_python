from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QApplication, QWidget
from workerui_code import Ui_Form
import sys
import time

class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)

class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.hard_worker1)
        #self.pushButton_2.clicked.connect(self.hard_worker2)

    def hard_worker1(self):
        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        #Mover o worker para a thread
        worker.moveToThread(thread)

        #Run
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)

        thread.finished.connect(self.deleteLater)
        worker.finished.connect(self.deleteLater)

        worker.started.connect(self.worker1_start)
        worker.progressed.connect(self.worker1_progress)
        worker.finished.connect(self.worker1_finish)

        thread.start()

    def worker1_start(self, value):
        self.label.setText(value)
        self.pushButton.setDisabled(True)

    def worker1_progress(self, value):
        self.label.setText(value)

    def worker1_finish(self):
        self.pushButton.setDisabled(False)
        print('acabou')

    def hard_worker2(self):
        self.label_2.setText('clicado2')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    mywidget.show()

    app.exec()

