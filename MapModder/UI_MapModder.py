# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapModder.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1133, 690)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.listLayout = QtGui.QVBoxLayout()
        self.listLayout.setObjectName(_fromUtf8("listLayout"))
        self.dataLabel = QtGui.QLabel(self.centralwidget)
        self.dataLabel.setMinimumSize(QtCore.QSize(200, 0))
        self.dataLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dataLabel.setObjectName(_fromUtf8("dataLabel"))
        self.listLayout.addWidget(self.dataLabel)
        self.dataList = QtGui.QListWidget(self.centralwidget)
        self.dataList.setMinimumSize(QtCore.QSize(300, 0))
        self.dataList.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dataList.setObjectName(_fromUtf8("dataList"))
        self.listLayout.addWidget(self.dataList)
        self.horizontalLayout_2.addLayout(self.listLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graphicsLabel = QtGui.QLabel(self.centralwidget)
        self.graphicsLabel.setObjectName(_fromUtf8("graphicsLabel"))
        self.verticalLayout_2.addWidget(self.graphicsLabel)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(500, 0))
        brush = QtGui.QBrush(QtGui.QColor(200, 220, 255))
        brush.setStyle(QtCore.Qt.CrossPattern)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.palLayout = QtGui.QVBoxLayout()
        self.palLayout.setObjectName(_fromUtf8("palLayout"))
        self.palLabel = QtGui.QLabel(self.centralwidget)
        self.palLabel.setObjectName(_fromUtf8("palLabel"))
        self.palLayout.addWidget(self.palLabel)
        self.palList = QtGui.QListWidget(self.centralwidget)
        self.palList.setMinimumSize(QtCore.QSize(200, 350))
        self.palList.setObjectName(_fromUtf8("palList"))
        self.palLayout.addWidget(self.palList)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.palLayout.addWidget(self.checkBox_2)
        self.verticalLayout_3.addLayout(self.palLayout)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.labelEdit = QtGui.QLineEdit(self.centralwidget)
        self.labelEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.labelEdit.setObjectName(_fromUtf8("labelEdit"))
        self.gridLayout.addWidget(self.labelEdit, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.palAddrBox = HexSpinBox(self.centralwidget)
        self.palAddrBox.setMaximum(100000000)
        self.palAddrBox.setSingleStep(32)
        self.palAddrBox.setObjectName(_fromUtf8("palAddrBox"))
        self.gridLayout.addWidget(self.palAddrBox, 5, 1, 1, 1)
        self.yTileBox = QtGui.QSpinBox(self.centralwidget)
        self.yTileBox.setMinimum(1)
        self.yTileBox.setMaximum(256)
        self.yTileBox.setProperty("value", 16)
        self.yTileBox.setObjectName(_fromUtf8("yTileBox"))
        self.gridLayout.addWidget(self.yTileBox, 7, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        self.xTileBox = QtGui.QSpinBox(self.centralwidget)
        self.xTileBox.setMinimum(1)
        self.xTileBox.setMaximum(256)
        self.xTileBox.setProperty("value", 16)
        self.xTileBox.setObjectName(_fromUtf8("xTileBox"))
        self.gridLayout.addWidget(self.xTileBox, 6, 1, 1, 1)
        self.compCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.compCheckBox.setEnabled(False)
        self.compCheckBox.setText(_fromUtf8(""))
        self.compCheckBox.setObjectName(_fromUtf8("compCheckBox"))
        self.gridLayout.addWidget(self.compCheckBox, 8, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.regButton = QtGui.QPushButton(self.centralwidget)
        self.regButton.setMinimumSize(QtCore.QSize(150, 0))
        self.regButton.setObjectName(_fromUtf8("regButton"))
        self.gridLayout.addWidget(self.regButton, 9, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.palAddrStep = QtGui.QSpinBox(self.centralwidget)
        self.palAddrStep.setMinimum(1)
        self.palAddrStep.setMaximum(100000)
        self.palAddrStep.setProperty("value", 32)
        self.palAddrStep.setObjectName(_fromUtf8("palAddrStep"))
        self.gridLayout.addWidget(self.palAddrStep, 5, 3, 1, 1)
        self.addrStep = QtGui.QSpinBox(self.centralwidget)
        self.addrStep.setMinimum(1)
        self.addrStep.setMaximum(100000)
        self.addrStep.setObjectName(_fromUtf8("addrStep"))
        self.gridLayout.addWidget(self.addrStep, 1, 3, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.prevButton = QtGui.QPushButton(self.centralwidget)
        self.prevButton.setObjectName(_fromUtf8("prevButton"))
        self.horizontalLayout.addWidget(self.prevButton)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.addrBox = HexSpinBox(self.centralwidget)
        self.addrBox.setMaximum(100000000)
        self.addrBox.setObjectName(_fromUtf8("addrBox"))
        self.gridLayout.addWidget(self.addrBox, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtGui.QAction(MainWindow)
        self.openAction.setObjectName(_fromUtf8("openAction"))
        self.quitAction = QtGui.QAction(MainWindow)
        self.quitAction.setObjectName(_fromUtf8("quitAction"))
        self.menu.addAction(self.openAction)
        self.menu.addAction(self.quitAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.dataList, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), MainWindow.guiDataItemActivated)
        QtCore.QObject.connect(self.regButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.guiRegButtonPressed)
        QtCore.QObject.connect(self.palList, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), MainWindow.guiPalItemActivated)
        QtCore.QObject.connect(self.addrStep, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.guiAddrStepChanged)
        QtCore.QObject.connect(self.palAddrStep, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.guiPalAddrStepChanged)
        QtCore.QObject.connect(self.xTileBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.guiTileXChanged)
        QtCore.QObject.connect(self.yTileBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.guiTileYChanged)
        QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.guiNextMapPressed)
        QtCore.QObject.connect(self.prevButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.guiPrevMapPressed)
        QtCore.QObject.connect(self.palAddrBox, QtCore.SIGNAL(_fromUtf8("valueChanged(QString)")), MainWindow.guiPalAddrChanged)
        QtCore.QObject.connect(self.addrBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.guiAddrChanged)
        QtCore.QObject.connect(self.openAction, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.openFile)
        QtCore.QObject.connect(self.quitAction, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Map Modder ver 0.3 by ideal.exe", None))
        self.dataLabel.setText(_translate("MainWindow", "登録データ", None))
        self.graphicsLabel.setText(_translate("MainWindow", "イメージ", None))
        self.palLabel.setText(_translate("MainWindow", "パレット", None))
        self.checkBox_2.setText(_translate("MainWindow", "グレースケール", None))
        self.label_9.setText(_translate("MainWindow", "Step", None))
        self.label_3.setText(_translate("MainWindow", "Step", None))
        self.label_5.setText(_translate("MainWindow", "ラベル", None))
        self.label_8.setText(_translate("MainWindow", "圧縮", None))
        self.palAddrBox.setPrefix(_translate("MainWindow", "0x", None))
        self.label_2.setText(_translate("MainWindow", "Y", None))
        self.label_6.setText(_translate("MainWindow", "アドレス", None))
        self.label_7.setText(_translate("MainWindow", "パレット", None))
        self.regButton.setText(_translate("MainWindow", "リストに登録", None))
        self.label.setText(_translate("MainWindow", "X", None))
        self.prevButton.setToolTip(_translate("MainWindow", "アドレスを現在のマップと同じサイズだけ減算し，パレットはStepの値を減算します", None))
        self.prevButton.setStatusTip(_translate("MainWindow", "アドレスを現在のマップと同じサイズだけ減算し，パレットはStepの値を減算します", None))
        self.prevButton.setText(_translate("MainWindow", "前のマップ", None))
        self.nextButton.setToolTip(_translate("MainWindow", "アドレスを現在のマップと同じサイズだけ加算し，パレットはStepの値を加算します", None))
        self.nextButton.setStatusTip(_translate("MainWindow", "アドレスを現在のマップと同じサイズだけ加算し，パレットはStepの値を加算します", None))
        self.nextButton.setText(_translate("MainWindow", "次のマップ", None))
        self.addrBox.setPrefix(_translate("MainWindow", "0x", None))
        self.menu.setTitle(_translate("MainWindow", "ファイル", None))
        self.openAction.setText(_translate("MainWindow", "ファイルを開く", None))
        self.openAction.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.quitAction.setText(_translate("MainWindow", "終了", None))
        self.quitAction.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

from hexspinbox import HexSpinBox
