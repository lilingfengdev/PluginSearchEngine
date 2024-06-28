from core.search import search
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTreeWidgetItem
from PySide6.QtCore import QObject, QThread, Signal
import sys
from ui import Ui_MainWindow
import pyperclip


class Worker(QObject):
    _signal = Signal(list)

    def __init__(self):
        super().__init__()
        # print("000")

    def work(self, keyword):
        try:
            results = search(keyword)
            print("searching...")
            self._signal.emit(results)
            print("emitted signal _")
        except Exception as e:
            print(e)


class MainWindow(QMainWindow):
    a = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = Worker()
        self.worker_thread = QThread()
        self.worker._signal.connect(self.shower)
        self.worker.moveToThread(self.worker_thread)
        self.a.connect(self.worker.work)
        self.ui.searchButton.clicked.connect(self.searcher)
        self.ui.outputTreeWidget.itemDoubleClicked.connect(self.copyurl)
        self.worker_thread.start()

    def searcher(self):
        keyword = self.ui.searchLine.text()
        self.ui.outputTreeWidget.clear()
        self.a.emit(keyword)

    def shower(self, results):
        for result in results:
            title = QTreeWidgetItem(self.ui.outputTreeWidget, [result.title, result.url, result.summary])

    def copyurl(self, item):
        # copy a text to the clipboard.
        pyperclip.copy(item.text(1))
        QMessageBox.information(self, "Copied!", "Copied the link to the clipboard!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    QMessageBox.information(window, "Usage", """1. Enter a keyword in the search box and click the search button.
2. Double click on the link to copy it to the clipboard.""")
    window.show()
    sys.exit(app.exec())
