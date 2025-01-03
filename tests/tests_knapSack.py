import unittest
from app.knapsackAlgoritmTemplate import KnapsackAlgorithmtemplate
from app.knapSackNaive import KnapsackNaive
from app.knapSackMem import KnapsackMemory
from app.knapSacTab import KnapsackTable

class TestKnapsack(unittest.TestCase):
    __WEIGHT=[1, 12, 4, 1, 2]
    __PRICE=[2, 4, 10, 1, 2]

    def test_knapsackNaive(self):
        self.__knapsackProblemTest(KnapsackNaive())

    def test_knapsackMem(self):
        self.__knapsackProblemTest(KnapsackMemory())

    def test_knapsackTab(self):
        self.__knapsackProblemTest(KnapsackTable())

    def __knapsackProblemTest(self, algorithm:KnapsackAlgorithmtemplate):
        self.assertEqual(algorithm.findMaxValue(self.__WEIGHT, self.__PRICE, 1), 2)
        self.assertEqual(algorithm.findMaxValue(self.__WEIGHT, self.__PRICE, 2), 3)
        self.assertEqual(algorithm.findMaxValue(self.__WEIGHT, self.__PRICE, 4), 10)
        self.assertEqual(algorithm.findMaxValue(self.__WEIGHT, self.__PRICE, 5), 12)
        self.assertEqual(algorithm.findMaxValue(self.__WEIGHT, self.__PRICE, 8), 15)

        