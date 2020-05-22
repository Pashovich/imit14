import random
import matplotlib.pyplot as plt
import math


def generate(answers):
    rand = random.uniform(0, 1)
    for inx, item in enumerate(answers):
        rand = rand - answers[inx]
        if rand <= 0:
            return inx

def generateProbasRandom(n):
    tempList = []
    for _ in range(n-1):
        prob = round(random.uniform(0, 1 - sum(tempList)),5)
        tempList.append(prob)
    tempList.append(1-sum(tempList))
    return tempList
    
    
def calcMathAverege(xList, pList):
    return sum([ x*p for x,p in zip(xList,pList)])

def calcDispersion(xList, pList):
    xListSquared = [item * item for item in xList]
    mathAverege = calcMathAverege(xList,pList)
    dispersion = calcMathAverege(xListSquared,pList) - mathAverege*mathAverege
    return dispersion

if __name__ == "__main__":

    N = int(input('Number of examples :  '))
    n = int(input('n :  '))
    probabilities = generateProbasRandom(n)
    y_pos = range(1,n+1)
    relust = [0]*n

    mathAverege = calcMathAverege(y_pos,probabilities)
    dispersion = calcDispersion(y_pos,probabilities)


    for i in range(N):
        answ = generate(probabilities)
        if answ !=-1:
            relust[answ]+=1
    
    frequency = [item/N for item in relust]

    plt.bar(y_pos,frequency, align='center', alpha = 0.5)
    plt.xticks(y_pos, y_pos) 
    mathAveregeE = calcMathAverege(frequency,y_pos)
    dispersionE = calcDispersion(y_pos, frequency)
    mathError = abs(mathAveregeE - mathAverege)
    dispersionError = abs(dispersionE - dispersion)
    print(mathError, dispersionError)
    print(sum([(n*n/(N*p)) for n, p in zip(relust, probabilities)]) - N)

    plt.show()