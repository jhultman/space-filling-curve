import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


def x(t): return np.square(np.cos(t))
def y(t): return np.square(np.cos(np.sqrt(2) * t))
def z(t): return np.square(np.cos(np.sqrt(3) * t))


def update(i, xdata, ydata, zdata, line):
    i = i ** 2
    line.set_data(xdata[:i], ydata[:i])
    line.set_3d_properties(zdata[:i], 'z')
    return line,


def init_plot(fig):
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()
    
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    
    fig.suptitle('Space-filling curve', family='monospace')
    return ax.plot([], [], [], animated=True, color='grey')


def get_data(T=500, dt=0.1):
    t = np.arange(0, T, dt)
    return x(t), y(t), z(t)


def plot_2D(T=200, dt=0.1):
    t = np.arange(0, T, dt)
    fig, ax = plt.subplots()
    ax.plot(x(t), y(t))
    ax.set_xlabel('x')
    ax.set_xlabel('y')
    fig.suptitle('Space-filling curve', family='monospace')
    plt.show()


def main():
    fig = plt.figure()
    line, = init_plot(fig)
    ani = FuncAnimation(fig, func=update, frames=100, 
        fargs=(*get_data(), line), blit=True)
    
    ani.save('space_filling.gif', dpi=80, writer='imagemagick')


if __name__ == '__main__':
    main()
