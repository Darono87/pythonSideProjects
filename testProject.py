import os
import sys
import random


class Stack:
    stackContainer = []

    def __init__(self):
        self.stackContainer = []

    def putOnStack(self, item):
        self.stackContainer.append(item)

    def getFromStack(self, remove):
        if len(self.stackContainer) < 1:
            return None
        retVal = self.stackContainer[-1]
        if remove:
            del self.stackContainer[-1]
        return retVal

    def getUntil(self, symbol, remUntil):
        toGoOut = ""
        while len(self.stackContainer) > 0 and self.stackContainer[-1] != symbol:
            toGoOut += self.getFromStack(True)
        if remUntil:
            self.getFromStack(True)
        return toGoOut
    def lookForUntil(self, until, forWhat):
        for x in range(0,len(self.stackContainer)):
            y = len(self.stackContainer) - 1 - x
            if self.stackContainer[y]==until:
                break
            if self.stackContainer[y]==forWhat:
                return True
        return False


print("Please give me an equation in standard form so I'll give you the ONP form:")
equation = input()
finalExpression = ""

myStack = Stack()
for x in range(0, len(equation)):
    if equation[x].isalnum():
        finalExpression += equation[x]
        continue
    if equation[x] == '(':
        myStack.putOnStack('(')
    if equation[x] == ')':
        finalExpression += myStack.getUntil('(', True)
    if equation[x] == "+":
        if myStack.lookForUntil('(', '*'):
            finalExpression += myStack.getUntil('(', False)
        myStack.putOnStack('+')
    if equation[x] == '*':
        myStack.putOnStack('*')

finalExpression += myStack.getUntil('(', False)

print(finalExpression)
