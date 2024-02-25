from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QLineEdit, QAction

from constants.strings import *


class Ui_MainWindow(object):
    def __init__(self):
        self.actionStop = None
        self.actionMenu = None
        self.actionUrlBar = None
        self.actionHome = None
        self.actionReload = None
        self.actionForward = None
        self.actionBack = None
        self.toolBar = None
        self.centralwidget = None
        self.browser = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 640)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(mainUrl))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.browser)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolTip("")
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.triggered.connect(self.browser.back)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(backIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBack.setIcon(icon)
        self.actionBack.setObjectName("actionBack")

        self.actionForward = QtWidgets.QAction(MainWindow)
        self.actionForward.triggered.connect(self.browser.forward)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(forwardIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon1)
        self.actionForward.setObjectName("actionForward")

        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.triggered.connect(self.browser.reload)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(reloadIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReload.setIcon(icon2)
        self.actionReload.setObjectName("actionReload")

        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.triggered.connect(self.navigate_home)

        self.actionUrlBar = QLineEdit()
        self.actionUrlBar.setMaximumHeight(70)
        self.actionUrlBar.setMaximumHeight(100)
        self.actionUrlBar.returnPressed.connect(self.navigate_to_url)
        self.browser.urlChanged.connect(self.update_url)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(homeIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon3)
        self.actionHome.setObjectName("actionHome")

        self.actionStop = QAction(MainWindow)
        self.actionStop.triggered.connect(self.browser.stop)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(stopIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon4)
        self.actionStop.setObjectName("actionStop")

        self.actionMenu = QAction(MainWindow)
        self.actionMenu.triggered.connect(self.print_page)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(menuIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMenu.setIcon((icon5))
        self.actionMenu.setObjectName("actionMenu")

        self.toolBar.addAction(self.actionBack)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionForward)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionReload)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addWidget(self.actionUrlBar)
        self.toolBar.addAction(self.actionMenu)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def navigate_home(self):
        self.browser.setUrl(QUrl(mainUrl))

    def navigate_to_url(self):
        if "www" or "com" or "in" or "net" == self.actionUrlBar.text():
            url = self.actionUrlBar.text()
            self.browser.setUrl(QUrl(f"https://{url}"))
        else:
            self.browser.setUrl(QUrl(f"https://www.google.com/search?q={self.actionUrlBar.text()}"))

    def update_url(self, q):
        self.actionUrlBar.setText(q.toString())

    def print_page(self):
        self.browser.page().printToPdf(pagePath)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionBack.setText(_translate("MainWindow", "Back"))
        self.actionBack.setToolTip(_translate("MainWindow", "Go Back"))
        self.actionBack.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionForward.setText(_translate("MainWindow", "forward"))
        self.actionForward.setToolTip(_translate("MainWindow", "Go Forward"))
        self.actionForward.setShortcut(_translate("MainWindow", "Right"))
        self.actionReload.setText(_translate("MainWindow", "reload"))
        self.actionReload.setToolTip(_translate("MainWindow", "Reload"))
        self.actionReload.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionHome.setText(_translate("MainWindow", "home"))
        self.actionHome.setToolTip(_translate("MainWindow", "Home"))
        self.actionHome.setShortcut(_translate("MainWindow", "Ctrl+H"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon(appIcon))
    app.setApplicationName(appName)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet(open(style, "r").read())
    MainWindow.setWindowOpacity(0.95)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
