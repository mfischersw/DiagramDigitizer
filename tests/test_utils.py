import numpy
import unittest


from src.diagramdigitizer.utils import DATA_DICT_EMPTY
from src.diagramdigitizer.utils import DATA_DICT_NO_CONTENT
from src.diagramdigitizer.utils import DATA_DICT_PART
from src.diagramdigitizer.utils import DATA_DICT_FILLED
from src.diagramdigitizer.utils import sortNameListWithTag
from src.diagramdigitizer.utils import contentStatusDict
from src.diagramdigitizer.utils import sortArrDataDict
from src.diagramdigitizer.utils import trafoDictKeys



class Test_sortNameListWithTag(unittest.TestCase):

    def test_sortNameListWithTag(self):
        testList = ['set2', 'set4', 'set1', 'set13', 'set12']
        expectedList = ['set1', 'set2', 'set4', 'set12', 'set13']
        self.assertListEqual(sortNameListWithTag(testList), expectedList)



class Test_contentStatusDict(unittest.TestCase):

    def test_contentStatusDict_empty(self):
        dataDict = {}
        self.assertEqual(contentStatusDict(dataDict), DATA_DICT_EMPTY)

    def test_contentStatusDict_nocontent(self):
        dataDict = { 'set1' : numpy.array([]) }
        self.assertEqual(contentStatusDict(dataDict), DATA_DICT_NO_CONTENT)

    def test_contentStatusDict_part(self):
        dataDict = { 'set1' : numpy.array([1.0, 2.0]), 'set2' : numpy.array([]) }
        self.assertEqual(contentStatusDict(dataDict), DATA_DICT_PART)

    def test_contentStatusDict_empty(self):
        dataDict = { 'set1' : numpy.array([1.0, 2.0]), 'set2' : numpy.array([3.0, 4.0]) }
        self.assertEqual(contentStatusDict(dataDict), DATA_DICT_FILLED)



class Test_sortArrDataDict(unittest.TestCase):

    def test_sortArrDataDict(self):

        arr1 = numpy.array([[1., 1.], [3., 2.], [4., 3.], [2., 4.]])
        arr2 = numpy.array([[8., 4.], [5., 5.], [4., 6.], [7., 7.]])
        dataDict = {'set1': arr1, 'set2': arr2}
        resDict = sortArrDataDict(dataDict)
        resArr1 = resDict['set1']
        res1_x = list(resArr1[:, 0])
        res1_y = list(resArr1[:, 1])
        resArr2 = resDict['set2']
        res2_x = list(resArr2[:, 0])
        res2_y = list(resArr2[:, 1])
        expectedResArr1 = numpy.array([[1., 1.], [2., 4.], [3., 2.], [4., 3.]])
        expectedRes1_x = list(expectedResArr1[:, 0])
        expectedRes1_y = list(expectedResArr1[:, 1])
        expectedResArr2 = numpy.array([[4., 6.], [5., 5.], [7., 7.], [8., 4.]])
        expectedRes2_x = list(expectedResArr2[:, 0])
        expectedRes2_y = list(expectedResArr2[:, 1])

        self.assertListEqual(res1_x, expectedRes1_x)
        self.assertListEqual(res1_y, expectedRes1_y)
        self.assertListEqual(res2_x, expectedRes2_x)
        self.assertListEqual(res2_y, expectedRes2_y)



class Test_trafoDictKeys(unittest.TestCase):

    def test_trafoDictKeys(self):
        dataDict = {'set1': 1.0, 'set2': 2.0}
        expectedList = [1, 2]
        self.assertListEqual(sorted(trafoDictKeys(dataDict).keys()), expectedList)



if __name__ == '__main__':
    unittest.main()
