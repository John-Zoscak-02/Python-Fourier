class Vector:

    def __init__(self):
        self.real = 0
        self.imaginary = 0
        self.complex = 0 + 0j

    def setComponents(complex):
        self.real = complex.real
        self.imaginary = complex.imag
        self.complex = complex.conjugate()

    def resetComponents(self):
        self.real = 0
        self.imaginary = 0
        self.complex = 0 + 0j

    def print(self):
        print("Real Component: %d" % self.real)
        print("Imaginary Component: %d" % self.imaginary)
        print("Real Component: %d" % self.complex)

