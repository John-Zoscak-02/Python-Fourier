class Vector:

    import numpy as np
    import scipy as sci

    def __init__(self):
        self.real = 0
        self.imaginary = 0
        self.complex = 0 + 0j

    def setComponents(self, complex):
        self.real = complex.real
        self.imaginary = complex.imag
        self.complex = complex.conjugate()

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

    def print(self):
        print("Real Component: %d" % self.real)
        print("Imaginary Component: %d" % self.imaginary)
        print("Real Component: %d" % self.complex)

        class Calculator:

            def __init__(self, vector):
                self.vector = vector

            @staticmethod
            def calculateConstant(n):
                import math
                import scipy.integrate as sci
                import numpy as np
                return sci.quad(lambda t: math.e ** (-n * 2 * math.pi * 1j * t), 0, 1)
