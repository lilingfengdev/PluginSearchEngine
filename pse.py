from plugin.engine.minebbs import Minebbs
from plugin.engine.klpbbs import Klpbbs
from plugin.engine.spigotmc import Spigot
from plugin.engine.tinksp import Tinksp
from concurrent.futures import ThreadPoolExecutor, wait
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTreeWidgetItem
from PySide6 import QtCore
import sys
import multiprocessing as m
from multiprocessing import Process as P
from ui import Ui_MainWindow
import pyperclip

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

def get_result(keyword, q):
    engine = [Spigot, Tinksp, Minebbs, Klpbbs]
    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_list = []
        for e in engine:
            future = executor.submit(e().search, keyword)
            print(0)
            future_list.append(future)
        wait(future_list)
        for future in future_list:
            for result in future.result():
                results.append(result)
                print(1)
    q.put(results)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.outputTreeWidget.itemDoubleClicked.connect(self.copyUrl)
    
    def search(self):
        self.ui.outputTreeWidget.clear()
        keyword = self.ui.searchLine.text()
        q = m.Queue()
        p = P(target=get_result, args=(keyword, q))
        p.start(); p.join(); results = q.get()
        for result in results:
            num = results.index(result)
            title = QTreeWidgetItem(self.ui.outputTreeWidget, [result.title, result.url, result.summary])
    
    def copyUrl(self, item):
        # copy a text to the clipboard.
        pyperclip.copy(item.text(1))
        QMessageBox.information(self, "Copied!", "已将该插件链接复制到剪贴板。")

if __name__ == "__main__":
    m.freeze_support()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
