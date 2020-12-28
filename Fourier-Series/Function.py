from Vector import Vector
import math


class Function:
    def __init__(self, coef, n):
        self.coef = coef
        self.n = n
        self.vector = Vector()
        self.vector.setComponents(coef)

    def update(self, time):
        self.vector.setComponents(Calculator.calculateVector(self, time))

    def print(self):
        print("({:.2f})e^(({:.2f})*2(PI)it)".format(self.coef, self.n))


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
        complexVector = function.coef * (math.e ** (function.n * (2 * math.pi) * 1j * time))
        return complexVector



