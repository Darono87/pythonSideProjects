import numpy as np
import matplotlib.pyplot as plt

class selectionSortOperator:
    def __init__(self, loadedArray, plot):
        self.toSort = loadedArray
        self.sorted = False
        self.plot = plot

        if len(loadedArray) < 2:
            self.sorted = True
        else:
            self.sortAxis = 0


    def searchForMin(self):
        tempMin = self.sortAxis
        for i in range(self.sortAxis, len(self.toSort)):
            if self.toSort[i] < self.toSort[tempMin]:
                tempMin = i
        return tempMin

    def performSortStep(self):

        if self.sorted:
            return 1

        if self.sortAxis >= len(self.toSort)-1:
            self.sorted = True
            return 1

        t = self.searchForMin()
        temp = self.toSort[self.sortAxis]
        self.toSort[self.sortAxis] = self.toSort[t]
        self.toSort[t] = temp
        self.sortAxis+=1

        return 0

    def animateSortOperation(self, i):
        for rect, h in zip(self.plot, self.toSort):
            rect.set_height(h)
        self.performSortStep()
