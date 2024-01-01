import sys
import time
from PyQt5.QtCore import Qt, QRunnable, QObject, pyqtSignal, QThreadPool
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget

class WorkerSignals(QObject):
    started = pyqtSignal()
    finished = pyqtSignal()
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class Worker(QRunnable):
    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    def run(self):
        self.signals.started.emit()
        result = self.func(*self.args, **self.kwargs)
        self.signals.result.emit(result)
        self.signals.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.threadpool = QThreadPool()

        self.threadpool.setMaxThreadCount(2)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label_running = QLabel("Running threads: 0", self)
        self.label_waiting = QLabel("Waiting threads: 0", self)
        self.label_completed = QLabel("Completed threads: 0", self)

        self.layout.addWidget(self.label_running)
        self.layout.addWidget(self.label_waiting)
        self.layout.addWidget(self.label_completed)

        self.start_button = QPushButton("Start Threads", self)
        self.start_button.clicked.connect(self.start_threads)
        self.layout.addWidget(self.start_button)

        self.thread_counter = 0
        self.completed_threads = 0

    def start_threads(self):
        for _ in range(5):  # Create 5 threads
            worker = Worker(self.do_work)
            worker.signals.started.connect(self.thread_started)
            worker.signals.finished.connect(self.thread_finished)

            self.threadpool.start(worker)

    def do_work(self):
        # Simulate some work
        for _ in range(5):
            time.sleep(1)
        return "Thread completed."

    def thread_started(self):
        self.thread_counter += 1
        self.update_labels()

    def thread_finished(self):
        self.thread_counter -= 1
        self.completed_threads += 1
        self.update_labels()

    def update_labels(self):
        running_threads = self.threadpool.activeThreadCount()
        waiting_threads = self.threadpool.waitForDone(msecs=0)  # Consider using QThreadPool::reserveThread() for waiting count
        completed_threads = self.completed_threads

        self.label_running.setText(f"Running threads: {running_threads}")
        self.label_waiting.setText(f"Waiting threads: {waiting_threads}")
        self.label_completed.setText(f"Completed threads: {completed_threads}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())