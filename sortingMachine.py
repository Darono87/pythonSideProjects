import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import insertionSortOperator as ISO
import selectionSortOperator as SSO
import bubbleSortOperator as BSO

#IDEA - MAKE GRADIENT
#\
#\
#\

def setBarsColorRainbowly(bars):
    colors = ["r","b","c","b","k","y"]
    i = 0
    for bar in bars:
        bar.set_color(colors[i])
        i+=1
        if i == len(colors):
            i = 0


testArray = np.random.randint(1, 100, 100)
frameTime = 150

plt.subplots_adjust(0.09,0.1,0.95,0.9,0.15,0.34)
plt.gcf().canvas.set_window_title('Sorting Machine')

bubbleBars = plt.subplot(221)
plt.title("Bubble Sort")
bubbleArray = np.copy(testArray)
bubblePlot = bubbleBars.bar(np.linspace(1,100,100),testArray,edgecolor="c", color="r")
operatorBSO = BSO.bubbleSortOperator(bubbleArray,bubblePlot)
aniBubble = animation.FuncAnimation(plt.gcf(),operatorBSO.animateSortOperation,interval=frameTime)


mergeBars = plt.subplot(222)
plt.title("Merge Sort")
mergeArray = np.copy(testArray)
#SAI.mergeSort(mergeArray)
mergeBars.bar(np.linspace(1,100,100),mergeArray,color="b")


selectionBars = plt.subplot(223)
selectionArray = np.copy(testArray)
selectionPlot = plt.bar(np.linspace(1, 100, 100), selectionArray, color="b")
plt.title("Selection Sort")
setBarsColorRainbowly(selectionPlot)
operatorSSO = SSO.selectionSortOperator(selectionArray,selectionPlot)
aniSelection = animation.FuncAnimation(plt.gcf(),operatorSSO.animateSortOperation,interval=frameTime)


insertionBars = plt.subplot(224)
insertionArray = np.copy(testArray)
insertionPlot = plt.bar(np.linspace(1, 100, 100), insertionArray, color="m")
plt.title("Insertion Sort")
operatorISO = ISO.insertionSortOperator(insertionArray,insertionPlot)
aniInsertion = animation.FuncAnimation(plt.gcf(),operatorISO.animateSortOperation,interval=frameTime)



plt.show()
