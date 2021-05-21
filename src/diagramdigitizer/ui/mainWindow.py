# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src\diagramdigitizer\ui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 718)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ccd5db, stop: 1 #34617e);\n"
"    min-width: 1200px;\n"
"    min-height: 640px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidgetHead = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidgetHead.setStyleSheet("")
        self.stackedWidgetHead.setObjectName("stackedWidgetHead")
        self.pageHeadMenu = QtWidgets.QWidget()
        self.pageHeadMenu.setObjectName("pageHeadMenu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pageHeadMenu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.pageHeadMenu)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.stackedWidgetHead.addWidget(self.pageHeadMenu)
        self.pageHeadProject = QtWidgets.QWidget()
        self.pageHeadProject.setObjectName("pageHeadProject")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.pageHeadProject)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_2 = QtWidgets.QLabel(self.pageHeadProject)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_16.addWidget(self.label_2)
        self.stackedWidgetHead.addWidget(self.pageHeadProject)
        self.pageHeadAxes = QtWidgets.QWidget()
        self.pageHeadAxes.setObjectName("pageHeadAxes")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.pageHeadAxes)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_3 = QtWidgets.QLabel(self.pageHeadAxes)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_17.addWidget(self.label_3)
        self.stackedWidgetHead.addWidget(self.pageHeadAxes)
        self.pageHeadData = QtWidgets.QWidget()
        self.pageHeadData.setObjectName("pageHeadData")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.pageHeadData)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_4 = QtWidgets.QLabel(self.pageHeadData)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_18.addWidget(self.label_4)
        self.stackedWidgetHead.addWidget(self.pageHeadData)
        self.pageHeadExport = QtWidgets.QWidget()
        self.pageHeadExport.setObjectName("pageHeadExport")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.pageHeadExport)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_5 = QtWidgets.QLabel(self.pageHeadExport)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_19.addWidget(self.label_5)
        self.stackedWidgetHead.addWidget(self.pageHeadExport)
        self.pageHeadInfo = QtWidgets.QWidget()
        self.pageHeadInfo.setObjectName("pageHeadInfo")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.pageHeadInfo)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_17 = QtWidgets.QLabel(self.pageHeadInfo)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_21.addWidget(self.label_17)
        self.stackedWidgetHead.addWidget(self.pageHeadInfo)
        self.verticalLayout_5.addWidget(self.stackedWidgetHead)
        self.frameCenter = QtWidgets.QFrame(self.centralwidget)
        self.frameCenter.setStyleSheet("#frameCenter {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;    \n"
"    background: white;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ddd, stop: 0.5 #ffffff, stop: 1 #cdcdcd);\n"
"}\n"
"\n"
"QComboBox\n"
"{   \n"
"    border: 1px solid #222;\n"
"    border-radius: 3;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     color: white;     \n"
" }\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 1px solid #222;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"}")
        self.frameCenter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCenter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCenter.setObjectName("frameCenter")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frameCenter)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stackedWidgetNavigation = QtWidgets.QStackedWidget(self.frameCenter)
        self.stackedWidgetNavigation.setMinimumSize(QtCore.QSize(340, 430))
        self.stackedWidgetNavigation.setMaximumSize(QtCore.QSize(400, 16777215))
        self.stackedWidgetNavigation.setStyleSheet("QStackedWidget {\n"
"    border: 1px solid #444;\n"
"    border-radius: 5px;    \n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #cccccc, stop: 1 #949393);\n"
"   margin-top: 10px;\n"
"}")
        self.stackedWidgetNavigation.setObjectName("stackedWidgetNavigation")
        self.pageMenu = QtWidgets.QWidget()
        self.pageMenu.setStyleSheet("QPushButton{\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    font-weight: bold; \n"
"    font-size: 15px;\n"
"    color: white;\n"
"    min-width: 200px;\n"
"    min-height: 60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20ff25, stop: 1 #10a613);\n"
"}")
        self.pageMenu.setObjectName("pageMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageMenu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonProject = QtWidgets.QPushButton(self.pageMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonProject.sizePolicy().hasHeightForWidth())
        self.buttonProject.setSizePolicy(sizePolicy)
        self.buttonProject.setMinimumSize(QtCore.QSize(204, 64))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/project_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonProject.setIcon(icon)
        self.buttonProject.setIconSize(QtCore.QSize(60, 60))
        self.buttonProject.setObjectName("buttonProject")
        self.verticalLayout_2.addWidget(self.buttonProject)
        self.buttonAxes = QtWidgets.QPushButton(self.pageMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonAxes.sizePolicy().hasHeightForWidth())
        self.buttonAxes.setSizePolicy(sizePolicy)
        self.buttonAxes.setMinimumSize(QtCore.QSize(204, 64))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/axes_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAxes.setIcon(icon1)
        self.buttonAxes.setIconSize(QtCore.QSize(60, 60))
        self.buttonAxes.setObjectName("buttonAxes")
        self.verticalLayout_2.addWidget(self.buttonAxes)
        self.buttonData = QtWidgets.QPushButton(self.pageMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonData.sizePolicy().hasHeightForWidth())
        self.buttonData.setSizePolicy(sizePolicy)
        self.buttonData.setMinimumSize(QtCore.QSize(204, 64))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/data_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonData.setIcon(icon2)
        self.buttonData.setIconSize(QtCore.QSize(60, 60))
        self.buttonData.setObjectName("buttonData")
        self.verticalLayout_2.addWidget(self.buttonData)
        self.buttonExport = QtWidgets.QPushButton(self.pageMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonExport.sizePolicy().hasHeightForWidth())
        self.buttonExport.setSizePolicy(sizePolicy)
        self.buttonExport.setMinimumSize(QtCore.QSize(204, 64))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/export_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonExport.setIcon(icon3)
        self.buttonExport.setIconSize(QtCore.QSize(60, 60))
        self.buttonExport.setObjectName("buttonExport")
        self.verticalLayout_2.addWidget(self.buttonExport)
        self.buttonInfo = QtWidgets.QPushButton(self.pageMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonInfo.sizePolicy().hasHeightForWidth())
        self.buttonInfo.setSizePolicy(sizePolicy)
        self.buttonInfo.setMinimumSize(QtCore.QSize(204, 64))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/info_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonInfo.setIcon(icon4)
        self.buttonInfo.setIconSize(QtCore.QSize(60, 60))
        self.buttonInfo.setObjectName("buttonInfo")
        self.verticalLayout_2.addWidget(self.buttonInfo)
        self.buttonQuit = QtWidgets.QPushButton(self.pageMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonQuit.sizePolicy().hasHeightForWidth())
        self.buttonQuit.setSizePolicy(sizePolicy)
        self.buttonQuit.setMinimumSize(QtCore.QSize(204, 64))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/quit_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonQuit.setIcon(icon5)
        self.buttonQuit.setIconSize(QtCore.QSize(60, 60))
        self.buttonQuit.setObjectName("buttonQuit")
        self.verticalLayout_2.addWidget(self.buttonQuit)
        self.stackedWidgetNavigation.addWidget(self.pageMenu)
        self.pageProject = QtWidgets.QWidget()
        self.pageProject.setStyleSheet("QPushButton{\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    font-weight: bold; \n"
"    font-size: 15px;\n"
"    color: white;\n"
"    min-width: 200px;\n"
"    min-height: 60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20ff25, stop: 1 #10a613);\n"
"}")
        self.pageProject.setObjectName("pageProject")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pageProject)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttonNewProject = QtWidgets.QPushButton(self.pageProject)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonNewProject.sizePolicy().hasHeightForWidth())
        self.buttonNewProject.setSizePolicy(sizePolicy)
        self.buttonNewProject.setMinimumSize(QtCore.QSize(204, 64))
        self.buttonNewProject.setObjectName("buttonNewProject")
        self.verticalLayout_3.addWidget(self.buttonNewProject)
        self.buttonOpenProject = QtWidgets.QPushButton(self.pageProject)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonOpenProject.sizePolicy().hasHeightForWidth())
        self.buttonOpenProject.setSizePolicy(sizePolicy)
        self.buttonOpenProject.setMinimumSize(QtCore.QSize(204, 64))
        self.buttonOpenProject.setObjectName("buttonOpenProject")
        self.verticalLayout_3.addWidget(self.buttonOpenProject)
        self.buttonSaveProject = QtWidgets.QPushButton(self.pageProject)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.buttonSaveProject.sizePolicy().hasHeightForWidth())
        self.buttonSaveProject.setSizePolicy(sizePolicy)
        self.buttonSaveProject.setMinimumSize(QtCore.QSize(204, 64))
        self.buttonSaveProject.setObjectName("buttonSaveProject")
        self.verticalLayout_3.addWidget(self.buttonSaveProject)
        spacerItem = QtWidgets.QSpacerItem(20, 256, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.stackedWidgetNavigation.addWidget(self.pageProject)
        self.pageAxes = QtWidgets.QWidget()
        self.pageAxes.setStyleSheet("QPushButton{\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    font-weight: bold; \n"
"    font-size: 15px;\n"
"    color: white;\n"
"    min-width: 130px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.pageAxes.setObjectName("pageAxes")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pageAxes)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.pageAxes)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        spacerItem1 = QtWidgets.QSpacerItem(332, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.pageAxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(310, 0))
        self.frame_4.setStyleSheet("QPushButton:checked{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4a42ec, stop: 1 #0d04ba);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #302c8c, stop: 1 #1b1863);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonPlaceX0 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(130)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.buttonPlaceX0.sizePolicy().hasHeightForWidth())
        self.buttonPlaceX0.setSizePolicy(sizePolicy)
        self.buttonPlaceX0.setMinimumSize(QtCore.QSize(134, 44))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/xmin_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlaceX0.setIcon(icon6)
        self.buttonPlaceX0.setIconSize(QtCore.QSize(40, 40))
        self.buttonPlaceX0.setCheckable(True)
        self.buttonPlaceX0.setObjectName("buttonPlaceX0")
        self.gridLayout.addWidget(self.buttonPlaceX0, 0, 0, 1, 1)
        self.lineEditX0 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditX0.sizePolicy().hasHeightForWidth())
        self.lineEditX0.setSizePolicy(sizePolicy)
        self.lineEditX0.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEditX0.setFont(font)
        self.lineEditX0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditX0.setObjectName("lineEditX0")
        self.gridLayout.addWidget(self.lineEditX0, 0, 1, 1, 1)
        self.buttonPlaceX1 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(130)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.buttonPlaceX1.sizePolicy().hasHeightForWidth())
        self.buttonPlaceX1.setSizePolicy(sizePolicy)
        self.buttonPlaceX1.setMinimumSize(QtCore.QSize(134, 44))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/xmax_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlaceX1.setIcon(icon7)
        self.buttonPlaceX1.setIconSize(QtCore.QSize(40, 40))
        self.buttonPlaceX1.setCheckable(True)
        self.buttonPlaceX1.setObjectName("buttonPlaceX1")
        self.gridLayout.addWidget(self.buttonPlaceX1, 1, 0, 1, 1)
        self.lineEditX1 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditX1.sizePolicy().hasHeightForWidth())
        self.lineEditX1.setSizePolicy(sizePolicy)
        self.lineEditX1.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEditX1.setFont(font)
        self.lineEditX1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditX1.setObjectName("lineEditX1")
        self.gridLayout.addWidget(self.lineEditX1, 1, 1, 1, 1)
        self.buttonPlaceY0 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(130)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.buttonPlaceY0.sizePolicy().hasHeightForWidth())
        self.buttonPlaceY0.setSizePolicy(sizePolicy)
        self.buttonPlaceY0.setMinimumSize(QtCore.QSize(134, 44))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/ymin_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlaceY0.setIcon(icon8)
        self.buttonPlaceY0.setIconSize(QtCore.QSize(40, 40))
        self.buttonPlaceY0.setCheckable(True)
        self.buttonPlaceY0.setObjectName("buttonPlaceY0")
        self.gridLayout.addWidget(self.buttonPlaceY0, 2, 0, 1, 1)
        self.lineEditY0 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditY0.sizePolicy().hasHeightForWidth())
        self.lineEditY0.setSizePolicy(sizePolicy)
        self.lineEditY0.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEditY0.setFont(font)
        self.lineEditY0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditY0.setObjectName("lineEditY0")
        self.gridLayout.addWidget(self.lineEditY0, 2, 1, 1, 1)
        self.buttonPlaceY1 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(130)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.buttonPlaceY1.sizePolicy().hasHeightForWidth())
        self.buttonPlaceY1.setSizePolicy(sizePolicy)
        self.buttonPlaceY1.setMinimumSize(QtCore.QSize(134, 44))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/images/ymax_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlaceY1.setIcon(icon9)
        self.buttonPlaceY1.setIconSize(QtCore.QSize(40, 40))
        self.buttonPlaceY1.setCheckable(True)
        self.buttonPlaceY1.setObjectName("buttonPlaceY1")
        self.gridLayout.addWidget(self.buttonPlaceY1, 3, 0, 1, 1)
        self.lineEditY1 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditY1.sizePolicy().hasHeightForWidth())
        self.lineEditY1.setSizePolicy(sizePolicy)
        self.lineEditY1.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEditY1.setFont(font)
        self.lineEditY1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditY1.setObjectName("lineEditY1")
        self.gridLayout.addWidget(self.lineEditY1, 3, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.pageAxes)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        spacerItem2 = QtWidgets.QSpacerItem(332, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.pageAxes)
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBoxXScale = QtWidgets.QComboBox(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.comboBoxXScale.setFont(font)
        self.comboBoxXScale.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBoxXScale.setIconSize(QtCore.QSize(16, 16))
        self.comboBoxXScale.setFrame(True)
        self.comboBoxXScale.setObjectName("comboBoxXScale")
        self.comboBoxXScale.addItem("")
        self.comboBoxXScale.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxXScale, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.comboBoxYScale = QtWidgets.QComboBox(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.comboBoxYScale.setFont(font)
        self.comboBoxYScale.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBoxYScale.setObjectName("comboBoxYScale")
        self.comboBoxYScale.addItem("")
        self.comboBoxYScale.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxYScale, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.line = QtWidgets.QFrame(self.pageAxes)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.frame_8 = QtWidgets.QFrame(self.pageAxes)
        self.frame_8.setStyleSheet("QPushButton:hover{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20ff25, stop: 1 #10a613);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.buttonClearAxes = QtWidgets.QPushButton(self.frame_8)
        self.buttonClearAxes.setMinimumSize(QtCore.QSize(134, 44))
        self.buttonClearAxes.setObjectName("buttonClearAxes")
        self.horizontalLayout_6.addWidget(self.buttonClearAxes)
        spacerItem3 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.frame_8.raise_()
        self.frame_7.raise_()
        self.frame_6.raise_()
        self.frame_5.raise_()
        self.frame_4.raise_()
        self.line.raise_()
        self.stackedWidgetNavigation.addWidget(self.pageAxes)
        self.pageData = QtWidgets.QWidget()
        self.pageData.setStyleSheet("QPushButton{\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    font-weight: bold; \n"
"    font-size: 15px;\n"
"    color: white;\n"
"    min-width: 200px;\n"
"    min-height: 60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20ff25, stop: 1 #10a613);\n"
"}")
        self.pageData.setObjectName("pageData")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pageData)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_13 = QtWidgets.QFrame(self.pageData)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.frame_13)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttonNewDataSet = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNewDataSet.sizePolicy().hasHeightForWidth())
        self.buttonNewDataSet.setSizePolicy(sizePolicy)
        self.buttonNewDataSet.setMinimumSize(QtCore.QSize(204, 64))
        self.buttonNewDataSet.setObjectName("buttonNewDataSet")
        self.gridLayout_4.addWidget(self.buttonNewDataSet, 0, 0, 1, 1)
        self.buttonRemoveDataSet = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRemoveDataSet.sizePolicy().hasHeightForWidth())
        self.buttonRemoveDataSet.setSizePolicy(sizePolicy)
        self.buttonRemoveDataSet.setMinimumSize(QtCore.QSize(204, 64))
        self.buttonRemoveDataSet.setObjectName("buttonRemoveDataSet")
        self.gridLayout_4.addWidget(self.buttonRemoveDataSet, 1, 0, 1, 1)
        self.comboBoxDataSet = QtWidgets.QComboBox(self.frame_10)
        self.comboBoxDataSet.setMinimumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.comboBoxDataSet.setFont(font)
        self.comboBoxDataSet.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBoxDataSet.setObjectName("comboBoxDataSet")
        self.gridLayout_4.addWidget(self.comboBoxDataSet, 2, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame_10)
        spacerItem4 = QtWidgets.QSpacerItem(149, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout_7.addWidget(self.frame_13)
        self.line_2 = QtWidgets.QFrame(self.pageData)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.frame_14 = QtWidgets.QFrame(self.pageData)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.frame_14)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        spacerItem5 = QtWidgets.QSpacerItem(220, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_14)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_9 = QtWidgets.QFrame(self.frame_12)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.labelXCurrent = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelXCurrent.setFont(font)
        self.labelXCurrent.setObjectName("labelXCurrent")
        self.gridLayout_3.addWidget(self.labelXCurrent, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.labelYCurrent = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelYCurrent.setFont(font)
        self.labelYCurrent.setObjectName("labelYCurrent")
        self.gridLayout_3.addWidget(self.labelYCurrent, 1, 1, 1, 1)
        self.horizontalLayout_13.addWidget(self.frame_9)
        spacerItem6 = QtWidgets.QSpacerItem(241, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.verticalLayout_7.addWidget(self.frame_14)
        spacerItem7 = QtWidgets.QSpacerItem(20, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.frame_14.raise_()
        self.frame_13.raise_()
        self.line_2.raise_()
        self.stackedWidgetNavigation.addWidget(self.pageData)
        self.pageExport = QtWidgets.QWidget()
        self.pageExport.setStyleSheet("QPushButton{\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    font-weight: bold; \n"
"    font-size: 15px;\n"
"    color: white;\n"
"    min-width: 200px;\n"
"    min-height: 60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20ff25, stop: 1 #10a613);\n"
"}")
        self.pageExport.setObjectName("pageExport")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.pageExport)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_16 = QtWidgets.QFrame(self.pageExport)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_16)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.radioButtonNone = QtWidgets.QRadioButton(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.radioButtonNone.setFont(font)
        self.radioButtonNone.setObjectName("radioButtonNone")
        self.verticalLayout_8.addWidget(self.radioButtonNone)
        self.radioButtonOrdering = QtWidgets.QRadioButton(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.radioButtonOrdering.setFont(font)
        self.radioButtonOrdering.setObjectName("radioButtonOrdering")
        self.verticalLayout_8.addWidget(self.radioButtonOrdering)
        self.radioButtonInterpolation = QtWidgets.QRadioButton(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.radioButtonInterpolation.setFont(font)
        self.radioButtonInterpolation.setObjectName("radioButtonInterpolation")
        self.verticalLayout_8.addWidget(self.radioButtonInterpolation)
        self.horizontalLayout_14.addWidget(self.frame_15)
        spacerItem8 = QtWidgets.QSpacerItem(222, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.verticalLayout_10.addWidget(self.frame_16)
        self.frame_18 = QtWidgets.QFrame(self.pageExport)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_17 = QtWidgets.QFrame(self.frame_18)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.buttonExportTextFile = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonExportTextFile.sizePolicy().hasHeightForWidth())
        self.buttonExportTextFile.setSizePolicy(sizePolicy)
        self.buttonExportTextFile.setMinimumSize(QtCore.QSize(204, 64))
        self.buttonExportTextFile.setObjectName("buttonExportTextFile")
        self.verticalLayout_9.addWidget(self.buttonExportTextFile)
        self.buttonExportCsvFile = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonExportCsvFile.sizePolicy().hasHeightForWidth())
        self.buttonExportCsvFile.setSizePolicy(sizePolicy)
        self.buttonExportCsvFile.setMinimumSize(QtCore.QSize(204, 64))
        self.buttonExportCsvFile.setObjectName("buttonExportCsvFile")
        self.verticalLayout_9.addWidget(self.buttonExportCsvFile)
        self.buttonExportExcelFile = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonExportExcelFile.sizePolicy().hasHeightForWidth())
        self.buttonExportExcelFile.setSizePolicy(sizePolicy)
        self.buttonExportExcelFile.setMinimumSize(QtCore.QSize(204, 64))
        self.buttonExportExcelFile.setObjectName("buttonExportExcelFile")
        self.verticalLayout_9.addWidget(self.buttonExportExcelFile)
        self.horizontalLayout_15.addWidget(self.frame_17)
        spacerItem9 = QtWidgets.QSpacerItem(149, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.verticalLayout_10.addWidget(self.frame_18)
        spacerItem10 = QtWidgets.QSpacerItem(20, 149, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem10)
        self.frame_18.raise_()
        self.frame_16.raise_()
        self.stackedWidgetNavigation.addWidget(self.pageExport)
        self.pageInfo = QtWidgets.QWidget()
        self.pageInfo.setStyleSheet("QPushButton{\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    font-weight: bold; \n"
"    font-size: 15px;\n"
"    color: white;\n"
"    min-width: 220px;\n"
"    min-height: 60px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20ff25, stop: 1 #10a613);\n"
"}")
        self.pageInfo.setObjectName("pageInfo")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.pageInfo)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_26 = QtWidgets.QLabel(self.pageInfo)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_11.addWidget(self.label_26)
        spacerItem11 = QtWidgets.QSpacerItem(20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem11)
        self.frame_19 = QtWidgets.QFrame(self.pageInfo)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem12 = QtWidgets.QSpacerItem(165, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem12)
        self.verticalLayout_11.addWidget(self.frame_19)
        spacerItem13 = QtWidgets.QSpacerItem(20, 77, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem13)
        self.label_16 = QtWidgets.QLabel(self.pageInfo)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_11.addWidget(self.label_16)
        self.frame_19.raise_()
        self.label_26.raise_()
        self.label_16.raise_()
        self.stackedWidgetNavigation.addWidget(self.pageInfo)
        self.horizontalLayout_7.addWidget(self.stackedWidgetNavigation)
        self.frame_3 = QtWidgets.QFrame(self.frameCenter)
        self.frame_3.setStyleSheet("QGraphicsView {\n"
"    border: 2px solid #444;\n"
"    border-radius: 5px;    \n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsViewMain = QtWidgets.QGraphicsView(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewMain.sizePolicy().hasHeightForWidth())
        self.graphicsViewMain.setSizePolicy(sizePolicy)
        self.graphicsViewMain.setMinimumSize(QtCore.QSize(400, 290))
        self.graphicsViewMain.setMouseTracking(True)
        self.graphicsViewMain.setStyleSheet("")
        self.graphicsViewMain.setObjectName("graphicsViewMain")
        self.verticalLayout.addWidget(self.graphicsViewMain)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 3px solid white;\n"
"    background: white;\n"
"    height: 12px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ccd5db, stop: 1 #34617e);\n"
"    border: 1px solid #aaa;\n"
"    height: 12px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #555);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -3px;\n"
"margin-bottom: -3px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover{\n"
"    background: QLinearGradient(x1:0, y1:0, x2:1, y2:1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(86, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.sliderZoom = QtWidgets.QSlider(self.frame_2)
        self.sliderZoom.setMaximum(100)
        self.sliderZoom.setProperty("value", 50)
        self.sliderZoom.setOrientation(QtCore.Qt.Horizontal)
        self.sliderZoom.setObjectName("sliderZoom")
        self.horizontalLayout_3.addWidget(self.sliderZoom)
        self.labelZoomFactor = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelZoomFactor.setFont(font)
        self.labelZoomFactor.setObjectName("labelZoomFactor")
        self.horizontalLayout_3.addWidget(self.labelZoomFactor)
        spacerItem15 = QtWidgets.QSpacerItem(86, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.frame_3.raise_()
        self.stackedWidgetNavigation.raise_()
        self.verticalLayout_5.addWidget(self.frameCenter)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.stackedWidgetBottom = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidgetBottom.setStyleSheet("QStackedWidget {\n"
"font: 75 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    font-weight: bold; \n"
"    font-size: 15px;\n"
"    color: white;\n"
"    min-width: 100px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20ff25, stop: 1 #10a613);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidgetBottom.setObjectName("stackedWidgetBottom")
        self.pageBottomBack = QtWidgets.QWidget()
        self.pageBottomBack.setObjectName("pageBottomBack")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.pageBottomBack)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem16 = QtWidgets.QSpacerItem(751, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.buttonBack = QtWidgets.QPushButton(self.pageBottomBack)
        self.buttonBack.setMinimumSize(QtCore.QSize(104, 44))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/images/back_quadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(icon10)
        self.buttonBack.setIconSize(QtCore.QSize(40, 40))
        self.buttonBack.setObjectName("buttonBack")
        self.horizontalLayout_8.addWidget(self.buttonBack)
        self.stackedWidgetBottom.addWidget(self.pageBottomBack)
        self.pageBottomMenu = QtWidgets.QWidget()
        self.pageBottomMenu.setObjectName("pageBottomMenu")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.pageBottomMenu)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem17 = QtWidgets.QSpacerItem(857, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem17)
        self.stackedWidgetBottom.addWidget(self.pageBottomMenu)
        self.horizontalLayout_9.addWidget(self.stackedWidgetBottom)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame.raise_()
        self.frameCenter.raise_()
        self.stackedWidgetHead.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidgetHead.setCurrentIndex(5)
        self.stackedWidgetNavigation.setCurrentIndex(5)
        self.stackedWidgetBottom.setCurrentIndex(0)
        self.buttonQuit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DiagramDigitizer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">DiagramDigitizer</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Project</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Axes</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Data</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Export</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Info</span></p></body></html>"))
        self.buttonProject.setText(_translate("MainWindow", "Project   "))
        self.buttonAxes.setText(_translate("MainWindow", "Axes      "))
        self.buttonData.setText(_translate("MainWindow", "Data       "))
        self.buttonExport.setText(_translate("MainWindow", "Export   "))
        self.buttonInfo.setText(_translate("MainWindow", "Info       "))
        self.buttonQuit.setText(_translate("MainWindow", "Quit       "))
        self.buttonNewProject.setText(_translate("MainWindow", "New Project"))
        self.buttonOpenProject.setText(_translate("MainWindow", "Open Project"))
        self.buttonSaveProject.setText(_translate("MainWindow", "Save Project"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Limits</span></p></body></html>"))
        self.buttonPlaceX0.setText(_translate("MainWindow", "Place x0"))
        self.buttonPlaceX1.setText(_translate("MainWindow", "Place x1"))
        self.buttonPlaceY0.setText(_translate("MainWindow", "Place y0"))
        self.buttonPlaceY1.setText(_translate("MainWindow", "Place y1"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Scales</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "X Scale"))
        self.comboBoxXScale.setItemText(0, _translate("MainWindow", "linear"))
        self.comboBoxXScale.setItemText(1, _translate("MainWindow", "logarithmic"))
        self.label_7.setText(_translate("MainWindow", "Y Scale"))
        self.comboBoxYScale.setItemText(0, _translate("MainWindow", "linear"))
        self.comboBoxYScale.setItemText(1, _translate("MainWindow", "logarithmic"))
        self.buttonClearAxes.setText(_translate("MainWindow", "Clear axes"))
        self.buttonNewDataSet.setText(_translate("MainWindow", "New data set"))
        self.buttonRemoveDataSet.setText(_translate("MainWindow", "Remove data set"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Current Position</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "x ="))
        self.labelXCurrent.setText(_translate("MainWindow", "xxx         "))
        self.label_10.setText(_translate("MainWindow", "y = "))
        self.labelYCurrent.setText(_translate("MainWindow", "xxx         "))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Data Processing</span></p></body></html>"))
        self.radioButtonNone.setText(_translate("MainWindow", "None"))
        self.radioButtonOrdering.setText(_translate("MainWindow", "Sorting"))
        self.radioButtonInterpolation.setText(_translate("MainWindow", "Interpolation"))
        self.buttonExportTextFile.setText(_translate("MainWindow", "Export to text file"))
        self.buttonExportCsvFile.setText(_translate("MainWindow", "Export to csv file"))
        self.buttonExportExcelFile.setText(_translate("MainWindow", "Export to Excel file"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">DiagramDigitizer is an easy-to-use tool </span></p><p><span style=\" font-size:14pt; font-style:italic;\">to extract numerical data from diagrams</span></p><p><span style=\" font-size:14pt; font-style:italic;\">and export them for further use.</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Copyright (C) 2016 Michael Fischer</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Zoom:  </span></p></body></html>"))
        self.labelZoomFactor.setText(_translate("MainWindow", "xxx      "))
        self.buttonBack.setText(_translate("MainWindow", "Back"))

from . import resources_rc
