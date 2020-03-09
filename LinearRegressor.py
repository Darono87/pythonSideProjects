import matplotlib.pyplot as plt
import numpy as np

def testData(aGuess, bGuess, aCoe, bCoe, spread, method, numSamples):
    xValuesTest, yValuesTest = createExperimentData(aCoe, bCoe, spread, method, numSamples)
    print(calculateRMSE(aGuess, bGuess, xValuesTest, yValuesTest))
    showScatter([aGuess], [bGuess], xValuesTest, yValuesTest,True)

def createExperimentData(aCoe, bCoe, spread, method, numSamples):

    xValuesTest = np.sort(np.random.sample(numSamples) * numSamples)
    yValuesTest = xValuesTest * aCoe + bCoe
    if not method:
        deviationMax = yValuesTest[int(numSamples/2)] * spread
    else:
        deviationMax = yValuesTest * spread

    deviation = deviationMax * np.abs(np.random.standard_normal(numSamples))
    deviationCoe = np.random.choice([-1, 1], numSamples)
    deviation = deviation * deviationCoe
    yValuesTest = yValuesTest + deviation

    return xValuesTest, yValuesTest

def gradiantDescent(actualA, actualB, xVal, yVal, learningRateA, learningRateB, periodLength, periodNum):
    guessListA = [actualA]
    guessListB = [actualB]
    for y in range(periodNum):
        for x in range(periodLength):
            actualA, actualB = gradiantDescentStep(actualA, actualB, xVal, yVal, learningRateA, learningRateB)
        guessListA.append(actualA)
        guessListB.append(actualB)
        showScatter([actualA], [actualB], xVal, yVal)

    showScatter(guessListA, guessListB, xVal, yVal)
    return actualA, actualB

def gradiantDescentStep(actualA, actualB, xVal, yVal, learningRateA, learningRateB):
    makeGuesses = actualA * xVal + actualB
    calB = makeGuesses - yVal
    sumB = 0
    for x in calB:
        sumB += x
    sumB = (sumB*2*learningRateB)/sumB.size
    newB = actualB - sumB

    calA = calB*xVal
    sumA = 0
    for x in calA:
        sumA += x
    sumA = (sumA*2*learningRateA)/sumA.size
    newA = actualA - sumA

    return newA, newB

def showScatter(guessA,guessB,xVal,yVal,showText = False):
    plt.scatter(x=xVal, y=yVal, c="#00AA55")
    limits = plt.axis()
    for x in np.arange(len(guessA)):
            linePoint1 = guessA[x]*limits[0]+guessB[x]
            linePoint2 = guessA[x]*limits[1]+guessB[x]
            plt.plot([limits[0],limits[1]],[linePoint1,linePoint2])
    plt.axis(limits)
    plt.xlabel("generowana moc W/h")
    plt.ylabel("cena produktu")
    if showText:
        plt.text(0.5, 0.95, r"RMSE = $ \sqrt{(\frac{1}{k} * \sum_{n=0}^{k} (x_n-y_n)^2)}$", verticalalignment = 'top', horizontalalignment = 'center',fontsize=8, transform=plt.gcf().transFigure, bbox=dict(boxstyle='round',pad=1, facecolor='#005500', alpha=0.5))
    plt.show()


def calculateRMSE(guessA, guessB, xVal, yVal):
    makeGuesses = guessA * xVal + guessB
    RMSEtab = (yVal-makeGuesses)**2
    RMSE = 0
    for i in RMSEtab:
        RMSE += i
    RMSE /= RMSEtab.size
    RMSE = np.sqrt(RMSE)
    return RMSE


plt.rc('text',usetex = True)
aCoefficient = float(input("Give me a coefficient of a line equation"))
bCoefficient = float(input("Give me b coefficient of a line equation"))
spread = float(input("Give me a scalar, from 0-1 to calculate standard deviation"))
method = int(input("Which method to use (0 = constant, 1 = linear)"))


aGuess = 2
bGuess = 5
xValuesTrain, yValuesTrain = createExperimentData(aCoefficient,bCoefficient,spread,method,300)

showScatter([], [],xValuesTrain,yValuesTrain)
print(aGuess, bGuess)
print(calculateRMSE(aGuess,bGuess,xValuesTrain,yValuesTrain))

aGuess, bGuess = gradiantDescent(aGuess, bGuess, xValuesTrain, yValuesTrain, 0.00000001, 0.0001, 5, 8)
print(aGuess, bGuess)
print(calculateRMSE(aGuess,bGuess,xValuesTrain,yValuesTrain))
testData(aGuess, bGuess, aCoefficient, bCoefficient, spread, method, 300)
