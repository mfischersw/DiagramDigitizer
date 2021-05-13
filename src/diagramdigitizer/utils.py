# This file is part of DiagramDigitizer.

"""
.. module:: utils
   :synopsis: Utility functions.

.. moduleauthor:: Michael Fischer
"""



import numpy



# Constants
DATASETTAG = "set"
DATASETTAGLEN = len(DATASETTAG)

DATA_DICT_EMPTY = -1
DATA_DICT_NO_CONTENT = 0
DATA_DICT_PART = 1
DATA_DICT_FILLED = 2



def sortNameListWithTag(nameList):
    """Sort list of entries [DATASETTAG][number] according to number.

    Parameters
    ----------
    nameList : list (str)
        List of entries [DATASETTAG][number].

    Returns
    -------
    out : list (str)
        Sorted list of entries [DATASETTAG][number].

    Example
    -------
    Basic example.

    >>> from diagramdigitizer import utils
    >>> nameList = [ 'set2', 'set4', 'set1', 'set13', 'set12' ]
    >>> nameList
    ['set2', 'set4', 'set1', 'set13', 'set12']
    >>> utils.sortNameListWithTag(nameList)
    ['set1', 'set2', 'set4', 'set12', 'set13']
    """

    indList = []
    for name in nameList:
        ind = int(name[DATASETTAGLEN:])
        indList.append(ind)

    indList.sort()

    nameListOut = []
    for ind in indList:
        nameListOut.append(DATASETTAG + str(ind))

    return nameListOut



def contentStatusDict(dataDict):
    """Content status (empty, no content, partially filled, filled) of data dictionary { str1 : numpy-array1, ...}.

    Parameters
    ----------
    dataDict : dict
        Data dictionary { TAG1 : numpy-array1, ...}.

    Returns
    -------
    out : int
        Content status.

    Example
    -------
    Basic example.

    >>> from diagramdigitizer import utils
    >>> dataDict = {}
    >>> utils.contentStatusDict(dataDict)
    -1
    >>> dataDict = { 'set1' : numpy.array([]) }
    >>> utils.contentStatusDict(dataDict)
    0
    >>> dataDict = { 'set1' : numpy.array([1.0, 2.0]), 'set2' : numpy.array([]) }
    >>> utils.contentStatusDict(dataDict)
    1
    >>> dataDict = { 'set1' : numpy.array([1.0, 2.0]), 'set2' : numpy.array([3.0, 4.0]) }
    >>> utils.contentStatusDict(dataDict)
    2
    """

    Nkeys = len(dataDict)
    Nfilled = 0

    if (Nkeys==0):
        return DATA_DICT_EMPTY
    else:
        for key in dataDict.keys():
            if (len(dataDict[key])>0):
                Nfilled = Nfilled + 1

        if (Nfilled == 0):
            return DATA_DICT_NO_CONTENT
        elif (Nfilled < Nkeys):
            return DATA_DICT_PART
        elif (Nfilled == Nkeys):
            return DATA_DICT_FILLED



def sortArrDataDict(dataDict):
    """Sort (x,y)-coordinate arrays within data dictionary { str1 : numpy-array1, ...} according to x-values in
    ascending order.

    Parameters
    ----------
    dataDict : dict
        Data dictionary { TAG1 : numpy-array1, ...}.

    Returns
    -------
    out : dict
        Data dictionary { TAG1 : sorted-numpy-array1, ...}.

    Example
    -------
    Basic example.

    >>> from diagramdigitizer import utils
    >>> arr1 = numpy.array([[1., 1.], [3., 2.], [4., 3.], [2., 4.]])
    >>> arr2 = numpy.array([[8., 4.], [5., 5.], [4., 6.], [7., 7.]])
    >>> dataDict = { 'set1' : arr1, 'set2' : arr2 }
    >>> utils.sortArrDataDict(dataDict)
    {'set1': array([[1., 1.],
        [2., 4.],
        [3., 2.],
        [4., 3.]]),
    'set2': array([[4., 6.],
        [5., 5.],
        [7., 7.],
        [8., 4.]])}
    """

    contStDict = contentStatusDict(dataDict)

    if ( (contStDict==DATA_DICT_EMPTY) or (contStDict==DATA_DICT_NO_CONTENT) ):
        return dataDict

    dataDictNew = {}

    for nameLine in dataDict.keys():
        
        arrin = dataDict[nameLine]

        if (len(arrin)>0):
            # get and sort by x value
            arr = arrin[numpy.argsort(arrin[:, 0])]
            dataDictNew[nameLine] = arr
        else:
            dataDictNew[nameLine] = arrin

    return dataDictNew



def trafoDictKeys(dataDict):
    """Transform dictionary keys from [DATASETTAG][number] to [number].

    Parameters
    ----------
    dataDict : dict
        Data dictionary { TAG1 : data, ...}.

    Returns
    -------
    out : dict
        Data dictionary { 1 : data, ...}.

    Example
    -------
    Basic example.

    >>> from diagramdigitizer import utils
    >>> dataDict = { 'set1' : 1.0, 'set2' : 2.0 }
    >>> sorted(utils.trafoDictKeys(dataDict).keys())
    [1, 2]
    """

    dataDictNew = {}
    for nameLine in dataDict.keys():
        index = int(nameLine[DATASETTAGLEN:])
        dataDictNew[index] = dataDict[nameLine]

    return dataDictNew