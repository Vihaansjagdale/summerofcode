import math, os

def convertToCelsius(tempInFarenheit):
    inCelsuis = ((tempInFarenheit - 32) * (5/9))
    return inCelsuis
def convertTofarenheit(tempInCelcius):
    inFarenheit=(tempInCelcius-32) * (5 / 9)
    return inFarenheit

print(convertTofarenheit(0))
print(convertToCelsius(180))

