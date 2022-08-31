class Vector:
    def __init__(self):
        self.real = 0
        self.imaginary = 0
        self.complex = 0 + 0j

    def setComponents(self, complex):
        self.real = complex.real
        self.imaginary = complex.imag
        self.complex = complex

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
        print("     Real Component: %f" % self.real)
        print("     Imaginary Component: %f" % self.imaginary)
        print("     Complex: %s" % self.complex)
        print()

