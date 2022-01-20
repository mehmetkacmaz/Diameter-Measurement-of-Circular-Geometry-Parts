from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1761, 886)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_methods = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_methods.setGeometry(QtCore.QRect(590, 10, 561, 611))
        self.tabWidget_methods.setObjectName("tabWidget_methods")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 531, 91))
        self.groupBox.setObjectName("groupBox")
        self.label_radius_pixelCounter = QtWidgets.QLabel(self.groupBox)
        self.label_radius_pixelCounter.setGeometry(QtCore.QRect(460, 30, 61, 20))
        self.label_radius_pixelCounter.setFrameShape(QtWidgets.QFrame.Box)
        self.label_radius_pixelCounter.setText("")
        self.label_radius_pixelCounter.setObjectName("label_radius_pixelCounter")
        self.lineEdit_thresholdvalue = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_thresholdvalue.setGeometry(QtCore.QRect(70, 60, 61, 20))
        self.lineEdit_thresholdvalue.setObjectName("lineEdit_thresholdvalue")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(410, 30, 41, 20))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.pushButton_pixelCounter = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_pixelCounter.setGeometry(QtCore.QRect(10, 30, 391, 23))
        self.pushButton_pixelCounter.setObjectName("pushButton_pixelCounter")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 531, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_radius_circleFitting = QtWidgets.QLabel(self.groupBox_2)
        self.label_radius_circleFitting.setGeometry(QtCore.QRect(460, 30, 61, 20))
        self.label_radius_circleFitting.setFrameShape(QtWidgets.QFrame.Box)
        self.label_radius_circleFitting.setText("")
        self.label_radius_circleFitting.setObjectName("label_radius_circleFitting")
        self.pushButton_circleFitting = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_circleFitting.setGeometry(QtCore.QRect(10, 30, 391, 23))
        self.pushButton_circleFitting.setObjectName("pushButton_circleFitting")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(410, 30, 41, 20))
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.lineEdit_thresholdvalue_circle_fitting = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_thresholdvalue_circle_fitting.setGeometry(QtCore.QRect(70, 60, 61, 20))
        self.lineEdit_thresholdvalue_circle_fitting.setObjectName("lineEdit_thresholdvalue_circle_fitting")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(170, 60, 41, 20))
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.lineEdit_circle_fitting_points = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_circle_fitting_points.setGeometry(QtCore.QRect(210, 60, 61, 20))
        self.lineEdit_circle_fitting_points.setObjectName("lineEdit_circle_fitting_points")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 260, 531, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_devernay = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_devernay.setGeometry(QtCore.QRect(10, 30, 391, 23))
        self.pushButton_devernay.setObjectName("pushButton_devernay")
        self.label_radius_devernay = QtWidgets.QLabel(self.groupBox_3)
        self.label_radius_devernay.setGeometry(QtCore.QRect(460, 30, 61, 20))
        self.label_radius_devernay.setFrameShape(QtWidgets.QFrame.Box)
        self.label_radius_devernay.setText("")
        self.label_radius_devernay.setObjectName("label_radius_devernay")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(410, 30, 41, 20))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setObjectName("label_10")
        self.lineEdit_s = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_s.setGeometry(QtCore.QRect(40, 70, 51, 20))
        self.lineEdit_s.setObjectName("lineEdit_s")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(20, 70, 21, 16))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(110, 70, 21, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_l = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_l.setGeometry(QtCore.QRect(130, 70, 51, 20))
        self.lineEdit_l.setObjectName("lineEdit_l")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(200, 70, 21, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_h = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_h.setGeometry(QtCore.QRect(220, 70, 51, 20))
        self.lineEdit_h.setObjectName("lineEdit_h")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(290, 70, 21, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_w = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_w.setGeometry(QtCore.QRect(320, 70, 51, 20))
        self.lineEdit_w.setObjectName("lineEdit_w")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 390, 531, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_radius_matlab = QtWidgets.QLabel(self.groupBox_4)
        self.label_radius_matlab.setGeometry(QtCore.QRect(460, 30, 61, 20))
        self.label_radius_matlab.setFrameShape(QtWidgets.QFrame.Box)
        self.label_radius_matlab.setText("")
        self.label_radius_matlab.setObjectName("label_radius_matlab")
        self.pushButton_matlab = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_matlab.setGeometry(QtCore.QRect(10, 30, 391, 23))
        self.pushButton_matlab.setObjectName("pushButton_matlab")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(410, 30, 41, 20))
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setObjectName("label_12")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_16.setObjectName("label_16")
        self.lineEdit_thresholdvalue_matlab = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_thresholdvalue_matlab.setGeometry(QtCore.QRect(70, 60, 61, 20))
        self.lineEdit_thresholdvalue_matlab.setObjectName("lineEdit_thresholdvalue_matlab")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(150, 60, 61, 20))
        self.label_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_17.setObjectName("label_17")
        self.lineEdit_iters_matlab = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_iters_matlab.setGeometry(QtCore.QRect(210, 60, 61, 20))
        self.lineEdit_iters_matlab.setObjectName("lineEdit_iters_matlab")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(300, 60, 31, 20))
        self.label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_18.setObjectName("label_18")
        self.lineEdit_order_matlab = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_order_matlab.setGeometry(QtCore.QRect(340, 60, 61, 20))
        self.lineEdit_order_matlab.setObjectName("lineEdit_order_matlab")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(420, 60, 31, 20))
        self.label_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_19.setObjectName("label_19")
        self.lineEdit_color_matlab = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_color_matlab.setGeometry(QtCore.QRect(460, 60, 61, 20))
        self.lineEdit_color_matlab.setObjectName("lineEdit_color_matlab")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 520, 531, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_radius_zernikePy = QtWidgets.QLabel(self.groupBox_5)
        self.label_radius_zernikePy.setGeometry(QtCore.QRect(460, 30, 61, 20))
        self.label_radius_zernikePy.setFrameShape(QtWidgets.QFrame.Box)
        self.label_radius_zernikePy.setText("")
        self.label_radius_zernikePy.setObjectName("label_radius_zernikePy")
        self.pushButton_zernikePy = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_zernikePy.setGeometry(QtCore.QRect(10, 30, 391, 23))
        self.pushButton_zernikePy.setObjectName("pushButton_zernikePy")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(410, 30, 41, 20))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.tabWidget_methods.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_methods.addTab(self.tab_2, "")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 568, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_info = QtWidgets.QLabel(self.tab_4)
        self.label_info.setGeometry(QtCore.QRect(20, 10, 521, 431))
        self.label_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_info.setWordWrap(True)
        self.label_info.setObjectName("label_info")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 101, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 180, 101, 361))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_3.setGeometry(QtCore.QRect(120, 180, 101, 361))
        self.listWidget_3.setObjectName("listWidget_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(120, 150, 101, 391))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(230, 150, 101, 281))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_4.setGeometry(QtCore.QRect(230, 180, 101, 361))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_5 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_5.setGeometry(QtCore.QRect(340, 180, 101, 361))
        self.listWidget_5.setObjectName("listWidget_5")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_4.setGeometry(QtCore.QRect(340, 150, 101, 391))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_5.setGeometry(QtCore.QRect(450, 150, 101, 391))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        self.listWidget_6 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_6.setGeometry(QtCore.QRect(450, 180, 101, 361))
        self.listWidget_6.setObjectName("listWidget_6")
        self.pushButton_reset = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_reset.setGeometry(QtCore.QRect(10, 110, 541, 23))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_excelfilesfolder = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_excelfilesfolder.setGeometry(QtCore.QRect(10, 20, 541, 23))
        self.pushButton_excelfilesfolder.setObjectName("pushButton_excelfilesfolder")
        self.pushButton_create = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_create.setGeometry(QtCore.QRect(10, 80, 541, 23))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 541, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 550, 541, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget.raise_()
        self.listWidget_2.raise_()
        self.tableWidget_2.raise_()
        self.listWidget_3.raise_()
        self.tableWidget_3.raise_()
        self.listWidget_4.raise_()
        self.tableWidget_4.raise_()
        self.listWidget_5.raise_()
        self.tableWidget_5.raise_()
        self.listWidget_6.raise_()
        self.pushButton_reset.raise_()
        self.pushButton_excelfilesfolder.raise_()
        self.pushButton_create.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(9, 629, 1731, 215))
        self.groupBox_7.setObjectName("groupBox_7")
        self.listWidget_terminal = QtWidgets.QListWidget(self.groupBox_7)
        self.listWidget_terminal.setGeometry(QtCore.QRect(10, 20, 1711, 181))
        self.listWidget_terminal.setObjectName("listWidget_terminal")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(1164, 10, 589, 611))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_snapshots = QtWidgets.QLabel(self.tab_5)
        self.label_snapshots.setGeometry(QtCore.QRect(10, 10, 561, 561))
        self.label_snapshots.setFrameShape(QtWidgets.QFrame.Box)
        self.label_snapshots.setText("")
        self.label_snapshots.setObjectName("label_snapshots")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_plot = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_plot.setGeometry(QtCore.QRect(500, 10, 75, 23))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.pushButton_plot.raise_()
        self.tabWidget_2.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1761, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_methods.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(self.listWidget_2.clear)
        self.pushButton_2.clicked.connect(self.listWidget_3.clear)
        self.pushButton_2.clicked.connect(self.listWidget_4.clear)
        self.pushButton_2.clicked.connect(self.listWidget_5.clear)
        self.pushButton_2.clicked.connect(self.listWidget_6.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Pixel Counter"))
        self.lineEdit_thresholdvalue.setText(_translate("MainWindow", "254"))
        self.label_3.setText(_translate("MainWindow", "Radius:"))
        self.pushButton_pixelCounter.setText(_translate("MainWindow", "Pixel Counter"))
        self.label_5.setText(_translate("MainWindow", "Threshold:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Circle Fitting"))
        self.pushButton_circleFitting.setText(_translate("MainWindow", "Circle Fitting"))
        self.label_8.setText(_translate("MainWindow", "Radius:"))
        self.lineEdit_thresholdvalue_circle_fitting.setText(_translate("MainWindow", "254"))
        self.label_7.setText(_translate("MainWindow", "Threshold:"))
        self.label_9.setText(_translate("MainWindow", "Points:"))
        self.lineEdit_circle_fitting_points.setText(_translate("MainWindow", "200"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Devernay Method"))
        self.pushButton_devernay.setText(_translate("MainWindow", "Devernay Method"))
        self.label_10.setText(_translate("MainWindow", "Radius:"))
        self.lineEdit_s.setText(_translate("MainWindow", "0.0"))
        self.label_11.setText(_translate("MainWindow", "S:"))
        self.label_13.setText(_translate("MainWindow", "L:"))
        self.lineEdit_l.setText(_translate("MainWindow", "15.0"))
        self.label_14.setText(_translate("MainWindow", "H:"))
        self.lineEdit_h.setText(_translate("MainWindow", "15.0"))
        self.label_15.setText(_translate("MainWindow", "W:"))
        self.lineEdit_w.setText(_translate("MainWindow", "0.0"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Accurate Subpixel Edge Detection (Matlab Code)"))
        self.pushButton_matlab.setText(_translate("MainWindow", "Accurate Subpixel Edge Detection (Matlab Code)"))
        self.label_12.setText(_translate("MainWindow", "Radius:"))
        self.label_16.setText(_translate("MainWindow", "Threshold:"))
        self.lineEdit_thresholdvalue_matlab.setText(_translate("MainWindow", "25"))
        self.label_17.setText(_translate("MainWindow", "Iterations:"))
        self.lineEdit_iters_matlab.setText(_translate("MainWindow", "1"))
        self.label_18.setText(_translate("MainWindow", "Order:"))
        self.lineEdit_order_matlab.setText(_translate("MainWindow", "2"))
        self.label_19.setText(_translate("MainWindow", "Color:"))
        self.lineEdit_color_matlab.setText(_translate("MainWindow", "10"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Zernike Moment (Python)"))
        self.pushButton_zernikePy.setText(_translate("MainWindow", "Zernike Moment (Python)"))
        self.label_4.setText(_translate("MainWindow", "Radius:"))
        self.tabWidget_methods.setTabText(self.tabWidget_methods.indexOf(self.tab), _translate("MainWindow", "Methods"))
        self.tabWidget_methods.setTabText(self.tabWidget_methods.indexOf(self.tab_2), _translate("MainWindow", "Preparation"))
        self.label_info.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">README</span></p><p align=\"justify\"><span style=\" color:#ffffff;\">-</span>----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p><p align=\"justify\"><span style=\" font-size:9pt;\">• The program can only be used for outer diameter measurements of parts with circular geometry. It uses 5 different measurement methods: &quot;Pixel Counter&quot;, &quot;Circle Fitting&quot;, &quot;Devernay Method&quot;, &quot;Accurate Subpixel Edge Detection Method&quot; and &quot;Zernike Moment Method&quot;. Except for the first two of these methods, the others make measurements in subpixel size.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">• In the </span><span style=\" font-size:9pt; font-weight:600;\">&quot;Preparations&quot;</span><span style=\" font-size:9pt;\"> tab, initial settings will be made so that the program can work properly.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">• In the first step, click on the </span><span style=\" font-size:9pt; font-weight:600;\">&quot;Excel Files Folder&quot;</span><span style=\" font-size:9pt;\"> button and select the folder where the result files of the measurements will be located with </span><span style=\" font-size:9pt; font-weight:600;\">.csv</span><span style=\" font-size:9pt;\"> extension.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">• Then click the &quot;</span><span style=\" font-size:9pt; font-weight:600;\">Snapshots Folder</span><span style=\" font-size:9pt;\">&quot; button and select the folder where the images for which diameter values are to be obtained are located.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">• It provides configuration of folders to be created for</span><span style=\" font-size:9pt; font-weight:600;\"> Devernay Method</span><span style=\" font-size:9pt;\"> and </span><span style=\" font-size:9pt; font-weight:600;\">Accurate Subpixel Edge Detection (Matlab Code) Method</span><span style=\" font-size:9pt;\"> via </span><span style=\" font-size:9pt; font-weight:600;\">&quot;Create Environment&quot;</span><span style=\" font-size:9pt;\"> button. These files will be stored in the folder where the Excel files are located.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">• The </span><span style=\" font-size:9pt; font-weight:600;\">&quot;RESET&quot;</span><span style=\" font-size:9pt;\"> button should be used to clear the cookies of previous operations.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">• Then, by coming to the</span><span style=\" font-size:9pt; font-weight:600;\"> &quot;Methods&quot;</span><span style=\" font-size:9pt;\"> tab, any desired method can perform diameter measurements by simply pressing the relevant button.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">• Each measurement method has its own separate parameters and they can be easily adjusted via the UI.</span><br/></p><p align=\"justify\"><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Info"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pixel Counter"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Circle Fitting"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Devernay M."))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A. Subpixel E. D."))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Zernike Moment"))
        self.pushButton_reset.setText(_translate("MainWindow", "RESET"))
        self.pushButton_excelfilesfolder.setText(_translate("MainWindow", "Excel Files Folder"))
        self.pushButton_create.setText(_translate("MainWindow", "Create Environment"))
        self.pushButton.setText(_translate("MainWindow", "Snapshots Folder"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear Tables"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Measurement Results"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Output"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Snapshot"))
        self.pushButton_plot.setText(_translate("MainWindow", "Plot"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Analysis"))



#######################################################################################  MAIN PROGRAM  ###################################################################################################################

import os
import sys
import cv2
import time
import glob
from ctypes import *
import math
import random 

import numpy as np
import pandas as pd

from subpixel_edges import subpixel_edges

#GUI Design
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QListWidget
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

#Zernike Moment
from modules import *
from functions import *
        
class GUI(QMainWindow):  
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Diameter Measurement Program")
        self.show()      
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        
        self.ui.listWidget_terminal.addItem("~~ DIAMETER MEASUREMENT PROGRAM ~~\n")
        
        self.ui.label_snapshots.setPixmap(QPixmap('default_snapshot.bmp'))
        #self.ui.label_snapshots.resize(QPixmap('default_snapshot.bmp').width(), QPixmap('default_snapshot.bmp').height())
        self.ui.label_snapshots.setScaledContents(1)
        
        self.ui.pushButton_pixelCounter.clicked.connect(self.method_connected_components)
        self.ui.pushButton_circleFitting.clicked.connect(self.method_circle_fitting)
        self.ui.pushButton_devernay.clicked.connect(self.method_devernay)
        self.ui.pushButton_matlab.clicked.connect(self.method_matlab_code)
        self.ui.pushButton_zernikePy.clicked.connect(self.zernikeMomentPython)
        
        self.ui.pushButton_reset.clicked.connect(self.reset)
        self.ui.pushButton_create.clicked.connect(self.createEnvironment)
        self.ui.pushButton.clicked.connect(self.snapshot_folder_select)
        self.ui.pushButton_excelfilesfolder.clicked.connect(self.main_folder_select)
        
    def snapshot_folder_select(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        global snapshots_path
        snapshots_path = path
        
    def main_folder_select(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        global main_path
        main_path = path
    
    def file_list(self, dir):
        return [file for file in os.listdir(dir) if file.endswith('.bmp')]

    def count_files(self, dir):
        return len([1 for x in list(os.scandir(dir)) if x.is_file()])
    
    def createEnvironment(self):
        try:
            devernaypgm_path = main_path + "/devernay/pgm"
            devernaytxt_path = main_path + "/devernay/txt"
            
            os.makedirs(main_path + "/matlab")
            os.makedirs(devernaypgm_path)
            os.makedirs(devernaytxt_path)
            os.makedirs(main_path + "/zernike/cleaned")
            os.makedirs(main_path + "/results")
        
        except (FileExistsError):
            print("Folders Already Exists")
            self.ui.listWidget_terminal.addItem("- Folders Already Exists")
            pass
        except Exception as e:
            raise e
        
    def reset(self):
        matlab_path = main_path + "/matlab"
        devernaypgm_path = main_path + "/devernay/pgm"
        devernaytxt_path = main_path + "/devernay/txt"
        zernike_cleaned_path = main_path + "/zernike/cleaned"
        zernike_results_path = main_path + "/results"
        
        for f in os.listdir(matlab_path):
            os.remove(os.path.join(matlab_path, f))
    
        for f in os.listdir(devernaypgm_path):
            os.remove(os.path.join(devernaypgm_path, f))
            
        for f in os.listdir(devernaytxt_path):
            os.remove(os.path.join(devernaytxt_path, f))
            
        for f in os.listdir(zernike_cleaned_path):
            os.remove(os.path.join(zernike_cleaned_path, f))
        
    def method_connected_components(self):
        radius_list = []
        
        threshold_value = int(self.ui.lineEdit_thresholdvalue.text())
        
        numberoffiles = self.count_files(snapshots_path)
        file_list = self.file_list(snapshots_path)
        
        row = 0
        for i in range(numberoffiles):
            img = cv2.imread(snapshots_path + "/" + file_list[i],0)
            print(snapshots_path + "/" + file_list[i])
                            
            th, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
            
            #thresh = cv2.copyMakeBorder(thresh, 0, 200, 200, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])
            thresh = cv2.bitwise_not(thresh)

            im_floodfill = thresh.copy()
            h, w = thresh.shape[:2]
            mask = np.zeros((h+2, w+2), np.uint8)
            cv2.floodFill(im_floodfill, mask, (0,0), 255)
            im_floodfill_inv = cv2.bitwise_not(im_floodfill)
            im_out = thresh | im_floodfill_inv

            image = im_out.astype('uint8')
            nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=4)
            sizes = stats[:, -1]

            max_label = 1
            max_size = sizes[1]
            for i in range(2, nb_components):
                if sizes[i] > max_size:
                    max_label = i
                    max_size = sizes[i]

            img2 = np.zeros(output.shape)
            img2[output == max_label] = 1

            number_of_circle_pixels = np.sum(img2 == 1)
            
            radius = math.sqrt(number_of_circle_pixels/math.pi)
                
            print("number_of_green_pixels:      ", number_of_circle_pixels)
            print("diameter:                    ", radius*2)
            diameter = radius*2
            
            self.ui.label_radius_pixelCounter.setText(str(radius*2))
            radius_list.append(diameter)
        
        
        np.savetxt(main_path + "/pixelcounter.csv", radius_list)
        
        print(radius_list)
        radius_list = np.array(radius_list)
        
        radius_list_2 = np.around(radius_list,5).astype('str')
        
        self.ui.listWidget_2.addItems(radius_list_2)
        self.ui.listWidget_terminal.addItem("Connected Components - Pixel Counter has been completed...")
        self.ui.listWidget_terminal.addItem("Parameters are :         Threshold: " + str(threshold_value))
        
    def method_circle_fitting(self):
        def circleFit(x,y):
            numPoints = len(x)
            
            xx = np.square(x)
            yy = np.square(y)
            xy = np.multiply(x,y)
            
            bigA = np.array([[np.sum(x), np.sum(y), numPoints],
                            [np.sum(xy), np.sum(yy), np.sum(y)],
                            [np.sum(xx), np.sum(xy), np.sum(x)]])
            
            bigB = np.array([[-np.sum(np.add(xx, yy))],
                            [-np.sum(np.add(np.multiply(xx,y), np.multiply(yy,y)))],
                            [-np.sum(np.add(np.multiply(xx,x), np.multiply(xy,y)))]])
            
            a = np.linalg.solve(bigA,bigB)
            
            xCenter = -0.5*a[0]
            yCenter = -0.5*a[1]
            center = (xCenter[0], yCenter[0])
            radius = math.sqrt((pow(a[0], 2) + pow(a[1], 2))/4 - a[2])
            
            return radius*2
        
        numberoffiles = self.count_files(snapshots_path)
        file_list = self.file_list(snapshots_path)
        
        threshold_value = int(self.ui.lineEdit_thresholdvalue_circle_fitting.text())
        points = int(self.ui.lineEdit_circle_fitting_points.text())
        radius_list = []
        for i in range(numberoffiles):
            img = cv2.imread(snapshots_path + "/" + file_list[i],0)
            print(snapshots_path + "/" + file_list[i])

            #################################### DETECT OBJECT ##############################################
            ret,thresh = cv2.threshold(img,254,255,cv2.THRESH_BINARY_INV)

            contours,ret = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            sorted_areas = np.sort([cv2.contourArea(c) for c in contours])

            cnt=contours[[cv2.contourArea(c) for c in contours].index(sorted_areas[-1])] #the biggest contour

            a,b,w,h = cv2.boundingRect(cnt); cv2.rectangle(thresh, (a,b), (a+w, b+h), (0,255,0), 1)
            
            thresh = thresh[b-20:b+w+20, a-20:(a+h)+20]

            a,b = thresh.shape
            merkez = int(a/2)
            sinir1 = int(a/2 - (a/4))
            sinir2 = int(a/2 + (a/4))
            #################################################################################################

            resized = thresh

            im_floodfill = resized.copy()
            h, w = resized.shape[:2]
            mask = np.zeros((h+2, w+2), np.uint8)
            cv2.floodFill(im_floodfill, mask, (0,0), (255,255,255))
            im_floodfill_inv = cv2.bitwise_not(im_floodfill)
            im_out = resized | im_floodfill_inv

            hh, ww = im_out.shape[:2]
            
            coordinateMatrixX = []
            coordinateMatrixY = []

            for i in range(points):
                yValue = random.randint(sinir1, sinir2)
                center = (merkez,yValue)
                cy = center[1]

                row = thresh[cy:cy+1, 0:ww]

                coords = np.argwhere(row==255)
                num_coords = len(coords)
                start = coords[0]
                finish = coords[num_coords-1]
                start_pt = (start[1], cy)
                finish_pt = (finish[1], cy)
                
                coordinateMatrixX.append(start[1])
                coordinateMatrixY.append(cy)
                
                coordinateMatrixX.append(finish[1])
                coordinateMatrixY.append(cy)

            coordinateMatrix = np.concatenate((coordinateMatrixX, coordinateMatrixY), 0, dtype=int)

            x = coordinateMatrixX
            y = coordinateMatrixY
            print(circleFit(x,y))
            self.ui.label_radius_circleFitting.setText(str(circleFit(x,y)))

            radius_list.append(circleFit(x,y))

        np.savetxt(main_path + "/circlefitting.csv", radius_list)
        
        radius_list = np.array(radius_list)
        
        radius_list_2 = np.around(radius_list,5).astype('str')
        
        self.ui.listWidget_3.addItems(radius_list_2)
        
        self.ui.listWidget_terminal.addItem("Circle Fitting has been completed...")
        self.ui.listWidget_terminal.addItem("Parameters are :         Threshold: " + str(threshold_value) + "           Points: " + str(points))

    def method_devernay(self):
        
        def circleFit(x,y):
            numPoints = len(x)
            
            xx = np.square(x)
            yy = np.square(y)
            xy = np.multiply(x,y)
            
            bigA = np.array([[np.sum(x), np.sum(y), numPoints], [np.sum(xy), np.sum(yy), np.sum(y)], [np.sum(xx), np.sum(xy), np.sum(x)]])
            
            bigB = np.array([[-np.sum(np.add(xx, yy))], [-np.sum(np.add(np.multiply(xx,y), np.multiply(yy,y)))], [-np.sum(np.add(np.multiply(xx,x), np.multiply(xy,y)))]])
            
            a = np.linalg.solve(bigA,bigB)
            
            xCenter = -0.5*a[0]
            yCenter = -0.5*a[1]
            center = (xCenter[0], yCenter[0])
            #print(a)
            radius = math.sqrt((pow(a[0], 2) + pow(a[1], 2))/4 - a[2])
            
            return radius*2
        
        file_list = self.file_list(snapshots_path)        
        numberoffiles = self.count_files(snapshots_path)
                
        for i in range(numberoffiles):
            img = cv2.imread(snapshots_path + "/" + file_list[i],0)
            print(snapshots_path + "/" + file_list[i])
                        
            cv2.imwrite(main_path + "/devernay/pgm/" + str(i+1) + ".pgm", img)
            
            s = self.ui.lineEdit_s.text()
            l = self.ui.lineEdit_l.text()
            h = self.ui.lineEdit_h.text()
            w = self.ui.lineEdit_w.text()
            
            print(s,l,h,w)
            
            command = "devernay " + main_path + "/devernay/pgm/" + str(i+1) + ".pgm -t " + main_path + "/devernay/txt/" + str(i+1) + ".txt -s " + str(s) + " -l " + str(l) + " -h " + str(h) + " -w " + str(w)
            os.system(command)
            print(command)

        outer_radius = []
        
        for i in range(numberoffiles):
            x_array = []
            y_array = []
            split_number = []
            lengths = []
            with open(main_path + '/devernay/txt/' + str(i+1) + '.txt') as f:
                for line in f:
                    x, y = line.split()
                    x_array.append(x)
                    y_array.append(y)

            for i in range(len(x_array)):
                data = x_array[i]
                if data == "-1":
                    split_number.append(i)
                    
            x_splitted = np.split(x_array, split_number)
            y_splitted = np.split(y_array, split_number)

            x_splitted = sorted(x_splitted, key=len, reverse=True)
            y_splitted = sorted(y_splitted, key=len, reverse=True)


            x_splitted[0] = x_splitted[0][1::25]
            y_splitted[0] = y_splitted[0][1::25]    
            
            x_splitted_i = x_splitted[0].astype(float)
            y_splitted_i = y_splitted[0].astype(float)
            
            outer_radius.append(circleFit(x_splitted_i, y_splitted_i))
                    
            self.ui.label_radius_devernay.setText(str(circleFit(x_splitted_i, y_splitted_i)))
                    
        print("\nOuter Radius: {}".format(outer_radius))
        
        np.savetxt(main_path + "/devernay.csv", outer_radius)
        
        radius_list = np.array(outer_radius)
        
        radius_list_2 = np.around(radius_list,5).astype('str')
        
        self.ui.listWidget_4.addItems(radius_list_2)
        
        self.ui.listWidget_terminal.addItem("Devernay Method has been completed...")
        self.ui.listWidget_terminal.addItem("Parameters are :         s: " + str(s) + "           l: " + str(l) + "           h: " + str(h) + "           w: " + str(w))
    
    def method_matlab_code(self):
        def circleFit(x,y):
            numPoints = len(x)
            
            xx = np.square(x)
            yy = np.square(y)
            xy = np.multiply(x,y)
            
            bigA = np.array([[np.sum(x), np.sum(y), numPoints], [np.sum(xy), np.sum(yy), np.sum(y)], [np.sum(xx), np.sum(xy), np.sum(x)]])
            
            bigB = np.array([[-np.sum(np.add(xx, yy))], [-np.sum(np.add(np.multiply(xx,y), np.multiply(yy,y)))], [-np.sum(np.add(np.multiply(xx,x), np.multiply(xy,y)))]])
            
            a = np.linalg.solve(bigA,bigB)
            
            xCenter = -0.5*a[0]
            yCenter = -0.5*a[1]
            center = (xCenter[0], yCenter[0])
            #print(a)
            radius = math.sqrt((pow(a[0], 2) + pow(a[1], 2))/4 - a[2])
            
            return radius*2
        
        """
        os.getcwd()
        collection = "snapshots/"
        for i, filename in enumerate(os.listdir(collection)):
            os.rename("snapshots/" + filename, "snapshots/" + str(i+1) + ".bmp")"""

        numberoffiles = self.count_files(snapshots_path)
        file_list = self.file_list(snapshots_path)

        for i in range(numberoffiles):            
            img = cv2.imread(snapshots_path + "/" + file_list[i],0)
            print(snapshots_path + "/" + file_list[i])
            
            ret,thresh = cv2.threshold(img,254,255,cv2.THRESH_BINARY_INV)

            contours,ret = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            sorted_areas = np.sort([cv2.contourArea(c) for c in contours])

            cnt=contours[[cv2.contourArea(c) for c in contours].index(sorted_areas[-1])] #the biggest contour

            a,b,w,h = cv2.boundingRect(cnt); cv2.rectangle(thresh, (a,b), (a+w, b+h), (0,255,0), 1)
            
            thresh = thresh[b-20:b+w+20, a-20:(a+h)+20]

            im_out = thresh
            hh, ww = im_out.shape[:2]

            thresh = im_out.astype('uint8')
            nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(im_out)
            sizes = stats[:, -1]

            max_label = 1
            max_size = sizes[1]
            for q in range(2, nb_components):
                if sizes[q] > max_size:
                    max_label = q
                    max_size = sizes[q]

            im_out = np.zeros(output.shape)
            im_out[output == max_label] = 255

            im_out.clip(max=1)

            mask =np.array(im_out, dtype="uint8")

            img = img[b-20:b+w+20, a-20:(a+h)+20]
            
            masked = cv2.bitwise_and(img, img, mask=mask)

            masked[masked==0] = 255
            
            cv2.imwrite(main_path + "/matlab/" + str(i+1) + ".bmp", masked)
        
        radius_list = []
        
        th = self.ui.lineEdit_thresholdvalue_matlab.text()
        iters = self.ui.lineEdit_iters_matlab.text()
        order = self.ui.lineEdit_order_matlab.text()
        color = self.ui.lineEdit_color_matlab.text()
        
        for i in range(numberoffiles):
            
            img = cv2.imread(main_path + "/matlab/" + str(i+1) + ".bmp",0)
            print(main_path + "/matlab/" + str(i+1) + ".bmp")
            
            a,b = img.shape
            merkez = int(a/2)
            radius = int(a/2 - a/6)
            
            img = np.array(img).astype(float)
            circled = cv2.circle(img, (merkez,merkez), radius=radius, color=int(color), thickness=-1)
            edges = subpixel_edges(img, int(th), int(iters), int(order))
            
            """plt.imshow(img)
            plt.quiver(edges.x, edges.y, edges.nx, -edges.ny, scale=40)
            plt.show()"""

            x = edges.x
            y = edges.y
            radius_list.append(circleFit(x, y))
            self.ui.label_radius_matlab.setText(str(circleFit(x, y)))
            
                                
        print("Outer Radius: {}".format(radius_list))

        np.savetxt(main_path + "/matlab_code.csv", radius_list)
        
        radius_list = np.array(radius_list)
        
        radius_list_2 = np.around(radius_list,5).astype('str')
        
        self.ui.listWidget_5.addItems(radius_list_2)
        
        self.ui.listWidget_terminal.addItem("Accurate Subpixel Edge Detection (Matlab Code) has been completed...")
        self.ui.listWidget_terminal.addItem("Parameters are :         Threshold: " + str(th) + "           Iterations: " + str(iters) + "           Order: " + str(order) + "           Color: " + str(color))
        
    
    def zernikeMomentPython(self):
        
        datafolderlist = [['"directory"'], ['"' + main_path + '/zernike/cleaned/images"']]
        np.savetxt(main_path + "/dataFolder.csv", datafolderlist, delimiter=",", fmt ='% s')
        
        savetocsvlist = [['"directory"'], ['"' + main_path + '/results"']]
        np.savetxt(main_path + "/saveTo.csv", savetocsvlist, delimiter=",", fmt ='% s')
        
        def circleFit(x,y):
            numPoints = len(x)
            
            xx = np.square(x)
            yy = np.square(y)
            xy = np.multiply(x,y)
            
            bigA = np.array([[np.sum(x), np.sum(y), numPoints], [np.sum(xy), np.sum(yy), np.sum(y)], [np.sum(xx), np.sum(xy), np.sum(x)]])
            
            bigB = np.array([[-np.sum(np.add(xx, yy))], [-np.sum(np.add(np.multiply(xx,y), np.multiply(yy,y)))], [-np.sum(np.add(np.multiply(xx,x), np.multiply(xy,y)))]])
            
            a = np.linalg.solve(bigA,bigB)
            
            xCenter = -0.5*a[0]
            yCenter = -0.5*a[1]
            center = (xCenter[0], yCenter[0])
            #print(a)
            radius = math.sqrt((pow(a[0], 2) + pow(a[1], 2))/4 - a[2])
            
            return radius*2
        
        numberoffiles = self.count_files(snapshots_path)
        file_list = self.file_list(snapshots_path)

        for i in range(numberoffiles):            
            img = cv2.imread(snapshots_path + "/" + file_list[i],0)
            print(snapshots_path + "/" + file_list[i])
            
            ret,thresh = cv2.threshold(img,254,255,cv2.THRESH_BINARY_INV)

            contours,ret = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            sorted_areas = np.sort([cv2.contourArea(c) for c in contours])

            cnt=contours[[cv2.contourArea(c) for c in contours].index(sorted_areas[-1])] #the biggest contour

            a,b,w,h = cv2.boundingRect(cnt); cv2.rectangle(thresh, (a,b), (a+w, b+h), (0,255,0), 1)
            
            thresh = thresh[b-20:b+w+20, a-20:(a+h)+20]

            im_out = thresh
            hh, ww = im_out.shape[:2]

            thresh = im_out.astype('uint8')
            nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(im_out)
            sizes = stats[:, -1]

            max_label = 1
            max_size = sizes[1]
            for q in range(2, nb_components):
                if sizes[q] > max_size:
                    max_label = q
                    max_size = sizes[q]

            im_out = np.zeros(output.shape)
            im_out[output == max_label] = 255

            im_out.clip(max=1)

            mask =np.array(im_out, dtype="uint8")

            img = img[b-20:b+w+20, a-20:(a+h)+20]
            
            masked = cv2.bitwise_and(img, img, mask=mask)

            masked[masked==0] = 255
            
            masked = cv2.circle(masked, (380,380), 340, 10, thickness=-1)
            
            cv2.imwrite(main_path + "/zernike/cleaned/" + str(i+1) + ".bmp", masked)
            
        
        name_list = []
        process_list = []
        gpars_list = []
        weight_list = []

        numberoffiles = self.count_files(snapshots_path)
        
        for i in range(numberoffiles):
            name_list.append(str(i+1) + ".bmp")
            process_list.append("x")
            gpars_list.append("ghosal_edge_parameters.txt")
            weight_list.append("1500kg")
                    
        # Name,process,GPars,averageWeight

        df = pd.DataFrame({'Name': name_list, 'process': process_list, 'GPars': gpars_list, 'averageWeight': weight_list})
        print(df)

        df.to_csv(main_path + "/imageinfo.csv", index=False)
        
        ### Read Settings Files
        # the test matrix contains the names of images to be processed 
        # and information on how to process each one
        
        img_info = pd.read_csv(
            os.path.join(main_path,"imageinfo.csv"),sep=",")
        idx_cases = np.where(img_info.process == "x")
        img_info = img_info.iloc[idx_cases[0]] # remove images wo/ x
        ncases = len(img_info)
        # the folder where the results are to be saved
        
        save = pd.read_csv(os.path.join(main_path,"saveTo.csv"),sep="	").iloc[0].directory
        
        if not os.path.isdir(save):
            os.mkdir(save)
        
        # new folder with timestamp
        savedirect = os.path.join(save)
        if not os.path.isdir(savedirect):
            os.mkdir(savedirect)
        # the folder containing all the images
        datafolder = pd.read_csv(
            os.path.join(main_path,"dataFolder.csv")).iloc[0].directory

        ### cycle cases of img_info
        pbarc = tqdm(total=ncases) # progress bar
        for c in range(ncases):
            # files, files..
            direct = os.path.join(main_path + "/zernike/cleaned",img_info.iloc[c].Name)
            # read the output file of tune_ghosal to get the parameters for edge
            # detection, edge thresholding and blurring
            pars = read_external_data(
                os.path.join("Settings",str(img_info.iloc[c].GPars)))[0]
            K_s, k_min, k_max, l_max, phi_min, outlier_sigma, blur = \
                int(pars[0]),pars[1],pars[2],pars[3],pars[4],pars[5],pars[6]

            ## detection and saving	
            # open original image
            img_o = read_image(direct)
            h, w = img_o.shape
            # blur (i.e filter) image
            img_f = blur_image(img_o,blur)
            # detect edges: Ghosal
            edg_full, org = ghosal_edge_v2(img_f,K_s,kmax=k_max,
                kmin=k_min,lmax=l_max,phimin=phi_min,mirror=True)
            # save to savedirect with same name as img
            savename = os.path.splitext(os.path.basename(direct))[0]+".txt"
            savename = os.path.join(savedirect,savename)
            np.savetxt(savename,edg_full,delimiter="	")
            # progress bar
            pbarc.update(1)
        pbarc.close()
        
        ################################ TXT ################################
        
        rad_list = []
        for i in range(numberoffiles):
            path = main_path + "/results/" + str(i+1) + ".txt"
            
            x_array = []
            y_array = []
            with open(path) as f:
                for line in f:
                    x, y = line.split()
                    x_array.append(x)
                    y_array.append(y)
                    
            x_array = np.array(x_array); x_array = (np.reshape(x_array, (x_array.shape[0],1))).astype(float)
            y_array = np.array(y_array); y_array = (np.reshape(y_array, (y_array.shape[0],1))).astype(float)

            rad_list.append(circleFit(x_array, y_array))
                
            self.ui.label_radius_zernikePy.setText(str(circleFit(x_array, y_array)))
        
        print("Outer Radius: {}".format(rad_list))

        np.savetxt(main_path + "/zernike_moment_py.csv", rad_list)
        
        radius_list = np.array(rad_list)
        
        radius_list_2 = np.around(radius_list,5).astype('str')
        
        self.ui.listWidget_6.addItems(radius_list_2)
        
        self.ui.listWidget_terminal.addItem("Zernike Moments Method has been completed...")

application = QApplication([])
# Force the style to be the same on all OSs:
#application.setStyle("Fusion")
window = GUI()
window.show()

application.exec_()
