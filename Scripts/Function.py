from Vector import Vector
import math

from svg.path import parse_path
from svg.path.path import Path
from xml.dom import minidom

class BaseFunction:
    def __init__(self, setname):
        # self.file = open("Sets/%s" % setname)
        # coordinatestrings = self.file.read().split("\n")
        # self.coordinates = []
        # for str in coordinatestrings:
        #     x_y = str.split(" ")
        #     self.coordinates.append((float(x_y[0]), float(x_y[1])))
        # self.numentries = len(self.coordinates)
        # print(coordinatestrings)
        # print(self.coordinates)

        self.file = minidom.parse('Sets/math-pi.svg')
        self.path_strings = [path.getAttribute('d') for path
                        in self.file.getElementsByTagName('path')]
        self.file.unlink()

        self.path = Path()
        for path_string in self.path_strings:
            self.path.append(parse_path(path_string))



    def print(self):
        print("Coordinates: %s" % self.coordinates)
        print("Num of Entries: %d" % self.numentries)

    def access(self, time):
        # loc = int (time * (self.numentries - 1))
        # return complex number representation of location based off of loc
        # loc can be understood as the "t" within a parametric equation. Finding the parametric equation that represents x and y
        # intra_coordinate_loc = (time * (self.numentries - 1)) % (self.numentries - 1)
        # ypara = (self.coordinates[int(intra_coordinate_loc) + 1][1] - self.coordinates[int(intra_coordinate_loc)][1])
        # y = ((loc % 1) * ypara) + self.coordinates[int(intra_coordinate_loc)][1]
        # xpara = (self.coordinates[int(intra_coordinate_loc) + 1][0] - self.coordinates[int(intra_coordinate_loc)][0])
        # x = ((loc % 1) * xpara) + self.coordinates[int(intra_coordinate_loc)][0]
        # return x + (y * 1j)
        return self.path.point(time)





class Function:
    def __init__(self, coef, n):
        self.coef = coef
        self.n = n
        self.vector = Vector()
        self.vector.setComponents(coef)


    def update(self, time):
        self.vector.setComponents(Calculator.calculate_vector(self, time))

    def print(self):
        print("({:.2f})e^(({:.2f})*2(PI)it)".format(self.coef, self.n))


class Calculator:

    def __init__(self, vector):
        self.vector = vector

    @staticmethod
    def calculate_constant(n, basefunc):
        integration = 0
        for i in range(0, 1001):
            t = i / 1000
            integration += basefunc.access(t)*(math.e ** (-n * 2 * math.pi * 1j * t))*0.001
        return integration
        #return sci.quad(lambda t: math.e ** (-n * 2 * math.pi * 1j * t), 0, 1)

    @staticmethod
    def calculate_vector(function, time):
        complex_vector = function.coef * (math.e ** (function.n * (2 * math.pi) * 1j * time))
        return complex_vector



