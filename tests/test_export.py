import numpy
import unittest


from src.diagramdigitizer.export import interpolateDataDict


class TestInterpolateDataDict(unittest.TestCase):

    def test_interpolateDataDict(self):

        arr1 = numpy.array([[1., 1.], [3., 2.], [4., 3.], [2., 4.]])
        arr2 = numpy.array([[8., 4.], [5., 5.], [4., 6.], [7., 7.]])
        dataDict = {'set1': arr1, 'set2': arr2}

        arr1Expexted = numpy.array([[1., 1.], [1.125, 1.0625], [1.25, 1.125], [1.375, 1.1875], [1.5, 1.25],
                                    [1.625, 1.3125], [1.75, 1.375], [1.875, 1.4375], [2., 1.5]])
        arr2Expexted = numpy.array([[8., 7.], [7.875, 7.], [7.75, 7.], [7.625, 7.], [7.5, 7.], [7.375, 7.],
                                    [7.25, 7.], [7.125, 7.], [7., 4.]])

        dataDictRes = interpolateDataDict(dataDict, 9)
        arr1Res = dataDictRes['set1']
        arr2Res = dataDictRes['set2']

        self.assertListEqual(arr1Res.tolist(), arr1Expexted.tolist())
        self.assertListEqual(arr2Res.tolist(), arr2Expexted.tolist())
