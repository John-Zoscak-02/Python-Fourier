import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation
import cmath

plot.style.use('dark_background')

fig = plot.figure()
ax = plot.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,


xdata, ydata =[], []

def animate(t):
    x = 10 * (0.5 + np.cos(3 * t)) * np.cos(t)
    y = 10 * (0.5 + np.cos(3 * t)) * np.sin(t)
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, 2 * cmath.pi, 0.01), interval=20, blit=True)
plot.show()
