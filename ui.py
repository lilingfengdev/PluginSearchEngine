# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 594)
        icon = QIcon()
        icon.addFile(u"o.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QTreeView {\n"
"	border:none\n"
"}\n"
"")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionSearchType = QAction(MainWindow)
        self.actionSearchType.setObjectName(u"actionSearchType")
        icon1 = QIcon()
        icon1.addFile(u"icons/radio-circle-marked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSearchType.setIcon(icon1)
        self.actionSearchName = QAction(MainWindow)
        self.actionSearchName.setObjectName(u"actionSearchName")
        icon2 = QIcon()
        icon2.addFile(u"icons/radio-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSearchName.setIcon(icon2)
        self.actionTextViewer = QAction(MainWindow)
        self.actionTextViewer.setObjectName(u"actionTextViewer")
        self.actionPlayerViewer = QAction(MainWindow)
        self.actionPlayerViewer.setObjectName(u"actionPlayerViewer")
        self.actionImageViewer = QAction(MainWindow)
        self.actionImageViewer.setObjectName(u"actionImageViewer")
        self.actionSearchWeb = QAction(MainWindow)
        self.actionSearchWeb.setObjectName(u"actionSearchWeb")
        self.actionSearchWeb.setIcon(icon2)
        self.actionSearchKey = QAction(MainWindow)
        self.actionSearchKey.setObjectName(u"actionSearchKey")
        self.actionSearchKey.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.groupBox.setMouseTracking(False)
        self.groupBox.setTabletTracking(False)
        self.groupBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.searchButton = QPushButton(self.groupBox)
        self.searchButton.setObjectName(u"searchButton")

        self.gridLayout.addWidget(self.searchButton, 0, 1, 1, 1)

        self.searchLine = QLineEdit(self.groupBox)
        self.searchLine.setObjectName(u"searchLine")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLine.sizePolicy().hasHeightForWidth())
        self.searchLine.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.searchLine, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.outputTreeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        self.outputTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.outputTreeWidget.setObjectName(u"outputTreeWidget")
        self.outputTreeWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.outputTreeWidget.sizePolicy().hasHeightForWidth())
        self.outputTreeWidget.setSizePolicy(sizePolicy1)
        self.outputTreeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.outputTreeWidget.setProperty("showDropIndicator", True)
        self.outputTreeWidget.setIndentation(20)
        self.outputTreeWidget.setRootIsDecorated(False)
        self.outputTreeWidget.setUniformRowHeights(False)
        self.outputTreeWidget.setItemsExpandable(True)
        self.outputTreeWidget.setSortingEnabled(False)
        self.outputTreeWidget.setAnimated(False)
        self.outputTreeWidget.setAllColumnsShowFocus(False)
        self.outputTreeWidget.setHeaderHidden(False)
        self.outputTreeWidget.setExpandsOnDoubleClick(True)
        self.outputTreeWidget.setColumnCount(3)
        self.outputTreeWidget.header().setVisible(True)
        self.outputTreeWidget.header().setCascadingSectionResizes(False)
        self.outputTreeWidget.header().setMinimumSectionSize(25)
        self.outputTreeWidget.header().setDefaultSectionSize(100)
        self.outputTreeWidget.header().setHighlightSections(False)

        self.verticalLayout_2.addWidget(self.outputTreeWidget)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PluginSearchEngine", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u4f5c\u8005", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u7528\u6cd5", None))
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionSearchType.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b\u641c\u7d22", None))
        self.actionSearchName.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0\u641c\u7d22", None))
        self.actionTextViewer.setText(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u67e5\u770b\u5668", None))
        self.actionPlayerViewer.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u64ad\u653e\u5668", None))
        self.actionImageViewer.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u67e5\u770b\u5668", None))
        self.actionSearchWeb.setText(QCoreApplication.translate("MainWindow", u"Web\u641c\u7d22", None))
        self.actionSearchKey.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5173\u952e\u5b57\u641c\u7d22", None))
#if QT_CONFIG(accessibility)
        self.groupBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.groupBox.setTitle("")
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.searchLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u60f3\u67e5\u8be2\u7684\u63d2\u4ef6", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"  \u672a\u5f00\u59cb", None))
        ___qtreewidgetitem = self.outputTreeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u7b80\u4ecb", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
    # retranslateUi

