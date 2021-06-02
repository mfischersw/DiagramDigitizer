# This file is part of DiagramDigitizer.

"""
.. module:: export
   :synopsis: Data export functions.

.. moduleauthor:: Michael Fischer
"""

# Imports
from collections import OrderedDict
import numpy
import xlsxwriter

from . import utils

# Constants
NINTERP = 100
FILE_FILTERS = {"text": '*.txt',
                "csv": '*.csv',
                "excel": '*.xlsx'}

PROCESSING_TYPE_INONE = 0
PROCESSING_TYPE_ISORT = 1
PROCESSING_TYPE_INTERP = 2


def interpolateDataDict(dataDict, nintp):
    """Interpolate (x,y)-coordinate data arrays within data dictionary { str1 : numpy-array1, ...}
    to new x-coordinates. The original (x,y)-coordinate data arrays are assumed to be sorted according to
    x-values.

    Parameters
    ----------
    dataDict : dict
        Data dictionary { str1 : numpy-array1, ...}.
    nintp : int
        Number of samples for interpolation.

    Returns
    -------
    out : dict
        Data dictionary { str1 : interpolated-numpy-array1, ...}.

    Example
    -------
    Basic example.

    >>> import numpy
    >>> from diagramdigitizer import export
    >>> arr1 = numpy.array([[1., 1.], [3., 2.], [4., 3.], [2., 4.]])
    >>> arr2 = numpy.array([[8., 4.], [5., 5.], [4., 6.], [7., 7.]])
    >>> dataDict = { 'set1' : arr1, 'set2' : arr2 }
    >>> export.interpolateDataDict(dataDict, 9)
    {'set1': array([[1.    , 1.    ],
        [1.125 , 1.0625],
        [1.25  , 1.125 ],
        [1.375 , 1.1875],
        [1.5   , 1.25  ],
        [1.625 , 1.3125],
        [1.75  , 1.375 ],
        [1.875 , 1.4375],
        [2.    , 1.5   ]]),
    'set2': array([[8.   , 7.   ],
        [7.875, 7.   ],
        [7.75 , 7.   ],
        [7.625, 7.   ],
        [7.5  , 7.   ],
        [7.375, 7.   ],
        [7.25 , 7.   ],
        [7.125, 7.   ],
        [7.   , 4.   ]])}
    """
    dataDictNew = {}

    for nameLine in dataDict.keys():

        arr = dataDict[nameLine]

        if (len(arr) > 1):

            arrNew = numpy.zeros((nintp, 2))
            arrNew[:, 0] = numpy.linspace(arr[0, 0], arr[-1, 0], num=nintp, endpoint=True)
            arrNew[:, 1] = numpy.interp(arrNew[:, 0], arr[:, 0], arr[:, 1])

            dataDictNew[nameLine] = arrNew

        else:
            dataDictNew[nameLine] = arr

    return dataDictNew


def exportData_to_text(filepath, dataDict, deli):
    """Write (x,y)-coordinate data arrays within data dictionary { str1 : numpy-array1, ...}
    to a text file. The x- and y-values are separated by a delimiter.

    Parameters
    ----------
    filepath : str
        File path.
    dataDict : dict
        Data dictionary { str1 : numpy-array1, ...}.
    deli : str
        Delimiter.
    """
    try:
        with open(filepath, 'w') as fp:

            dataDictNew = utils.trafoDictKeys(dataDict)
            dataDictOrd = OrderedDict(sorted(dataDictNew.items()))

            for nameLine in dataDictOrd.keys():

                arr = dataDictOrd[nameLine]

                if not (deli == ";"):

                    fp.write('# ' + utils.DATASETTAG + str(nameLine) + '\n')

                    for ii in range(len(arr)):
                        fp.write(str(arr[ii, 0]) + deli + str(arr[ii, 1]) + '\n')

                    fp.write('\n')

                else:
                    for ii in range(len(arr)):
                        fp.write(utils.DATASETTAG + str(nameLine) + deli + str(arr[ii, 0]) + deli +
                                 str(arr[ii, 1]) + '\n')

    except OSError as e:
        print("OS ERROR: ", e.errno)


