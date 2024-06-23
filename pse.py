from plugin.engine.minebbs import Minebbs
from plugin.engine.klpbbs import Klpbbs
from plugin.engine.spigotmc import Spigot
from plugin.engine.tinksp import Tinksp
from concurrent.futures import ThreadPoolExecutor, wait
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTreeWidgetItem
from PySide6.QtCore import QObject, QThread, Signal, QSize
from PySide6.QtGui import QIcon
import sys
from ui import Ui_MainWindow
import pyperclip

class Worker(QObject):
    _signal = Signal(list)
    _warner = Signal(str)

    def __init__(self):
        super().__init__()

    def work(self, keyword):
        try:
            engine = [Spigot, Tinksp, Minebbs, Klpbbs]
            results = []
            with ThreadPoolExecutor(max_workers=6) as executor:
                future_list = []
                for e in engine:
                    future = executor.submit(e().search, keyword)
                    future_list.append(future)
                wait(future_list)
                for future in future_list:
                    for result in future.result():
                        results.append(result)
            self._signal.emit(results)
        except Exception as e:
            self._warner.emit(str(e))

class MainWindow(QMainWindow):
    a = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = Worker()
        self.worker_thread = QThread()
        self.worker._signal.connect(self.shower)
        self.worker._warner.connect(self.showWarning)
        self.worker.moveToThread(self.worker_thread)
        self.a.connect(self.worker.work)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.outputTreeWidget.itemDoubleClicked.connect(self.copyUrl)
        self.worker_thread.start()
        icon = QIcon()
        icon.addFile(u"o.ico", QSize(), QIcon.Normal, QIcon.Off)

    def search(self):
        self.ui.progressBar.setMaximum(0)
        keyword = self.ui.searchLine.text()
        self.ui.outputTreeWidget.clear()
        self.a.emit(keyword)
        self.ui.progressBar.setFormat("进行中")

    def shower(self, results):
        for result in results:
            num = results.index(result)
            title = QTreeWidgetItem(self.ui.outputTreeWidget, [result.title, result.url, result.summary])
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setFormat("  未开始")
    
    def copyUrl(self, item):
        # copy a text to the clipboard.
        pyperclip.copy(item.text(1))
        QMessageBox.information(self, "Copied!", "已将该插件链接复制到剪贴板。")

    def showWarning(self, message):
        QMessageBox.information(self, "Error! 发生错误! 尝试关闭VPN / 更换网络环境 / 更换关键词。", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
