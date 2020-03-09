import matplotlib.pyplot as plt
import numpy as np


def findSymbolOutOfPara(symbol, content):
    num = -1
    ignore = False
    while num < len(content)-1:
        num += 1
        if content[num]==')':
            ignore = False
            continue
        if ignore:
            continue
        if content[num]=='(':
            ignore = True
            continue
        if symbol == content[num]:
            return num


    return -1

trygEq = input("Give me please, a sin/cos equation to sketch")
pointToCut = findSymbolOutOfPara('+',trygEq)
if pointToCut!=-1:
    trygEqExplode = [trygEq[0:pointToCut],trygEq[pointToCut+1:]]
else:
    trygEqExplode = [trygEq]
yShift = 0
mainPart = ""
if len(trygEqExplode) > 1:
    if trygEqExplode[0].find('s')!=-1 or trygEqExplode[0].find('c')!=-1   or trygEqExplode[0].find('t')!=-1  or trygEqExplode[0].find('l')!=-1:
        mainPart = trygEqExplode[0]
        yShift = int(trygEqExplode[1])
    else:
        mainPart = trygEqExplode[1]
        yShift = int(trygEqExplode[0])
else:
    mainPart = trygEq
print(mainPart)


pointToCut = findSymbolOutOfPara('*',mainPart)
if pointToCut!=-1:
    mainProducts = [mainPart[0:pointToCut],mainPart[pointToCut+1:]]
else:
    mainProducts = [mainPart]
multiplier = 1
mainFunction = ""
print(mainProducts[1])
if len(mainProducts) > 1:
    if mainProducts[0].find('s')!=-1 or mainProducts[0].find('c')!=-1  or mainProducts[0].find('t')!=-1  or mainProducts[0].find('l')!=-1 :
        mainFunction = mainProducts[0]
        multiplier = int(mainProducts[1])
    else:
        mainFunction = mainProducts[1]
        multiplier = int(mainProducts[0])
else:
    mainFunction = mainProducts[0]

print(mainFunction)
insideFunction = mainFunction.split("(")[1]
insideFunction = insideFunction[:-1]
insideFunctionSplit = insideFunction.split('+')
addCoefficient = 0
multiCoefficient = 1
if len(insideFunctionSplit) > 1:
    if insideFunctionSplit[0].find('x')!=-1:
        addCoefficient = int(insideFunctionSplit[1])
        if insideFunctionSplit[0][:-2] != '':
            multiCoefficient = int(insideFunctionSplit[0][:-2])
    else:
        addCoefficient = int(insideFunctionSplit[0])
        if insideFunctionSplit[1][:-2] != '':
            multiCoefficient = int(insideFunctionSplit[1][:-2])

xValues = np.linspace(-12 * np.pi, 12 * np.pi, 1000)
if mainFunction[0] == 'c':
    trigValues = np.cos(xValues * multiCoefficient + addCoefficient)
elif mainFunction[0] == 't':
    trigValues = np.tan(xValues * multiCoefficient + addCoefficient)
elif mainFunction[0] == 'l':
    trigValues = np.log2(xValues * multiCoefficient + addCoefficient)
else:
    trigValues = np.sin(xValues * multiCoefficient + addCoefficient)

trigValues *= multiplier
trigValues += yShift

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(xValues, trigValues, alpha=0.7, color="#A14491", linestyle="--", linewidth=4)
plt.subplot(2,2,2)
plt.plot(xValues, trigValues, alpha=0.7, color="#A14491", linestyle="--", linewidth=3)
plt.subplot(2,2,3)
plt.plot(xValues, trigValues, alpha=0.7, color="#A14491", linestyle="--", linewidth=2)
plt.figure(2)
plt.ylim(-5,5)
plt.plot(xValues, trigValues,alpha=0.2,  color="#519441", linestyle="-", linewidth=1)
plt.plot(xValues, trigValues, alpha=0.2, color="#519441", linestyle="-", linewidth=1)

plt.show()