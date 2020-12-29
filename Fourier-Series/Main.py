from Function import Function, Calculator, BaseFunction

import math
filename_base_function = "star"
range_of_n = range(-10, 10)

def main():
    global time
    print("Iteration: %f" % time)
    for function in functions:
        function.update(time)
        function.vector.print()
    time += 1
    pass


if __name__ == "__main__":
    functions = []
    base_function = BaseFunction(filename_base_function)
    for n in range_of_n:
        functions.append(Function(Calculator.calculate_constant(n, base_function), n))

    global time
    time = 0
    while time < 10:
        main()

    # function = Function(2.5, 1)
    # function.print()
    # for num in range(0, 1001):
    #     t = (num / 1000)
    #     print(t)
    #     function.update(t)
    #     function.vector.print()


