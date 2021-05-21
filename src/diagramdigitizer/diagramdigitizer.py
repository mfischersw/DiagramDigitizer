# This file is part of DiagramDigitizer.

"""
.. module:: diagramdigitizer
   :synopsis: Graphical user interace module.

.. moduleauthor:: Michael Fischer
"""

# Imports
from functools import partial
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

from . import ui
from . import graphscene
from . import export
from . import utils


def run():
    """GUI main loop.
    """
    app = QtWidgets.QApplication(sys.argv)

    mainwindow = DDMainWindow()
    mainwindow.showMaximized()

    sys.exit(app.exec_())


class DDMainWindow(QtWidgets.QMainWindow):
    """GUI: Main window.
    """

    def __init__(self, *args):

        QtWidgets.QMainWindow.__init__(self, *args)

        self.ui = ui.mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # Activate stylesheet use for centralwidget
        self.ui.centralwidget.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.setWindowTitle("DiagramDigitizer")

        self.initGraphicsView()
        self.initAxesScaleTypes()
        self.initRadioButtonsExport()
        self.initZoom()

        # Organize axis buttons / edits
        self.__dictAxisButtonsOPERATION_MODES = {
            "X0": (self.ui.buttonPlaceX0, self.__graphicsScene.OPERATION_MODES.OP_AXIS_X0),
            "X1": (self.ui.buttonPlaceX1, self.__graphicsScene.OPERATION_MODES.OP_AXIS_X1),
            "Y0": (self.ui.buttonPlaceY0, self.__graphicsScene.OPERATION_MODES.OP_AXIS_Y0),
            "Y1": (self.ui.buttonPlaceY1, self.__graphicsScene.OPERATION_MODES.OP_AXIS_Y1)}

        self.__dictAxisEditsOPERATION_MODES = {
            "X0": (self.ui.lineEditX0, self.__graphicsScene.OPERATION_MODES.OP_AXIS_X0),
            "X1": (self.ui.lineEditX1, self.__graphicsScene.OPERATION_MODES.OP_AXIS_X1),
            "Y0": (self.ui.lineEditY0, self.__graphicsScene.OPERATION_MODES.OP_AXIS_Y0),
            "Y1": (self.ui.lineEditY1, self.__graphicsScene.OPERATION_MODES.OP_AXIS_Y1)}

        # Uncheck all axes buttons
        self.uncheckAxisButtons()

        # Init data set count
        self.__countDataSet = 0

        # Menu page at start
        self.showPageMenu()

        # Signal-slot connects
        self.createConnects()

    def createConnects(self):

        # Navigation
        self.ui.buttonBack.clicked.connect(self.showPageMenu)
        self.ui.buttonProject.clicked.connect(self.showPageProject)
        self.ui.buttonAxes.clicked.connect(self.showPageAxes)
        self.ui.buttonData.clicked.connect(self.showPageData)
        self.ui.buttonExport.clicked.connect(self.showPageExport)
        self.ui.buttonInfo.clicked.connect(self.showPageInfo)
        self.ui.buttonQuit.clicked.connect(self.quitProgram)

        # Project
        self.ui.buttonNewProject.clicked.connect(self.newProject)
        self.ui.buttonOpenProject.clicked.connect(self.loadProject)
        self.ui.buttonSaveProject.clicked.connect(self.saveProject)

        # Axes
        self.ui.buttonClearAxes.clicked.connect(self.clearAxes)

        self.ui.comboBoxXScale.currentIndexChanged.connect(self.setAxisXScale)
        self.ui.comboBoxYScale.currentIndexChanged.connect(self.setAxisYScale)

        for axisFlag in self.__dictAxisButtonsOPERATION_MODES.keys():
            axEdit = self.__dictAxisEditsOPERATION_MODES[axisFlag][0]
            axEdit.textEdited.connect(self.readAxisRealCoords)

            axButton = self.__dictAxisButtonsOPERATION_MODES[axisFlag][0]
            axButton.clicked.connect(partial(self.handleAxisButton, axisFlag))

        # Data
        self.ui.buttonNewDataSet.clicked.connect(self.newDataSet)
        self.ui.buttonRemoveDataSet.clicked.connect(self.removeDataSet)
        self.ui.comboBoxDataSet.currentIndexChanged.connect(self.actDataSet)

        # Export
        self.ui.buttonExportTextFile.clicked.connect(partial(self.exportToFile, "text"))
        self.ui.buttonExportCsvFile.clicked.connect(partial(self.exportToFile, "csv"))
        self.ui.buttonExportExcelFile.clicked.connect(partial(self.exportToFile, "excel"))

        # Mouse
        self.__graphicsScene.mouseMovedSignal.connect(self.updateMouseCoords)

        # Zoom
        self.ui.sliderZoom.valueChanged.connect(self.zoomGraphicsView)

    def initAxesScaleTypes(self):

        # Init axes scaletypes to linear
        self.ui.comboBoxXScale.setCurrentIndex(0)
        self.ui.comboBoxYScale.setCurrentIndex(0)

    def initRadioButtonsExport(self):

        self.ui.radioButtonNone.setChecked(True)
        self.ui.radioButtonOrdering.setChecked(False)
        self.ui.radioButtonInterpolation.setChecked(False)

    def initGraphicsView(self):

        self.__graphicsView = self.ui.graphicsViewMain
        self.__graphicsScene = graphscene.DDGraphicsScene()
        self.__graphicsView.setScene(self.__graphicsScene)
        self.__graphicsView.show()
        self.__graphicsView.setEnabled(True)

    def initZoom(self):

        self.ui.labelZoomFactor.setText(str(100) + " %")

    @QtCore.pyqtSlot()
    def showPageMenu(self):

        self.ui.stackedWidgetNavigation.setCurrentIndex(self.ui.stackedWidgetNavigation.indexOf(self.ui.pageMenu))
        self.ui.stackedWidgetHead.setCurrentIndex(self.ui.stackedWidgetHead.indexOf(self.ui.pageHeadMenu))
        self.ui.stackedWidgetBottom.setCurrentIndex(self.ui.stackedWidgetBottom.indexOf(self.ui.pageBottomMenu))

        self.__graphicsScene.setOperationMode(self.__graphicsScene.OPERATION_MODES.OP_WATCH)

    @QtCore.pyqtSlot()
    def showPageProject(self):

        self.ui.stackedWidgetNavigation.setCurrentIndex(self.ui.stackedWidgetNavigation.indexOf(self.ui.pageProject))
        self.ui.stackedWidgetHead.setCurrentIndex(self.ui.stackedWidgetHead.indexOf(self.ui.pageHeadProject))
        self.ui.stackedWidgetBottom.setCurrentIndex(self.ui.stackedWidgetBottom.indexOf(self.ui.pageBottomBack))

        self.__graphicsScene.setOperationMode(self.__graphicsScene.OPERATION_MODES.OP_WATCH)

    @QtCore.pyqtSlot()
    def showPageAxes(self):

        self.ui.stackedWidgetNavigation.setCurrentIndex(self.ui.stackedWidgetNavigation.indexOf(self.ui.pageAxes))
        self.ui.stackedWidgetHead.setCurrentIndex(self.ui.stackedWidgetHead.indexOf(self.ui.pageHeadAxes))
        self.ui.stackedWidgetBottom.setCurrentIndex(self.ui.stackedWidgetBottom.indexOf(self.ui.pageBottomBack))

        self.uncheckAxisButtons()

    @QtCore.pyqtSlot()
    def showPageData(self):

        self.ui.stackedWidgetNavigation.setCurrentIndex(self.ui.stackedWidgetNavigation.indexOf(self.ui.pageData))
        self.ui.stackedWidgetHead.setCurrentIndex(self.ui.stackedWidgetHead.indexOf(self.ui.pageHeadData))
        self.ui.stackedWidgetBottom.setCurrentIndex(self.ui.stackedWidgetBottom.indexOf(self.ui.pageBottomBack))

        self.__graphicsScene.setOperationMode(self.__graphicsScene.OPERATION_MODES.OP_DATA)

    @QtCore.pyqtSlot()
    def showPageInfo(self):

        self.ui.stackedWidgetNavigation.setCurrentIndex(self.ui.stackedWidgetNavigation.indexOf(self.ui.pageInfo))
        self.ui.stackedWidgetHead.setCurrentIndex(self.ui.stackedWidgetHead.indexOf(self.ui.pageHeadInfo))
        self.ui.stackedWidgetBottom.setCurrentIndex(self.ui.stackedWidgetBottom.indexOf(self.ui.pageBottomBack))

        self.__graphicsScene.setOperationMode(self.__graphicsScene.OPERATION_MODES.OP_WATCH)

    @QtCore.pyqtSlot()
    def showPageExport(self):

        self.ui.stackedWidgetNavigation.setCurrentIndex(self.ui.stackedWidgetNavigation.indexOf(self.ui.pageExport))
        self.ui.stackedWidgetHead.setCurrentIndex(self.ui.stackedWidgetHead.indexOf(self.ui.pageHeadExport))
        self.ui.stackedWidgetBottom.setCurrentIndex(self.ui.stackedWidgetBottom.indexOf(self.ui.pageBottomBack))

        self.__graphicsScene.setOperationMode(self.__graphicsScene.OPERATION_MODES.OP_WATCH)

    @QtCore.pyqtSlot()
    def quitProgram(self):
        pass

    @QtCore.pyqtSlot()
    def newProject(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open an image file to be digitized',
                                                         filter='Images (*.png *.jpg *.jpeg *.bmp)')

        if (fileName and (len(fileName[0]) > 0)):
            try:

                self.__graphicsScene.newScene(fileName[0])
                self.updateAxesLineEditsFromScene()
                self.updateAxesScaleTypesFromScene()
                self.updateDataSetListFromScene()
                self.initRadioButtonsExport()

            except:
                pass

    @QtCore.pyqtSlot()
    def saveProject(self):

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, caption='Save project to file', filter='*.mydig')
        if (fileName and (len(fileName[0]) > 0)):
            try:
                self.__graphicsScene.saveScene(fileName[0])
            except:
                pass

    @QtCore.pyqtSlot()
    def loadProject(self):

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, caption='Open a project from file', filter='*.mydig')
        if (fileName and (len(fileName[0]) > 0)):
            try:

                self.__graphicsScene.loadScene(fileName[0])
                self.updateAxesLineEditsFromScene()
                self.updateAxesScaleTypesFromScene()
                self.updateDataSetListFromScene()
                self.initRadioButtonsExport()

            except:
                pass

    def updateAxesLineEditsFromScene(self):

        x0Real = self.__graphicsScene.get_x0Real()
        x1Real = self.__graphicsScene.get_x1Real()
        y0Real = self.__graphicsScene.get_y0Real()
        y1Real = self.__graphicsScene.get_y1Real()

        if (x0Real is None):
            self.ui.lineEditX0.clear()
        else:
            self.ui.lineEditX0.setText(str(x0Real))

        if (x1Real is None):
            self.ui.lineEditX1.clear()
        else:
            self.ui.lineEditX1.setText(str(x1Real))

        if (y0Real is None):
            self.ui.lineEditY0.clear()
        else:
            self.ui.lineEditY0.setText(str(y0Real))

        if (y1Real is None):
            self.ui.lineEditY1.clear()
        else:
            self.ui.lineEditY1.setText(str(y1Real))

    def updateAxesScaleTypesFromScene(self):

        scaleX = self.__graphicsScene.getScaleX()
        scaleY = self.__graphicsScene.getScaleY()

        if (scaleX == self.__graphicsScene.SCALETYPE_AXES.AXIS_LIN_X):
            self.ui.comboBoxXScale.setCurrentIndex(0)
        else:
            self.ui.comboBoxXScale.setCurrentIndex(1)

        if (scaleY == self.__graphicsScene.SCALETYPE_AXES.AXIS_LIN_Y):
            self.ui.comboBoxYScale.setCurrentIndex(0)
        else:
            self.ui.comboBoxYScale.setCurrentIndex(1)

    def updateDataSetListFromScene(self):

        self.__countDataSet = 0
        self.ui.comboBoxDataSet.clear()

        nameListh = self.__graphicsScene.getNamesLinesOfDataPoints()
        nameList = utils.sortNameListWithTag(nameListh)

        for ind in range(len(nameList)):
            self.ui.comboBoxDataSet.addItem(nameList[ind])

        if (len(nameList) > 0):
            lastName = nameList[-1]
            self.__countDataSet = int(lastName[utils.DATASETTAGLEN:])

            ind = 0
            self.ui.comboBoxDataSet.setCurrentIndex(ind)
            self.actDataSet()

    @QtCore.pyqtSlot()
    def setAxisXScale(self):

        if (self.ui.comboBoxXScale.currentIndex() == 0):  # linear
            self.__graphicsScene.setScaleX(self.__graphicsScene.SCALETYPE_AXES.AXIS_LIN_X)
        else:  # log
            self.__graphicsScene.setScaleX(self.__graphicsScene.SCALETYPE_AXES.AXIS_LOG_X)

    @QtCore.pyqtSlot()
    def setAxisYScale(self):

        if (self.ui.comboBoxYScale.currentIndex() == 0):  # linear
            self.__graphicsScene.setScaleY(self.__graphicsScene.SCALETYPE_AXES.AXIS_LIN_Y)
        else:  # log
            self.__graphicsScene.setScaleY(self.__graphicsScene.SCALETYPE_AXES.AXIS_LOG_Y)

    @QtCore.pyqtSlot()
    def readAxisRealCoords(self):

        for axisFlag in self.__dictAxisButtonsOPERATION_MODES.keys():

            axEdit = self.__dictAxisEditsOPERATION_MODES[axisFlag][0]

            try:
                val = float(axEdit.text())

                if (axisFlag == "X0"):
                    self.__graphicsScene.set_x0Real(val)
                elif (axisFlag == "X1"):
                    self.__graphicsScene.set_x1Real(val)
                elif (axisFlag == "Y0"):
                    self.__graphicsScene.set_y0Real(val)
                elif (axisFlag == "Y1"):
                    self.__graphicsScene.set_y1Real(val)

            except:
                pass

    def uncheckAxisButtons(self):

        for axisFlag in self.__dictAxisButtonsOPERATION_MODES.keys():
            axButton = self.__dictAxisButtonsOPERATION_MODES[axisFlag][0]
            axButton.setChecked(False)

        self.__graphicsScene.setOperationMode(self.__graphicsScene.OPERATION_MODES.OP_WATCH)

    @QtCore.pyqtSlot()
    def handleAxisButton(self, axisFlag):

        axButton = self.__dictAxisButtonsOPERATION_MODES[axisFlag][0]
        axOpMode = self.__dictAxisButtonsOPERATION_MODES[axisFlag][1]

        state = axButton.isChecked()
        self.uncheckAxisButtons()

        if (state):
            axButton.setChecked(True)
            self.__graphicsScene.setOperationMode(axOpMode)

    @QtCore.pyqtSlot()
    def clearAxes(self):

        self.__graphicsScene.removeAllAxisPoints()
        self.uncheckAxisButtons()

        for axisFlag in self.__dictAxisButtonsOPERATION_MODES.keys():
            axEdit = self.__dictAxisEditsOPERATION_MODES[axisFlag][0]
            axEdit.clear()

    @QtCore.pyqtSlot()
    def actDataSet(self):

        ind = self.ui.comboBoxDataSet.currentIndex()
        singleLineName = self.ui.comboBoxDataSet.itemText(ind)

        self.__graphicsScene.set_nameCurrentSingleLine(singleLineName)

        self.__graphicsScene.showLineOfDataPoints(singleLineName)

    @QtCore.pyqtSlot()
    def newDataSet(self):

        if (self.__graphicsScene.getBackgroundStatus()):
            self.__countDataSet = self.__countDataSet + 1
            singleLineName = utils.DATASETTAG + str(self.__countDataSet)
            self.ui.comboBoxDataSet.addItem(singleLineName)
            self.ui.comboBoxDataSet.setCurrentIndex(self.ui.comboBoxDataSet.findText(singleLineName))

            self.__graphicsScene.newLineOfDataPoints(singleLineName)

            self.__graphicsScene.showLineOfDataPoints(singleLineName)

    @QtCore.pyqtSlot()
    def removeDataSet(self):

        ind = self.ui.comboBoxDataSet.currentIndex()
        singleLineName = self.ui.comboBoxDataSet.itemText(ind)

        self.ui.comboBoxDataSet.removeItem(ind)

        self.__graphicsScene.removeLineOfDataPoints(singleLineName)

        self.actDataSet()

    def determineProcType(self):

        if (self.ui.radioButtonNone.isChecked()):
            return export.PROCESSING_TYPE_INONE
        elif (self.ui.radioButtonOrdering.isChecked()):
            return export.PROCESSING_TYPE_ISORT
        elif (self.ui.radioButtonInterpolation.isChecked()):
            return export.PROCESSING_TYPE_INTERP

    @QtCore.pyqtSlot()
    def exportToFile(self, fileFlag):

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, caption='Export data to file',
                                                         filter=export.FILE_FILTERS[fileFlag])
        if fileName:
            try:
                dictRealCoords = self.__graphicsScene.determineDataPointsRealCoords()
                export.exportData_to_fileGen(fileName[0], dictRealCoords, fileFlag, self.determineProcType())
            except:
                pass

    @QtCore.pyqtSlot(str, str)
    def updateMouseCoords(self, xStr, yStr):

        self.ui.labelXCurrent.setText(xStr)
        self.ui.labelYCurrent.setText(yStr)

    def myGraphicsViewEnterEvent(self, event):
        QtWidgets.QGraphicsView.enterEvent(self, event)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CrossCursor)

    def myGraphicsViewLeaveEvent(self, event):
        QtWidgets.QGraphicsView.leaveEvent(self, event)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)

    @QtCore.pyqtSlot()
    def zoomGraphicsView(self):

        zoomFac = self.calcZoomFactor()

        self.ui.labelZoomFactor.setText(str(int(zoomFac * 100)) + " %")
        matrix = QtGui.QTransform()
        matrix.scale(zoomFac, zoomFac)
        self.__graphicsView.setTransform(matrix)

    def calcZoomFactor(self):

        slidPos = self.ui.sliderZoom.value()
        slidCen = 50

        zmin = 0.25
        zcen = 1.0
        zmax = 4.0

        if (slidPos == slidCen):
            zoomFac = 1.0
        elif (slidPos < slidCen):
            zoomFac = zmin + slidPos * (zcen - zmin) / slidCen
        elif (slidPos > slidCen):
            zoomFac = 1.0 + (slidPos - slidCen) * (zmax - zcen) / slidCen

        return zoomFac
