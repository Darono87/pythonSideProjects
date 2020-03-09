import numpy as np
import matplotlib.pyplot as plt


class insertionSortOperator:
    def __init__(self,loadedArray, plot):
        self.toSort = loadedArray
        self.sorted = False
        self.plot = plot

        if len(loadedArray) < 2:
            self.sorted = True
        else:
            self.propagate = 1
            self.toSwitch = 0
            self.toMove = self.toSort[self.propagate]

    def performSlowSortStep(self):
        if self.sorted:
            return
        if self.toSwitch < 0 or self.toSort[self.toSwitch] <= self.toMove:
            #print("B")
            self.toSort[self.toSwitch+1] = self.toMove
            self.propagate += 1
            if self.propagate == len(self.toSort):
                self.sorted = True
                return 1
            self.toSwitch = self.propagate - 1
            self.toMove = self.toSort[self.propagate]
            return 0
        else:
            #print("A")
            self.toSort[self.toSwitch + 1] = self.toSort[self.toSwitch]
            self.toSwitch -= 1
            return 0

    def performFastSortStep(self):
        while True:
            if self.sorted:
                return 1
            if self.toSwitch < 0 or self.toSort[self.toSwitch] <= self.toMove:
                #print("B")
                self.toSort[self.toSwitch+1] = self.toMove
                self.propagate += 1
                if self.propagate == len(self.toSort):
                    self.sorted = True
                    return 1
                self.toSwitch = self.propagate - 1
                self.toMove = self.toSort[self.propagate]
                return 0
            else:
                #print("A")
                self.toSort[self.toSwitch + 1] = self.toSort[self.toSwitch]
                self.toSwitch -= 1

    def animateSortOperation(self, i):
        for rect, h in zip(self.plot, self.toSort):
            rect.set_height(h)
        self.performFastSortStep()

