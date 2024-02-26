import validators
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QLineEdit, QAction
from constants.strings import AppStringConstants as Asc


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
        # Main Ui Initialization
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(Asc.mainUrl))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.browser)

        # Seating Up Tool Bar
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolTip("")
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # Tool Bar Back Action Button
        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.triggered.connect(self.browser.back)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Asc.backIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBack.setIcon(icon)
        self.actionBack.setObjectName(Asc.actionBack)

        # Tool Bar Forward Action Button
        self.actionForward = QtWidgets.QAction(MainWindow)
        self.actionForward.triggered.connect(self.browser.forward)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Asc.forwardIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon1)
        self.actionForward.setObjectName(Asc.actionForward)

        # Tool Bar Reload Button
        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.triggered.connect(self.browser.reload)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Asc.reloadIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReload.setIcon(icon2)
        self.actionReload.setObjectName(Asc.actionReload)

        # Tool Bar Home Navigation Button
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.triggered.connect(self.navigate_home)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(Asc.homeIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon3)
        self.actionHome.setObjectName(Asc.actionHome)

        # Tool Bar Stop Action Button
        self.actionStop = QAction(MainWindow)
        self.actionStop.triggered.connect(self.browser.stop)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(Asc.stopIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon4)
        self.actionStop.setObjectName(Asc.actionStop)

        # Tool Bar Url Bar Line Edit
        self.actionUrlBar = QLineEdit()
        self.actionUrlBar.setMaximumHeight(70)
        self.actionUrlBar.setMaximumHeight(100)
        self.actionUrlBar.returnPressed.connect(self.navigate_to_url)
        self.browser.urlChanged.connect(self.update_url)

        # Tool Bar Menu Action Button
        self.actionMenu = QAction(MainWindow)
        self.actionMenu.triggered.connect(self.print_page)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(Asc.menuIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMenu.setIcon((icon5))
        self.actionMenu.setObjectName(Asc.actionMenu)

        # Adding All Elements In Tool Bar
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
        self.browser.setUrl(QUrl(Asc.mainUrl))

    def navigate_to_url(self):
        url = self.actionUrlBar.text()
        if validators.url(f"https://{url}"):
            self.browser.setUrl(QUrl(f"https://{url}"))
        else:
            # self.browser.setUrl(QUrl(f"{Asc.googleMainUrl}/search?q={url.replace(" ", "+")}"))
            self.browser.setUrl(QUrl(f"{Asc.mainUrl}/?va=e&t=hh&q={url.replace(" ", "+")}&ia=web"))

    def update_url(self, q):
        self.actionUrlBar.setText(q.toString())

    def print_page(self):
        self.browser.page().printToPdf(Asc.pagePath)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionBack.setText(_translate("MainWindow", Asc.back))
        self.actionBack.setToolTip(_translate("MainWindow", "Go Back"))
        self.actionBack.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionForward.setText(_translate("MainWindow", Asc.forward))
        self.actionForward.setToolTip(_translate("MainWindow", "Go Forward"))
        self.actionForward.setShortcut(_translate("MainWindow", "Right"))
        self.actionReload.setText(_translate("MainWindow", "reload"))
        self.actionReload.setToolTip(_translate("MainWindow", Asc.reload))
        self.actionReload.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionHome.setText(_translate("MainWindow", "home"))
        self.actionHome.setToolTip(_translate("MainWindow", Asc.home))
        self.actionHome.setShortcut(_translate("MainWindow", "Ctrl+H"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon(Asc.appIcon))
    app.setApplicationName(Asc.appName)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet(open(Asc.style, "r").read())
    MainWindow.setWindowOpacity(0.95)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
