from app.knapsackAlgoritmTemplate import KnapsackAlgorithmtemplate

class KnapsackNaive(KnapsackAlgorithmtemplate):
    def findMaxValue(self, weights:list, prices:list, maxCapacity:int)->float:
        return self.__knapSackNaiveRec(weights, prices, maxCapacity, len(weights))

    def __knapSackNaiveRec(self,weights:list, prices:list, maxCapacity:int, indexItem:int)->float:

        if indexItem == 0 or maxCapacity == 0:
            return 0

        elif weights[indexItem - 1] > maxCapacity:
            return self.__knapSackNaiveRec(weights, prices, maxCapacity, indexItem - 1)

        else:
            withI = prices[indexItem - 1] + self.__knapSackNaiveRec(weights, prices, maxCapacity - weights[indexItem - 1], indexItem - 1)
            withoutI = self.__knapSackNaiveRec(weights, prices, maxCapacity, indexItem - 1)

            if withI > withoutI:
                return withI
            else:
                return withoutI