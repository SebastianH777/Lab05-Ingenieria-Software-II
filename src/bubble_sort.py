class BubbleSorter:

    def sort(self, values):
        n = len(values)

        for i in range(n, 1, -1):
            for j in range(i - 1):

                if values[j] > values[j + 1]:
                    aux = values[j]
                    values[j] = values[j + 1]
                    values[j + 1] = aux

        return values