from Function import Function, Calculator, BaseFunction

import math
filename_base_function = "star"
range_of_n = range(-50, 50)

def main():
    global iteration
    print("Time: %f" % (iteration / 1000))
    vector_sum = 0
    for function in functions:
        function.update(iteration/1000)
        vector_sum += function.vector.getComplex()
    iteration += 1
    print("     %s" % vector_sum)
    pass


if __name__ == "__main__":
    functions = []
    base_function = BaseFunction(filename_base_function)
    for n in range_of_n:
        functions.append(Function(Calculator.calculate_constant(n, base_function), n))

    global iteration
    iteration = 0
    while iteration < 1000:
        main()

    # function = Function(2.5, 1)
    # function.print()
    # for num in range(0, 1001):
    #     t = (num / 1000)
    #     print(t)
    #     function.update(t)
    #     function.vector.print()