import math
import scipy.integrate as sci
import scipy as sc
import cmath
import numpy as np
import quadpy
#val = sci.quad(lambda t: cmath.e ** (-2 * cmath.pi * t * complex(0, 1)), 0, 1)[0].real
def f(t):
    return cmath.e ** (4 * cmath.pi * t * complex(0, 1))


result = quadpy.quad(f, 0, 1)
print(result[0])

other = result[0] * cmath.e ** (-2 * cmath.pi * 2)
