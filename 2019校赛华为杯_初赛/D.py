#@Time  : 2019/5/18 12:29
#@Author: Root
#@File  : D.py

import sys


def solve():
    n = int(input())
    lines = [input() for i in range(n)]

    xs = [0] * (n + 1)
    ys = [0] * (n + 1)

    for i, line in enumerate(lines) :
        t = line.split()
        xs[i + 1] = int(t[0])
        ys[i + 1] = int(t[1])

    minSteps = sys.maxsize


    def setMinXSteps(k: int, xS, xPotentials, yS, yPotentials) :
        nonlocal currentSteps
        nonlocal minSteps
        if k > n:

            def setMinYSteps(h: int, yS, yPotentials):
                nonlocal minSteps
                nonlocal currentSteps
                if h > n:
                    if currentSteps < minSteps:
                        minSteps = currentSteps
                    return

                originalYDecision = yS[h]
                if originalYDecision in yPotentials:
                    yPotentials.remove(originalYDecision)
                    setMinYSteps(h + 1, yS, yPotentials)
                    yList = list(yPotentials)
                    yPotentials.add(originalYDecision)
                    currentSteps += 1
                    for yDecision in yList:
                        yS[h] = yDecision
                        yPotentials.remove(yDecision)
                        setMinYSteps(h + 1, yS, yPotentials)
                        yPotentials.add(yDecision)
                    yS[h] = originalYDecision
                    currentSteps -= 1
                else:
                    yList = list(yPotentials)
                    currentSteps += 1
                    for yDecision in yList:
                        yS[h] = yDecision
                        yPotentials.remove(yDecision)
                        setMinYSteps(h + 1, yS, yPotentials)
                        yPotentials.add(yDecision)
                    yS[h] = originalYDecision
                    currentSteps -= 1

            setMinYSteps(1, yS, yPotentials)
            return

        # 先考虑当前状态
        originalXDecision = xS[k]
        if originalXDecision in xPotentials:
            xPotentials.remove(originalXDecision)
            setMinXSteps(k + 1, xS, xPotentials, yS, yPotentials)

            xList = list(xPotentials)

            xPotentials.add(originalXDecision)

            currentSteps += 1
            for xDecision in xList:
                xS[k] = xDecision
                xPotentials.remove(xDecision)
                setMinXSteps(k + 1, xS, xPotentials, yS, yPotentials)
                xPotentials.add(xDecision)
            xS[k] = originalXDecision
            currentSteps -= 1
        else:
            xList = list(xPotentials)
            currentSteps += 1
            for xDecision in xList:
                xS[k] = xDecision
                xPotentials.remove(xDecision)
                setMinXSteps(k + 1, xS, xPotentials, yS, yPotentials)
                xPotentials.add(xDecision)
            xS[k] = originalXDecision
            currentSteps -= 1

    currentSteps = 0
    tempX = xs.copy()
    tempY = ys.copy()
    tempPotentialX = set(range(1, n + 1))
    tempPotentialY = set(range(1, n + 1))
    setMinXSteps(1, tempX, tempPotentialX, tempY, tempPotentialY)

    currentSteps = 0
    tempX = xs.copy()
    tempY = ys.copy()
    tempPotentialX = set(range(1, n + 1))
    tempPotentialY = set(range(1, n + 1))
    setMinXSteps(1, tempY, tempPotentialY, tempX, tempPotentialX)
    return minSteps


if __name__ == "__main__" :

    T = int(input())
    for i in range(T) :
        print(solve())



