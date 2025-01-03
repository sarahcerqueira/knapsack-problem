from app.knapsackAlgoritmTemplate import KnapsackAlgorithmtemplate

class KnapsackTable(KnapsackAlgorithmtemplate):
    def findMaxValue(self, weights:list, prices:list, maxCapacity:int)->float:
        table = self.__buildMatrix(weights, prices, maxCapacity)
        numItens = len(weights) - 1
        return table[numItens][maxCapacity]

    def __buildMatrix(self, weights, prices, maxCapacity):
        table = self.__createMatrixWithZeros(prices,maxCapacity)
        weights.insert(0, 0)
        prices.insert(0, 0)
        indexLine = 0
        indexColumn = 0

        while indexLine < len(prices):
            while indexColumn < maxCapacity + 1:
                if indexColumn == 0 or indexLine == 0:
                    table[indexLine][indexColumn] = 0

                elif weights[indexLine] <= indexColumn:
                    withoutI = table[indexLine - 1][indexColumn]
                    withI = prices[indexLine] + table[indexLine - 1][indexColumn - weights[indexLine]]

                    if withI > withoutI:
                        table[indexLine][indexColumn] = withI
                    else:
                        table[indexLine][indexColumn] = withoutI
                else:
                    table[indexLine][indexColumn] = table[indexLine - 1][indexColumn]

                indexColumn = indexColumn + 1
            indexLine = indexLine + 1
            indexColumn = 0

        return table

    def __createMatrixWithZeros(self, prices, maxCapacity):
        indexLines = 0
        table = []

        while indexLines < len(prices) + 1:
            line = [0] * (maxCapacity + 1)
            table.append(line)
            indexLines = indexLines + 1

        return table