class Vector:
    import numpy as np
    import scipy as sci

    def __init__(self):
        self.real = 0
        self.imaginary = 0
        self.complex = 0 + 0j
        self.num = 0

    def setComponents(self, complex, number):
        self.real = complex.real
        self.imaginary = complex.imag
        self.complex = complex.conjugate()
        self.num = number

    def getReal(self):
        return self.real

    def getImaginary(self):
        return self.imaginary

    def getComplex(self):
        return self.complex

    def resetComponents(self):
        self.real = 0
        self.imaginary = 0
        self.complex = 0 + 0j
        self.num = 0

    def print(self):
        print("Real Component: %d" % self.real)
        print("Imaginary Component: %d" % self.imaginary)
        print("Real Component: %d" % self.complex)


class Calculator:

    def __init__(self, vector):
        self.vector = vector

    @staticmethod
    def calculateConstant(n):
        import quadpy
        import cmath

        def f(t):
            return cmath.e ** (-n * 2 * cmath.pi * t * complex(0, 1))

        result = quadpy.quad(f, 0, 1)
        return result[0]

    def calculateFrequency(self, time):
        import math
        return Calculator.calculateConstant(self.vector.num) * math.e ** (self.vector.num * 2 * math.pi * 1j * time)
