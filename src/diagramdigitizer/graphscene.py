# This file is part of DiagramDigitizer.

"""
.. module:: graphscene
   :synopsis: Graphics scene for diagram digitization module.

.. moduleauthor:: Michael Fischer
"""

# Imports
import numpy
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets


class DDGraphicsScene(QtWidgets.QGraphicsScene):
    """ Graphics scene

        Class attributes:
            * Operation modes (watch mode, axes add modes, axes delete modes, data mode)
            * Presented axes (x axis, y axis)
            * Axes scale types (linear/logarithmic)    
            * Basic graphical items (data points, axes points, axes lines)

        Getters { line names list, axes limits, axes scale types }

        Setters { operation mode, current line, axes limits, axes scale types }           

        Basic scene setup { new, save, load }

        Data { line: new, remove, show; point: add, remove }
    
        Axes { points: add, remove; lines: update }

        Mouse { press, move }

        Calculation { coordinates }
    """

    class OPERATION_MODES:
        (OP_WATCH, OP_AXIS_X0, OP_DEL_AXIS_X0, OP_AXIS_X1, OP_DEL_AXIS_X1,
         OP_AXIS_Y0, OP_DEL_AXIS_Y0, OP_AXIS_Y1, OP_DEL_AXIS_Y1, OP_DATA) = range(10)

    class PRESENTED_AXES:
        (AXIS_X, AXIS_Y) = range(2)

    class SCALETYPE_AXES:
        (AXIS_LIN_X, AXIS_LOG_X, AXIS_LIN_Y, AXIS_LOG_Y) = range(4)

    # Graphical items
    PEN_WIDTH = 2
    PEN_AXIS = QtGui.QPen(QtCore.Qt.blue, PEN_WIDTH, QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.MiterJoin)
    PEN_POINT = QtGui.QPen(QtCore.Qt.red, PEN_WIDTH, QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.BevelJoin)

    BASITEM_POINT_CONF = {"x": -5.0, "y": -5.0, "d": 10.0}  # for circle
    BASITEM_AXES_CONF = {"basis": 16, "height": 20}  # for triangle

    BASITEM_POINT = QtCore.QRectF(BASITEM_POINT_CONF["x"], BASITEM_POINT_CONF["y"], BASITEM_POINT_CONF["d"],
                                  BASITEM_POINT_CONF["d"])
    BASITEM_X0 = QtGui.QPolygonF([QtCore.QPoint(BASITEM_AXES_CONF["height"], -BASITEM_AXES_CONF["basis"] / 2.0),
                                 QtCore.QPoint(BASITEM_AXES_CONF["height"], BASITEM_AXES_CONF["basis"] / 2.0),
                                 QtCore.QPoint(PEN_WIDTH, 0)])
    BASITEM_X1 = QtGui.QPolygonF([QtCore.QPoint(-BASITEM_AXES_CONF["height"], -BASITEM_AXES_CONF["basis"] / 2.0),
                                 QtCore.QPoint(-BASITEM_AXES_CONF["height"], BASITEM_AXES_CONF["basis"] / 2.0),
                                 QtCore.QPoint(-PEN_WIDTH, 0)])
    BASITEM_Y0 = QtGui.QPolygonF([QtCore.QPoint(-BASITEM_AXES_CONF["basis"] / 2.0, -BASITEM_AXES_CONF["height"]),
                                 QtCore.QPoint(BASITEM_AXES_CONF["basis"] / 2.0, -BASITEM_AXES_CONF["height"]),
                                 QtCore.QPoint(0, -PEN_WIDTH)])
    BASITEM_Y1 = QtGui.QPolygonF([QtCore.QPoint(-BASITEM_AXES_CONF["basis"] / 2.0, BASITEM_AXES_CONF["height"]),
                                 QtCore.QPoint(BASITEM_AXES_CONF["basis"] / 2.0, BASITEM_AXES_CONF["height"]),
                                 QtCore.QPoint(0, PEN_WIDTH)])

    BASITEMS_AXES = {OPERATION_MODES.OP_AXIS_X0: BASITEM_X0, OPERATION_MODES.OP_AXIS_X1: BASITEM_X1,
                     OPERATION_MODES.OP_AXIS_Y0: BASITEM_Y0, OPERATION_MODES.OP_AXIS_Y1: BASITEM_Y1}
    BASITEMS_DEL_AXES = {OPERATION_MODES.OP_DEL_AXIS_X0, OPERATION_MODES.OP_DEL_AXIS_X1,
                         OPERATION_MODES.OP_DEL_AXIS_Y0, OPERATION_MODES.OP_DEL_AXIS_Y1}

    # Signal: Mouse moved
    mouseMovedSignal = QtCore.pyqtSignal(str, str)

    def __init__(self, *args):

        QtWidgets.QGraphicsScene.__init__(self, *args)

        # Initialize scene
        self.resetScene()

    def resetScene(self):

        self.clear()

        # Background data
        self.__background = None
        self.__backgroundFilepath = None

        # Re-init: watch mode
        self.__operationMode = DDGraphicsScene.OPERATION_MODES.OP_WATCH

        # Current line
        self.__nameCurrentSingleLine = None

        # Graphical items data
        self.__dictLinesOfDataPoints = {}
        self.__dictAxesPointItems = {}
        self.__dictAxesItems = {}

        # Axes limits
        self.__x0Real = None
        self.__x1Real = None
        self.__y0Real = None
        self.__y1Real = None

        # Axes scale types
        self.__scaleX = DDGraphicsScene.SCALETYPE_AXES.AXIS_LIN_X
        self.__scaleY = DDGraphicsScene.SCALETYPE_AXES.AXIS_LIN_Y

    def getBackgroundStatus(self):

        return not (self.__background is None)

    def setOperationMode(self, mode):

        self.__operationMode = mode

    def getNamesLinesOfDataPoints(self):

        nameList = []

        for absName in self.__dictLinesOfDataPoints.keys():
            nameList.append(absName)

        return nameList

    def set_nameCurrentSingleLine(self, nameSingleLine):

        self.__nameCurrentSingleLine = nameSingleLine

    def get_x0Real(self):

        return self.__x0Real

    def set_x0Real(self, x0):

        self.__x0Real = x0

    def get_x1Real(self):

        return self.__x1Real

    def set_x1Real(self, x1):

        self.__x1Real = x1

    def get_y0Real(self):

        return self.__y0Real

    def set_y0Real(self, y0):

        self.__y0Real = y0

    def get_y1Real(self):

        return self.__y1Real

    def set_y1Real(self, y1):

        self.__y1Real = y1

    def getScaleX(self):

        return self.__scaleX

    def setScaleX(self, scaleType):

        self.__scaleX = scaleType

    def getScaleY(self):

        return self.__scaleY

    def setScaleY(self, scaleType):

        self.__scaleY = scaleType

    def newScene(self, filename):

        # Reset everything
        self.resetScene()

        # Setup background from file
        self.setupBackgroundFromFile(filename)

    def saveScene(self, filename):

        dumpDict = {}

        # Image file name
        dumpDict["Image"] = self.__backgroundFilepath

        # Axes        
        dumpDict["x0"] = self.__x0Real
        dumpDict["x1"] = self.__x1Real
        dumpDict["y0"] = self.__y0Real
        dumpDict["y1"] = self.__y1Real
        dumpDict["scaleX"] = self.__scaleX
        dumpDict["scaleY"] = self.__scaleY

        # Transform axes point items scene coordinates
        dumpDict["AxesPointItemsCoords"] = self.trafo_itemsToCoords_axesPoints()

        # Transform data point items scene coordinates
        dumpDict["LinesOfDataPointsCoords"] = self.trafo_itemsToCoords_dataPoints()

        try:
            pickle.dump(dumpDict, open(filename, "wb"))
        except OSError as e:
            print("OS ERROR: ", e.errno)

    def loadScene(self, filename):

        try:

            # Reset everything
            self.resetScene()

            dumpDict = pickle.load(open(filename, "rb"))

            # Image file name
            self.setupBackgroundFromFile(dumpDict["Image"])

            # Axes   
            self.__x0Real = dumpDict["x0"]
            self.__x1Real = dumpDict["x1"]
            self.__y0Real = dumpDict["y0"]
            self.__y1Real = dumpDict["y1"]
            self.__scaleX = dumpDict["scaleX"]
            self.__scaleY = dumpDict["scaleY"]

            # Transform axes point scene coordinates to items 
            self.trafo_coordsToItems_axesPoints(dumpDict["AxesPointItemsCoords"])

            self.updateAxis()

            # Transform data point scene coordinates to items 
            self.trafo_coordsToItems_dataPoints(dumpDict["LinesOfDataPointsCoords"])

        except OSError as e:
            print("OS ERROR: ", e.errno)

    def setupBackgroundFromFile(self, filepath):

        self.__backgroundFilepath = filepath
        pixmap = QtGui.QPixmap(filepath)
        self.__background = self.addPixmap(pixmap)

    def trafo_itemsToCoords_axesPoints(self):

        dictAxesPointItems_coords = {}

        for opMode in self.__dictAxesPointItems.keys():
            item = self.__dictAxesPointItems[opMode]
            itemPos = item.scenePos()
            (x, y) = (itemPos.x(), itemPos.y())
            dictAxesPointItems_coords[opMode] = (x, y)

        return dictAxesPointItems_coords

    def trafo_coordsToItems_axesPoints(self, dictAxesPointItems_coords):

        self.__dictAxesPointItems = {}

        for opMode in dictAxesPointItems_coords.keys():
            (x, y) = dictAxesPointItems_coords[opMode]
            item = self.addPolygon(DDGraphicsScene.BASITEMS_AXES[opMode], DDGraphicsScene.PEN_AXIS)
            item.setPos(QtCore.QPointF(x, y))
            self.__dictAxesPointItems[opMode] = item

    def trafo_itemsToCoords_dataPoints(self):

        dictLinesOfDataPoints_coords = {}

        for absName in self.__dictLinesOfDataPoints.keys():
            dictLinesOfDataPoints_coords[absName] = []
            for item in self.__dictLinesOfDataPoints[absName]:
                itemPos = item.scenePos()
                (x, y) = (itemPos.x(), itemPos.y())
                dictLinesOfDataPoints_coords[absName].append((x, y))

        return dictLinesOfDataPoints_coords

    def trafo_coordsToItems_dataPoints(self, dictLinesOfDataPoints_coords):

        self.__dictLinesOfDataPoints = {}

        for absName in dictLinesOfDataPoints_coords.keys():

            self.__dictLinesOfDataPoints[absName] = []

            for (x, y) in dictLinesOfDataPoints_coords[absName]:
                item = self.addEllipse(DDGraphicsScene.BASITEM_POINT, DDGraphicsScene.PEN_POINT)
                item.setPos(QtCore.QPointF(x, y))
                self.__dictLinesOfDataPoints[absName].append(item)

    def newLineOfDataPoints(self, nameSingleLine):

        self.__nameCurrentSingleLine = nameSingleLine

        # Empty list
        self.__dictLinesOfDataPoints[self.__nameCurrentSingleLine] = []

    def removeLineOfDataPoints(self, nameSingleLine):

        if ((len(nameSingleLine) > 0) and (nameSingleLine in self.__dictLinesOfDataPoints.keys())):

            # Remove all corresponding items from scene
            for item in self.__dictLinesOfDataPoints[nameSingleLine]:
                self.removeItem(item)

            self.__dictLinesOfDataPoints.pop(nameSingleLine)
            self.__nameCurrentSingleLine = None

    def showLineOfDataPoints(self, nameSingleLine):

        if ((len(nameSingleLine) > 0) and (nameSingleLine in self.__dictLinesOfDataPoints.keys())):

            # hide all others
            for absName in self.__dictLinesOfDataPoints.keys():
                for item in self.__dictLinesOfDataPoints[absName]:
                    item.setVisible(False)

            # show respective line
            for item in self.__dictLinesOfDataPoints[nameSingleLine]:
                item.setVisible(True)

    def showAllLinesOfDataPoints(self):

        for absName in self.__dictLinesOfDataPoints.keys():
            for item in self.__dictLinesOfDataPoints[absName]:
                item.setVisible(True)

    def addDataPoint(self, mousePos):

        if (self.__operationMode == DDGraphicsScene.OPERATION_MODES.OP_DATA and not (
                self.__nameCurrentSingleLine is None)):
            item = self.addEllipse(DDGraphicsScene.BASITEM_POINT, DDGraphicsScene.PEN_POINT)
            item.setPos(mousePos)
            self.__dictLinesOfDataPoints[self.__nameCurrentSingleLine].append(item)

    def removeDataPoint(self, item):

        if (self.__operationMode == DDGraphicsScene.OPERATION_MODES.OP_DATA and not (
                self.__nameCurrentSingleLine is None)):

            if (item in self.__dictLinesOfDataPoints[self.__nameCurrentSingleLine]):
                self.removeItem(item)
                self.__dictLinesOfDataPoints[self.__nameCurrentSingleLine].remove(item)

    def addAxisPoint(self, mousePos):

        if (self.__operationMode in DDGraphicsScene.BASITEMS_AXES.keys()):

            # remove old item if present
            if (self.__operationMode in self.__dictAxesPointItems.keys()):
                item = self.__dictAxesPointItems[self.__operationMode]
                self.removeItem(item)
                self.__dictAxesPointItems.pop(self.__operationMode)

            # new item
            item = self.addPolygon(DDGraphicsScene.BASITEMS_AXES[self.__operationMode],
                                   DDGraphicsScene.PEN_AXIS)
            item.setPos(mousePos)
            self.__dictAxesPointItems[self.__operationMode] = item
            self.__operationMode = self.__operationMode + 1  # internal delete mode
            self.updateAxis()

    def removeAxisPoint(self, item):

        if (self.__operationMode in DDGraphicsScene.BASITEMS_DEL_AXES and (
                self.__operationMode - 1) in self.__dictAxesPointItems.keys()):

            if (item == self.__dictAxesPointItems[self.__operationMode - 1]):
                self.removeItem(item)
                self.__dictAxesPointItems.pop(self.__operationMode - 1)
                self.__operationMode = self.__operationMode - 1  # internal add mode
                self.updateAxis()

    def removeAllAxisPoints(self):

        for opMode in DDGraphicsScene.BASITEMS_AXES.keys():

            if (opMode in self.__dictAxesPointItems.keys()):
                item = self.__dictAxesPointItems[opMode]
                self.removeItem(item)
                self.__dictAxesPointItems.pop(opMode)

        self.__operationMode = DDGraphicsScene.OPERATION_MODES.OP_WATCH
        self.updateAxis()

    def updateAxis(self):

        self.updateAxisGen(DDGraphicsScene.OPERATION_MODES.OP_AXIS_X0,
                           DDGraphicsScene.OPERATION_MODES.OP_AXIS_X1,
                           DDGraphicsScene.PRESENTED_AXES.AXIS_X)
        self.updateAxisGen(DDGraphicsScene.OPERATION_MODES.OP_AXIS_Y0,
                           DDGraphicsScene.OPERATION_MODES.OP_AXIS_Y1,
                           DDGraphicsScene.PRESENTED_AXES.AXIS_Y)

    def updateAxisGen(self, op_mode_0, op_mode_1, axis):

        if (self.isAxisPointItemsReadyGen(op_mode_0, op_mode_1)):

            line = QtCore.QLineF(self.__dictAxesPointItems[op_mode_0].scenePos(),
                                 self.__dictAxesPointItems[op_mode_1].scenePos())

            if not (axis in self.__dictAxesItems):
                item = self.addLine(line, DDGraphicsScene.PEN_AXIS)
                self.__dictAxesItems[axis] = item
            else:
                self.__dictAxesItems[axis].setLine(line)

        else:
            if (axis in self.__dictAxesItems):
                self.removeItem(self.__dictAxesItems[axis])
                self.__dictAxesItems.pop(axis)

    def mousePressEvent(self, event):

        QtWidgets.QGraphicsScene.mousePressEvent(self, event)

        mousePos = event.scenePos();
        item = self.itemAt(mousePos, QtGui.QTransform())

        if not (self.__background is None):

            if event.button() == QtCore.Qt.LeftButton:  # add
                if (item is self.__background):
                    self.addAxisPoint(mousePos)
                    self.addDataPoint(mousePos)

            elif event.button() == QtCore.Qt.RightButton:  # remove
                if not (item is self.__background):
                    self.removeAxisPoint(item)
                    self.removeDataPoint(item)

    def mouseMoveEvent(self, event):

        QtWidgets.QGraphicsScene.mouseMoveEvent(self, event)

        if (self.isAxisPointItemsComplete() and self.isAxisRealReady()):

            realCoords = self.calculateRealCoordinates(event.scenePos())

            self.mouseMovedSignal.emit(str(realCoords[0]), str(realCoords[1]))

        else:
            self.mouseMovedSignal.emit("", "")

    def calculateRealCoordinates(self, mousePos):

        # X axes vectors
        XOvec_sc = self.buildAxesPointVec(DDGraphicsScene.OPERATION_MODES.OP_AXIS_X0)
        X1vec_sc = self.buildAxesPointVec(DDGraphicsScene.OPERATION_MODES.OP_AXIS_X1)
        (len_X0X1_sc, evec_X0X1_sc) = self.calcLenEvec(X1vec_sc - XOvec_sc)

        # Y axes vectors
        YOvec_sc = self.buildAxesPointVec(DDGraphicsScene.OPERATION_MODES.OP_AXIS_Y0)
        Y1vec_sc = self.buildAxesPointVec(DDGraphicsScene.OPERATION_MODES.OP_AXIS_Y1)
        (len_Y0Y1_sc, evec_Y0Y1_sc) = self.calcLenEvec(Y1vec_sc - YOvec_sc)

        # Mouse Vector
        mouseVec_sc = self.buildPointVec(mousePos)

        # relative vector
        mouseVec_sc_rel_X0 = mouseVec_sc - XOvec_sc
        mouseVec_sc_rel_Y0 = mouseVec_sc - YOvec_sc

        # projection
        xProj_sc = numpy.dot(mouseVec_sc_rel_X0, evec_X0X1_sc)
        yProj_sc = numpy.dot(mouseVec_sc_rel_Y0, evec_Y0Y1_sc)

        # scaling to real coordinates
        if (self.__scaleX == DDGraphicsScene.SCALETYPE_AXES.AXIS_LIN_X):
            scaleX = (self.__x1Real - self.__x0Real) / len_X0X1_sc
            xReal = self.__x0Real + scaleX * xProj_sc
        else:
            scaleX = (numpy.log(self.__x1Real) - numpy.log(self.__x0Real)) / len_X0X1_sc
            xReal = numpy.exp(numpy.log(self.__x0Real) + scaleX * xProj_sc)

        if (self.__scaleY == DDGraphicsScene.SCALETYPE_AXES.AXIS_LIN_Y):
            scaleY = (self.__y1Real - self.__y0Real) / len_Y0Y1_sc
            yReal = self.__y0Real + scaleY * yProj_sc
        else:
            scaleY = (numpy.log(self.__y1Real) - numpy.log(self.__y0Real)) / len_Y0Y1_sc
            yReal = numpy.exp(numpy.log(self.__y0Real) + scaleY * yProj_sc)

        return (xReal, yReal)

    def buildAxesPointVec(self, opMode):

        return self.buildPointVec(self.__dictAxesPointItems[opMode].scenePos())

    def buildPointVec(self, scrPos):

        return numpy.array([scrPos.x(), scrPos.y()])

    def calcLenEvec(self, vec):

        len_vec = numpy.sqrt(numpy.dot(vec, vec))
        evec = vec / len_vec

        return (len_vec, evec)

    def determineDataPointsRealCoords(self):

        dictRealCoords = {}

        if (self.isAxisPointItemsComplete() and self.isAxisRealReady()):

            for nameSingleLine in self.__dictLinesOfDataPoints.keys():

                numItems = len(self.__dictLinesOfDataPoints[nameSingleLine])
                dictRealCoords[nameSingleLine] = numpy.zeros((numItems, 2))

                ii = -1
                for item in self.__dictLinesOfDataPoints[nameSingleLine]:
                    ii = ii + 1

                    itemPos = item.scenePos()
                    (x, y) = self.calculateRealCoordinates(itemPos)

                    dictRealCoords[nameSingleLine][ii, 0] = x
                    dictRealCoords[nameSingleLine][ii, 1] = y

        return dictRealCoords

    def isAxisPointItemsReadyGen(self, op_mode_0, op_mode_1):

        return (op_mode_0 in self.__dictAxesPointItems) and (op_mode_1 in self.__dictAxesPointItems)

    def isAxisPointItemsComplete(self):

        return (self.isAxisPointItemsReadyGen(DDGraphicsScene.OPERATION_MODES.OP_AXIS_X0,
                                              DDGraphicsScene.OPERATION_MODES.OP_AXIS_X1) and
                self.isAxisPointItemsReadyGen(DDGraphicsScene.OPERATION_MODES.OP_AXIS_Y0,
                                              DDGraphicsScene.OPERATION_MODES.OP_AXIS_Y1))

    def isAxisRealReady(self):

        areValsPres = not ((self.__x0Real is None) or (self.__x1Real is None) or (self.__y0Real is None) or (
                self.__y1Real is None))
        areValsOK = (self.__x0Real != self.__x1Real) and (self.__y0Real != self.__y1Real)

        if (self.__scaleX == DDGraphicsScene.SCALETYPE_AXES.AXIS_LOG_X):
            areLogValsValid_x = (self.__x0Real > 0.0) and (self.__x1Real > 0.0)
        else:
            areLogValsValid_x = True

        if (self.__scaleY == DDGraphicsScene.SCALETYPE_AXES.AXIS_LOG_Y):
            areLogValsValid_y = (self.__y0Real > 0.0) and (self.__y1Real > 0.0)
        else:
            areLogValsValid_y = True

        return (areValsPres and areValsOK and areLogValsValid_x and areLogValsValid_y)
