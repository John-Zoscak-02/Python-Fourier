from Vector import Vector


class Function:

    def __init__(self, coef, n):
        self.coef = coef
        self.n = n
        self.vector = Vector()

    def setFunction(self, coef, n):
        self.coef = coef
        self.n = n

    def print(self):
        print("%de^(%d*2(pi)it)" % (self.coef, self.n))

class Calculator:

    def __init__(self, vector):
        self.vector = vector

    @staticmethod
    def calculateConstant(n):
        import math
        import scipy.integrate as sci
        import numpy as np
        return sci.quad(lambda t: math.e ** (-n * 2 * math.pi * 1j * t), 0, 1)

    @staticmethod
    def calculateVector(function, time):
        #calculate a vector given a function and a time
        return Vector()

