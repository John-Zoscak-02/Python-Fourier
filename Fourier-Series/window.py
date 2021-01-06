import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation
import cmath
from Function import Function, Calculator, BaseFunction

filename_base_function = ""
range_of_n = range(-150, 150)

plot.style.use('dark_background')
fig = plot.figure()
ax = plot.axes(xlim=(0, 110), ylim=(0, 110))
plot.gca().invert_yaxis()
line, = ax.plot([], [], lw=2)
xdata, ydata =[], []

def init():
    line.set_data([], [])
    return line,


def animate(t):
    print("Time: %f" % t)
    vector_sum = 0
    for function in functions:
        function.update(t)
        vector_sum += function.vector.getComplex()

    print("     %s" % vector_sum)
    x = vector_sum.real
    y = vector_sum.imag
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,


if __name__ == "__main__":
    global functions
    functions = []
    base_function = BaseFunction(filename_base_function)
    for n in range_of_n:
        functions.append(Function(Calculator.calculate_constant(n, base_function), n))

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, 1.01, 0.01), interval=20, blit=True, repeat=False)
    plot.show()



