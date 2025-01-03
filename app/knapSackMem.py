from app.knapsackAlgoritmTemplate import KnapsackAlgorithmtemplate

class KnapsackMemory(KnapsackAlgorithmtemplate):
    def findMaxValue(self, weights:list, prices:list, maxCapacity:int)->float:
        indexItem = len(prices)
        memory = {}
        return  self.__ksMenRec(weights, prices, maxCapacity, indexItem, memory)

    def __ksMenRec(self, weights:list, prices:list, maxCapacity:int, indexItem:int, memory:dict)->float:
        if (maxCapacity, indexItem) in memory:
            return memory[(maxCapacity, indexItem)]

        if indexItem == 0 or maxCapacity == 0:
            memory[(maxCapacity, indexItem)] = 0

        elif weights[indexItem - 1] > maxCapacity:
            memory[(maxCapacity, indexItem)] = self.__ksMenRec(weights, prices, maxCapacity, indexItem - 1, memory)

        else:
            withI = prices[indexItem - 1] + self.__ksMenRec(weights, prices, maxCapacity - weights[indexItem - 1], indexItem - 1, memory)
            withoutI = self.__ksMenRec(weights, prices, maxCapacity, indexItem - 1, memory)

            if withI > withoutI:
                memory[(maxCapacity, indexItem)] = withI
            else:
                memory[(maxCapacity, indexItem)] = withoutI

        return memory[(maxCapacity, indexItem)]
