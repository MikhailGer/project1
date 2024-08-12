# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sattings-app.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(800, 707)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/tune_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        mainWindow.setAnimated(True)
        mainWindow.setDocumentMode(False)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBox_ports = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ports.setObjectName("comboBox_ports")
        self.verticalLayout_2.addWidget(self.comboBox_ports)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_mods = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_mods.setObjectName("comboBox_mods")
        self.comboBox_mods.addItem("")
        self.comboBox_mods.setItemText(0, "")
        self.comboBox_mods.addItem("")
        self.comboBox_mods.addItem("")
        self.comboBox_mods.addItem("")
        self.comboBox_mods.addItem("")
        self.verticalLayout.addWidget(self.comboBox_mods)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page_0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_0 = QtWidgets.QLabel(self.page_0)
        self.label_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_0.setObjectName("label_0")
        self.horizontalLayout_9.addWidget(self.label_0)
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_1 = QtWidgets.QGroupBox(self.page_1)
        self.groupBox_1.setObjectName("groupBox_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_1)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.comboBox_disc_selector = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_disc_selector.setObjectName("comboBox_disc_selector")
        self.verticalLayout_7.addWidget(self.comboBox_disc_selector)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.comboBox_ID_name = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_ID_name.setObjectName("comboBox_ID_name")
        self.comboBox_ID_name.addItem("")
        self.comboBox_ID_name.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox_ID_name)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.CreateDisc = QtWidgets.QPushButton(self.groupBox_2)
        self.CreateDisc.setObjectName("CreateDisc")
        self.verticalLayout_9.addWidget(self.CreateDisc)
        self.Results = QtWidgets.QPushButton(self.groupBox_2)
        self.Results.setEnabled(False)
        self.Results.setObjectName("Results")
        self.verticalLayout_9.addWidget(self.Results)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.DeleteDisc = QtWidgets.QPushButton(self.groupBox_2)
        self.DeleteDisc.setEnabled(False)
        self.DeleteDisc.setObjectName("DeleteDisc")
        self.verticalLayout_8.addWidget(self.DeleteDisc)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.pushButton_device_settings = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_device_settings.setObjectName("pushButton_device_settings")
        self.verticalLayout_9.addWidget(self.pushButton_device_settings)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_6.addWidget(self.groupBox_1)
        self.stackedWidget.addWidget(self.page_1)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.lineEdit_sampleID_scaning = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_sampleID_scaning.setEnabled(False)
        self.lineEdit_sampleID_scaning.setObjectName("lineEdit_sampleID_scaning")
        self.verticalLayout_12.addWidget(self.lineEdit_sampleID_scaning)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.listView_scaning = QtWidgets.QListView(self.groupBox_3)
        self.listView_scaning.setObjectName("listView_scaning")
        self.verticalLayout_13.addWidget(self.listView_scaning)
        self.progressBar_scaning = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar_scaning.setProperty("value", 24)
        self.progressBar_scaning.setObjectName("progressBar_scaning")
        self.verticalLayout_13.addWidget(self.progressBar_scaning)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.verticalLayout_11.addWidget(self.groupBox_3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_17.addWidget(self.label_6)
        self.lineEdit_sampleID_training = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_sampleID_training.setEnabled(False)
        self.lineEdit_sampleID_training.setObjectName("lineEdit_sampleID_training")
        self.verticalLayout_17.addWidget(self.lineEdit_sampleID_training)
        self.verticalLayout_16.addLayout(self.verticalLayout_17)
        self.listView_training = QtWidgets.QListView(self.groupBox_4)
        self.listView_training.setObjectName("listView_training")
        self.verticalLayout_16.addWidget(self.listView_training)
        self.verticalLayout_15.addLayout(self.verticalLayout_16)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_training_previous = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_training_previous.setObjectName("pushButton_training_previous")
        self.horizontalLayout_5.addWidget(self.pushButton_training_previous)
        self.pushButton_training_invalid = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_training_invalid.setObjectName("pushButton_training_invalid")
        self.horizontalLayout_5.addWidget(self.pushButton_training_invalid)
        self.pushButton_training_valid = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_training_valid.setObjectName("pushButton_training_valid")
        self.horizontalLayout_5.addWidget(self.pushButton_training_valid)
        self.pushButton_training_next = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_training_next.setObjectName("pushButton_training_next")
        self.horizontalLayout_5.addWidget(self.pushButton_training_next)
        self.verticalLayout_15.addLayout(self.horizontalLayout_5)
        self.pushButton_training_save = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_training_save.setObjectName("pushButton_training_save")
        self.verticalLayout_15.addWidget(self.pushButton_training_save)
        self.verticalLayout_18.addWidget(self.groupBox_4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_20.addWidget(self.label_7)
        self.lineEdit_base_motor_steps = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_base_motor_steps.setObjectName("lineEdit_base_motor_steps")
        self.verticalLayout_20.addWidget(self.lineEdit_base_motor_steps)
        self.verticalLayout_31.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_21.addWidget(self.label_8)
        self.lineEdit_base_motor_speed = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_base_motor_speed.setObjectName("lineEdit_base_motor_speed")
        self.verticalLayout_21.addWidget(self.lineEdit_base_motor_speed)
        self.verticalLayout_31.addLayout(self.verticalLayout_21)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_23.addWidget(self.label_14)
        self.lineEdit_base_acceleration = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_base_acceleration.setObjectName("lineEdit_base_acceleration")
        self.verticalLayout_23.addWidget(self.lineEdit_base_acceleration)
        self.verticalLayout_31.addLayout(self.verticalLayout_23)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_30.addWidget(self.label_15)
        self.lineEdit_base_MaxSpeed = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_base_MaxSpeed.setObjectName("lineEdit_base_MaxSpeed")
        self.verticalLayout_30.addWidget(self.lineEdit_base_MaxSpeed)
        self.verticalLayout_31.addLayout(self.verticalLayout_30)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_22.addWidget(self.label_9)
        self.comboBox_base_motor_dir = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_base_motor_dir.setObjectName("comboBox_base_motor_dir")
        self.comboBox_base_motor_dir.addItem("")
        self.comboBox_base_motor_dir.addItem("")
        self.verticalLayout_22.addWidget(self.comboBox_base_motor_dir)
        self.verticalLayout_31.addLayout(self.verticalLayout_22)
        self.pushButton_base_motor = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_base_motor.setObjectName("pushButton_base_motor")
        self.verticalLayout_31.addWidget(self.pushButton_base_motor)
        self.horizontalLayout_7.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_11 = QtWidgets.QLabel(self.groupBox_7)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_26.addWidget(self.label_11)
        self.lineEdit_stand_motor_steps = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_stand_motor_steps.setObjectName("lineEdit_stand_motor_steps")
        self.verticalLayout_26.addWidget(self.lineEdit_stand_motor_steps)
        self.verticalLayout_33.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_12 = QtWidgets.QLabel(self.groupBox_7)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_27.addWidget(self.label_12)
        self.lineEdit_stand_motor_speed = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_stand_motor_speed.setObjectName("lineEdit_stand_motor_speed")
        self.verticalLayout_27.addWidget(self.lineEdit_stand_motor_speed)
        self.verticalLayout_33.addLayout(self.verticalLayout_27)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_16 = QtWidgets.QLabel(self.groupBox_7)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_25.addWidget(self.label_16)
        self.lineEdit_head_acceleration = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_head_acceleration.setObjectName("lineEdit_head_acceleration")
        self.verticalLayout_25.addWidget(self.lineEdit_head_acceleration)
        self.verticalLayout_33.addLayout(self.verticalLayout_25)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_17 = QtWidgets.QLabel(self.groupBox_7)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_32.addWidget(self.label_17)
        self.lineEdit_head_MaxSpeed = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_head_MaxSpeed.setObjectName("lineEdit_head_MaxSpeed")
        self.verticalLayout_32.addWidget(self.lineEdit_head_MaxSpeed)
        self.verticalLayout_33.addLayout(self.verticalLayout_32)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_13 = QtWidgets.QLabel(self.groupBox_7)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_28.addWidget(self.label_13)
        self.comboBox_stand_motor_dir = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_stand_motor_dir.setObjectName("comboBox_stand_motor_dir")
        self.comboBox_stand_motor_dir.addItem("")
        self.comboBox_stand_motor_dir.addItem("")
        self.verticalLayout_28.addWidget(self.comboBox_stand_motor_dir)
        self.verticalLayout_33.addLayout(self.verticalLayout_28)
        self.pushButton_stand_motor = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_stand_motor.setObjectName("pushButton_stand_motor")
        self.verticalLayout_33.addWidget(self.pushButton_stand_motor)
        self.horizontalLayout_7.addWidget(self.groupBox_7)
        self.verticalLayout_29.addLayout(self.horizontalLayout_7)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_24.addWidget(self.label_10)
        self.listView_tenzo = QtWidgets.QListView(self.groupBox_5)
        self.listView_tenzo.setObjectName("listView_tenzo")
        self.verticalLayout_24.addWidget(self.listView_tenzo)
        self.verticalLayout_29.addLayout(self.verticalLayout_24)
        self.verticalLayout_19.addWidget(self.groupBox_5)
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout_2.addWidget(self.groupBox)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.loop_start = QtWidgets.QAction(mainWindow)
        self.loop_start.setCheckable(True)
        self.loop_start.setChecked(False)
        self.loop_start.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/cycle_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/cycle_24dp_00FF00_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/icons/cycle_24dp_00FF00_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.loop_start.setIcon(icon1)
        self.loop_start.setAutoRepeat(True)
        self.loop_start.setObjectName("loop_start")
        self.loop_stop = QtWidgets.QAction(mainWindow)
        self.loop_stop.setCheckable(False)
        self.loop_stop.setChecked(False)
        self.loop_stop.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/close_24dp_FF0000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loop_stop.setIcon(icon2)
        self.loop_stop.setObjectName("loop_stop")
        self.toolBar.addAction(self.loop_start)
        self.toolBar.addAction(self.loop_stop)

        self.retranslateUi(mainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.loop_stop.triggered['bool'].connect(self.loop_stop.setDisabled) # type: ignore
        self.loop_stop.triggered['bool'].connect(self.loop_start.toggle) # type: ignore
        self.loop_start.toggled['bool'].connect(self.loop_stop.setEnabled) # type: ignore
        self.loop_stop.triggered['bool'].connect(self.loop_start.setDisabled) # type: ignore
        self.loop_start.toggled['bool'].connect(self.loop_start.setDisabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.comboBox_ports, self.comboBox_mods)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Панель управления установкой"))
        self.label.setText(_translate("mainWindow", "Выбрать порт"))
        self.label_2.setText(_translate("mainWindow", "Режим работы"))
        self.comboBox_mods.setItemText(1, _translate("mainWindow", "1.Полный диск"))
        self.comboBox_mods.setItemText(2, _translate("mainWindow", "2.Часть диска"))
        self.comboBox_mods.setItemText(3, _translate("mainWindow", "3.Обучение"))
        self.comboBox_mods.setItemText(4, _translate("mainWindow", "4.Отладка"))
        self.label_0.setText(_translate("mainWindow", "Выберите порт и режим работы установки"))
        self.groupBox_1.setTitle(_translate("mainWindow", "Параметры режима"))
        self.label_3.setText(_translate("mainWindow", "Выбрать образец"))
        self.label_4.setText(_translate("mainWindow", "Отоброзить по:"))
        self.comboBox_ID_name.setItemText(0, _translate("mainWindow", "ID"))
        self.comboBox_ID_name.setItemText(1, _translate("mainWindow", "Name"))
        self.CreateDisc.setText(_translate("mainWindow", "Создать новый образец"))
        self.Results.setText(_translate("mainWindow", "Результаты образца"))
        self.DeleteDisc.setText(_translate("mainWindow", "Удалить выбранный образец"))
        self.pushButton_device_settings.setText(_translate("mainWindow", "Настройки установки"))
        self.groupBox_3.setTitle(_translate("mainWindow", "Сканирование"))
        self.label_5.setText(_translate("mainWindow", "Образец"))
        self.lineEdit_sampleID_scaning.setText(_translate("mainWindow", "1111111231"))
        self.groupBox_4.setTitle(_translate("mainWindow", "Обучение"))
        self.label_6.setText(_translate("mainWindow", "Образец"))
        self.lineEdit_sampleID_training.setText(_translate("mainWindow", "1111111231"))
        self.pushButton_training_previous.setText(_translate("mainWindow", "Предыдущая"))
        self.pushButton_training_invalid.setText(_translate("mainWindow", "Не годная"))
        self.pushButton_training_valid.setText(_translate("mainWindow", "Годная"))
        self.pushButton_training_next.setText(_translate("mainWindow", "Следующая"))
        self.pushButton_training_save.setText(_translate("mainWindow", "Сохранить"))
        self.groupBox_5.setTitle(_translate("mainWindow", "Отладка"))
        self.groupBox_6.setTitle(_translate("mainWindow", "Двигатель основания"))
        self.label_7.setText(_translate("mainWindow", "количество шагов"))
        self.label_8.setText(_translate("mainWindow", "начальная скорость вращения"))
        self.label_14.setText(_translate("mainWindow", "ускорение"))
        self.label_15.setText(_translate("mainWindow", "максимальная скорость"))
        self.label_9.setText(_translate("mainWindow", "направление вращения"))
        self.comboBox_base_motor_dir.setItemText(0, _translate("mainWindow", "по часовой"))
        self.comboBox_base_motor_dir.setItemText(1, _translate("mainWindow", "против часовой"))
        self.pushButton_base_motor.setText(_translate("mainWindow", "двигать"))
        self.groupBox_7.setTitle(_translate("mainWindow", "Двигатель установки"))
        self.label_11.setText(_translate("mainWindow", "количество шагов"))
        self.label_12.setText(_translate("mainWindow", "начальная скорость вращения"))
        self.label_16.setText(_translate("mainWindow", "ускорение"))
        self.label_17.setText(_translate("mainWindow", "максимальная скорость"))
        self.label_13.setText(_translate("mainWindow", "направление вращения"))
        self.comboBox_stand_motor_dir.setItemText(0, _translate("mainWindow", "по часовой"))
        self.comboBox_stand_motor_dir.setItemText(1, _translate("mainWindow", "против часовой"))
        self.pushButton_stand_motor.setText(_translate("mainWindow", "двигать"))
        self.label_10.setText(_translate("mainWindow", "показания тензодатчика"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.loop_start.setText(_translate("mainWindow", "Начать цикл"))
        self.loop_start.setToolTip(_translate("mainWindow", "Начать цикл с заданными параметрами"))
        self.loop_stop.setText(_translate("mainWindow", "Остановить цикл"))
        self.loop_stop.setToolTip(_translate("mainWindow", "Остановить выполнение цикла"))
