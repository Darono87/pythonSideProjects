import numpy as np
import matplotlib.pyplot as plt


class bubbleSortOperator:
    def __init__(self, loadedArray, plot):
        self.toSort = loadedArray
        self.sorted = False
        self.plot = plot
        self.subsOccurred = False
        self.subsElem = 0
        self.subsDelim = 1

        if len(loadedArray) < 2:
            self.sorted = True

    def performSortStep(self):
        for i in range(0,100):
            if self.sorted:
                return 1

            if self.subsElem == len(self.toSort) - self.subsDelim:
                if not self.subsOccurred:
                    self.sorted = 1
                    return 1
                else:
                    self.subsElem = 0
                    self.subsOccurred = False
                    self.subsDelim += 1
                    return 0

            if self.toSort[self.subsElem] > self.toSort[self.subsElem + 1]:
                temp = self.toSort[self.subsElem]
                self.toSort[self.subsElem] = self.toSort[self.subsElem + 1]
                self.toSort[self.subsElem + 1] = temp
                self.subsOccurred = True
            self.subsElem += 1
        return 0

    def animateSortOperation(self, i):
        for rect, h in zip(self.plot, self.toSort):
            rect.set_height(h)
        self.performSortStep()
