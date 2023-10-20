from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication, QWidget
from workerui_code import Ui_Form
import sys
import time

class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
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
        self.pushButton_2.clicked.connect(self.hard_worker2) 

    def hard_worker1(self):
        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        #Mover o worker para a thread
        worker.moveToThread(thread)

        #Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1_start)
        worker.progressed.connect(self.worker1_progress)
        worker.finished.connect(self.worker1_finish)

        thread.start()

    def worker1_start(self, value):
        self.pushButton.setDisabled(True)
        self.label.setText(value)

    def worker1_progress(self, value):
        self.label.setText(value)

    def worker1_finish(self):
        self.pushButton.setDisabled(False)
        self.label.setText('acabou')

    def hard_worker2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker2 = self._worker2
        thread2 = self._thread2

        worker2.moveToThread(thread2)
        
        thread2.started.connect(worker2.doWork)
        worker2.finished.connect(thread2.quit)

        thread2.finished.connect(thread2.deleteLater)
        worker2.finished.connect(worker2.deleteLater)

        worker2.started.connect(self.worker2_start)
        worker2.progressed.connect(self.worker2_progress)
        worker2.finished.connect(self.worker2_finish)

        thread2.start()

    def worker2_start(self, value):
        self.pushButton_2.setDisabled(True)
        self.label_2.setText(value)

    def worker2_progress(self, value):
        self.label_2.setText(value)

    def worker2_finish(self):
        self.pushButton_2.setDisabled(False)
        self.label_2.setText('acabou')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    mywidget.show()

    app.exec()