def exportData_to_excel(filepath, dataDict):
    """Write (x,y)-coordinate data arrays within data dictionary { str1 : numpy-array1, ...}
    to an Excel file. The resulting Excel file contains a plot of the data.

    Parameters
    ----------
    filepath : str
        File path.
    dataDict : dict
        Data dictionary { str1 : numpy-array1, ...}.
    """
    try:
        # Open Excel workbook
        workbook = xlsxwriter.Workbook(filepath)
        workbook.add_format({'bold': True})
        formatHead = workbook.add_format()
        formatHead.set_bg_color('green')

        worksheet = workbook.add_worksheet()

        contStDict = utils.contentStatusDict(dataDict)
        if (contStDict == utils.DATA_DICT_EMPTY or contStDict == utils.DATA_DICT_NO_CONTENT):
            workbook.close()
            return

        # Write data
        dataDictNew = utils.trafoDictKeys(dataDict)
        dataDictOrd = OrderedDict(sorted(dataDictNew.items()))

        indStart = []
        indEnd = []
        count = 0
        for nameLine in dataDictOrd.keys():
            worksheet.write(count, 0, utils.DATASETTAG + str(nameLine), formatHead)
            count = count + 1

            indStart.append(count + 1)

            arr = dataDictOrd[nameLine]
            if (len(arr) > 0):
                for ii in range(len(arr)):
                    worksheet.write(count + ii, 0, (arr[ii, 0]))
                    worksheet.write(count + ii, 1, (arr[ii, 1]))

                count = count + ii + 2
            else:
                count = count + 2

            indEnd.append(count - 1)

        # Diagram in excel sheet
        chartAll = workbook.add_chart({'type': 'scatter'})

        for ii in range(len(indStart)):

            if (indStart[ii] == indEnd[ii]):
                continue

            excflag_name = '=Sheet1!$A$' + str(indStart[ii] - 1)
            excflag_categories = '=Sheet1!$A$' + str(indStart[ii]) + ':$A$' + str(indEnd[ii])
            excflag_values = '=Sheet1!$B$' + str(indStart[ii]) + ':$B$' + str(indEnd[ii])

            chartAll.add_series({
                'name': excflag_name,
                'categories': excflag_categories,
                'values': excflag_values,
                'line': {'none': True},
                'marker': {'type': 'automatic'},
            })

        chartAll.set_title({'name': 'Results of digitization'})
        chartAll.set_x_axis({'name': 'x'})
        chartAll.set_y_axis({'name': 'y'})
        chartAll.set_size({'x_scale': 2.0, 'y_scale': 1.5})
        chartAll.set_style(42)

        worksheet.insert_chart('D2', chartAll)

        # Close Excel workbook
        workbook.close()

    except OSError as e:
        print("OS ERROR: ", e.errno)


def exportData_to_fileGen(filepath, dataDict, filetype, procType):
    """Write (x,y)-coordinate data arrays within data dictionary { str1 : numpy-array1, ...}
    to a file (text or Excel).

    Parameters
    ----------
    filepath : str
        File path.
    dataDict : dict
        Data dictionary { str1 : numpy-array1, ...}.
    filetype: str
        Type of file ("text", "csv", "excel").
    procType: int
        Processing type, i.e. none, sort, interpolation.
    """
    if (procType == PROCESSING_TYPE_INONE):
        dataDicth = dataDict
    elif (procType == PROCESSING_TYPE_ISORT):
        dataDicth = utils.sortArrDataDict(dataDict)
    elif (procType == PROCESSING_TYPE_INTERP):
        dataDicth = interpolateDataDict(utils.sortArrDataDict(dataDict), NINTERP)

    if (filetype == "text"):
        exportData_to_text(filepath, dataDicth, "\t")
    elif (filetype == "csv"):
        exportData_to_text(filepath, dataDicth, ";")
    elif (filetype == "excel"):
        exportData_to_excel(filepath, dataDicth)
