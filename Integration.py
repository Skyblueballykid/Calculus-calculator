from Derivation import *

def integral(startingx, endingx, numrectangles):
    width = (float(endingx) - float(startingx))/numrectangles
    runningSum = 0
    for i in range(numrectangles):
        height = f(startingx + i*width)
        area = height * width
        runningSum += area
    return runningSum