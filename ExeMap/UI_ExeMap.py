# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ideal\Dropbox\Program\EXE6_Tools\ExeMap\ExeMap.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self._2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self._2.setObjectName("_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.openButton = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        self.openButton.setMinimumSize(QtCore.QSize(32, 32))
        self.openButton.setObjectName("openButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.openButton)
        self.saveButton = QtWidgets.QToolButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setMinimumSize(QtCore.QSize(32, 32))
        self.saveButton.setObjectName("saveButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.saveButton)
        self._2.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mapListGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mapListGroupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.mapListGroupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mapListGroupBox.setObjectName("mapListGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mapListGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mapList = QtWidgets.QListWidget(self.mapListGroupBox)
        self.mapList.setAlternatingRowColors(True)
        self.mapList.setObjectName("mapList")
        self.verticalLayout.addWidget(self.mapList)
        self.attributeGroupBox = QtWidgets.QGroupBox(self.mapListGroupBox)
        self.attributeGroupBox.setObjectName("attributeGroupBox")
        self.formLayout_5 = QtWidgets.QFormLayout(self.attributeGroupBox)
        self.formLayout_5.setObjectName("formLayout_5")
        self.widthLabel = QtWidgets.QLabel(self.attributeGroupBox)
        self.widthLabel.setObjectName("widthLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.widthLabel)
        self.heightLabel = QtWidgets.QLabel(self.attributeGroupBox)
        self.heightLabel.setObjectName("heightLabel")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.heightLabel)
        self.widthValueLabel = QtWidgets.QLabel(self.attributeGroupBox)
        self.widthValueLabel.setObjectName("widthValueLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widthValueLabel)
        self.heightValueLabel = QtWidgets.QLabel(self.attributeGroupBox)
        self.heightValueLabel.setObjectName("heightValueLabel")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.heightValueLabel)
        self.tileMapLabel = QtWidgets.QLabel(self.attributeGroupBox)
        self.tileMapLabel.setObjectName("tileMapLabel")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.tileMapLabel)
        self.tileMapValueLabel = QtWidgets.QLabel(self.attributeGroupBox)
        self.tileMapValueLabel.setObjectName("tileMapValueLabel")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tileMapValueLabel)
        self.verticalLayout.addWidget(self.attributeGroupBox)
        self.horizontalLayout.addWidget(self.mapListGroupBox)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.mapTab = QtWidgets.QWidget()
        self.mapTab.setObjectName("mapTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mapTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.mapTab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setMinimumSize(QtCore.QSize(400, 0))
        brush = QtGui.QBrush(QtGui.QColor(150, 200, 255))
        brush.setStyle(QtCore.Qt.CrossPattern)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_4.addWidget(self.graphicsView)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tilesetTable = QtWidgets.QTableWidget(self.groupBox_2)
        self.tilesetTable.setShowGrid(False)
        self.tilesetTable.setRowCount(64)
        self.tilesetTable.setColumnCount(16)
        self.tilesetTable.setObjectName("tilesetTable")
        self.tilesetTable.horizontalHeader().setVisible(False)
        self.tilesetTable.horizontalHeader().setDefaultSectionSize(16)
        self.tilesetTable.verticalHeader().setVisible(False)
        self.tilesetTable.verticalHeader().setDefaultSectionSize(16)
        self.verticalLayout_3.addWidget(self.tilesetTable)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.paletteTable = QtWidgets.QTableWidget(self.groupBox)
        self.paletteTable.setRowCount(16)
        self.paletteTable.setColumnCount(16)
        self.paletteTable.setObjectName("paletteTable")
        self.paletteTable.horizontalHeader().setDefaultSectionSize(20)
        self.paletteTable.verticalHeader().setVisible(True)
        self.paletteTable.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout_2.addWidget(self.paletteTable)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.layerBox = QtWidgets.QGroupBox(self.frame)
        self.layerBox.setMinimumSize(QtCore.QSize(200, 0))
        self.layerBox.setMaximumSize(QtCore.QSize(400, 150))
        self.layerBox.setObjectName("layerBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layerBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.layerBox)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.radioButton = QtWidgets.QRadioButton(self.layerBox)
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layerBox)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layerBox)
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radioButton_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layerBox)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layerBox)
        self.radioButton_3.setText("")
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.radioButton_3)
        self.verticalLayout_4.addWidget(self.layerBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addWidget(self.frame)
        self.tabWidget.addTab(self.mapTab, "")
        self.movementTab = QtWidgets.QWidget()
        self.movementTab.setObjectName("movementTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.movementTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.movementTab)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_3.addWidget(self.graphicsView_2)
        self.tabWidget.addTab(self.movementTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self._2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.mapList.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.map_entry_selected)
        self.checkBox_2.toggled['bool'].connect(MainWindow.bg2_visible_changed)
        self.checkBox_3.toggled['bool'].connect(MainWindow.bg1_visible_changed)
        self.graphicsView.rubberBandChanged['QRect','QPointF','QPointF'].connect(MainWindow.rubber_band_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EXE Map"))
        self.openButton.setText(_translate("MainWindow", "Open ROM"))
        self.saveButton.setText(_translate("MainWindow", "Save ROM"))
        self.mapListGroupBox.setTitle(_translate("MainWindow", "Map List"))
        self.attributeGroupBox.setTitle(_translate("MainWindow", "Map Attribute"))
        self.widthLabel.setText(_translate("MainWindow", "Width:"))
        self.heightLabel.setText(_translate("MainWindow", "Height:"))
        self.widthValueLabel.setText(_translate("MainWindow", "-"))
        self.heightValueLabel.setText(_translate("MainWindow", "-"))
        self.tileMapLabel.setText(_translate("MainWindow", "Tile Map Offset:"))
        self.tileMapValueLabel.setText(_translate("MainWindow", "-"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Tile Set"))
        self.groupBox.setTitle(_translate("MainWindow", "Palette"))
        self.layerBox.setTitle(_translate("MainWindow", "Layer"))
        self.checkBox.setText(_translate("MainWindow", "Movement"))
        self.checkBox_2.setText(_translate("MainWindow", "BG2"))
        self.checkBox_3.setText(_translate("MainWindow", "BG1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapTab), _translate("MainWindow", "Map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.movementTab), _translate("MainWindow", "Movement"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

