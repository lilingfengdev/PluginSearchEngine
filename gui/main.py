from core.search import search
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTreeWidgetItem
from PySide6.QtCore import QObject, QThread, Signal
import sys
from gui.ui import Ui_MainWindow
import pyperclip


class Worker(QObject):
    _signal = Signal(list)

    def __init__(self):
        super().__init__()
        # print("000")

    def work(self, lyst: list):
        keyword, boolean = lyst[0], lyst[1]
        print("Working")
        results = search(keyword, boolean)
        print("searching...")
        self._signal.emit(results)
        print("emitted signal _")


class MainWindow(QMainWindow):
    a = Signal(list)

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
        self.ui.progressBar.setMaximum(0)
        keyword = self.ui.searchLine.text()
        self.ui.outputTreeWidget.clear()
        state = self.ui.checkBox.checkState()
        print(state)
        translation = True if state == self.ui.checkBox.checkState().Unchecked else False
        self.a.emit([keyword, translation])

    def shower(self, results):
        for result in results:
            title = QTreeWidgetItem(self.ui.outputTreeWidget, [result.title, result.url, result.summary])
        self.ui.progressBar.setMaximum(100)

    def copyurl(self, item):
        # copy a text to the clipboard.
        pyperclip.copy(item.text(1))
        QMessageBox.information(self, "Copied!", "已将链接复制到剪贴板！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    QMessageBox.information(window, "Usage", """1. 在搜索框中输入关键字，点击搜索按钮。
2. 双击链接将其复制到剪贴板。""")
    window.show()
    sys.exit(app.exec())
