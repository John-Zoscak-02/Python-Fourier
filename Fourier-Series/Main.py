from Function import Calculator

time = 0
functions = []

def main():
    global time
    for function in functions :
        v = Calculator.calculateVector(function, time)
        #send v to GUI
    time += 1


if __name__ == "__main__":
    global functions
    # initialize all the functions
    while True:
        main()