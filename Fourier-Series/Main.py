from Function import Calculator
from Function import Function
import math

time = 0
functions = []

def main():
    global time
    for function in functions :
        v = Calculator.calculateVector(function, time)
        #send v to GUI
    time += 1


if __name__ == "__main__":
    # global functions
    # # initialize all the functions
    # while True:
    #     main()

    function = Function(2.5, 1)

    function.print()

    for num in range(0, 1001):
        t = (num / 1000)
        print(t)
        function.update(t)
        function.vector.print()


