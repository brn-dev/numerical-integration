import numerical_integration
from integration_rules import rectangle_rule
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


class Interval:
    def __init__(self, start, end, width, num_slices, slice_width):
        self.start = start
        self.end = end
        self.width = width
        self.num_slices = num_slices
        self.slice_width = slice_width

        
def create_interval(start, end, num_slices):
    width = end - start
    return Interval(start, end, width, num_slices, width / num_slices)


def f(x):
    return -(3 * x**4 - 2 * x**3 + 9 * x**2 + 5 * x + 4)


def plot_rectangle_rule_start(start=-5, end=5, num_slices=10, graph_resolution=500):
    interval = create_interval(start, end, num_slices)
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)
    
    x_rectangle = np.linspace(interval.start, interval.end, interval.num_slices, endpoint=False)
    y_rectangle = f(x_rectangle)
    
    plot_rectangle_rule(interval, x, y, x_rectangle, y_rectangle)

    
def plot_rectangle_rule_mid(start=-5, end=5, num_slices=10, graph_resolution=500):
    interval = create_interval(start, end, num_slices)
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)
    
    x_rectangle = np.linspace(interval.start, interval.end, interval.num_slices, endpoint=False)
    y_rectangle = f(x_rectangle + interval.slice_width / 2)
    
    plot_rectangle_rule(interval, x, y, x_rectangle, y_rectangle)
    
    
def plot_rectangle_rule_end(start=-5, end=5, num_slices=10, graph_resolution=500):
    interval = create_interval(start, end, num_slices)
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)
    
    x_rectangle = np.linspace(interval.start, interval.end, interval.num_slices, endpoint=False)
    y_rectangle = f(x_rectangle + interval.slice_width)
    
    plot_rectangle_rule(interval, x, y, x_rectangle, y_rectangle)
    

def create_color_scale(num_shades, start_color, end_color):
    colors = []
    r = np.linspace(start_color[0], end_color[0], num=num_shades, endpoint=True)
    g = np.linspace(start_color[1], end_color[1], num=num_shades, endpoint=True)
    b = np.linspace(start_color[2], end_color[2], num=num_shades, endpoint=True)
    
    for i in range(num_shades):
        color = (r[i], g[i], b[i])
        colors.append(color)
    
    return colors


def plot_rectangle_rule(interval, x, y, x_rectangle, y_rectangle):
    fig, ax = plt.subplots(figsize=(20, 12))
    ax.plot(x, y, color=(1, 0, 0), linewidth=4)
    color_scale = create_color_scale(interval.num_slices, (0, 0, 1), (0, 1, 0.6))
    
    for i in range(interval.num_slices):
        rectangle_bottom_left = (x_rectangle[i], 0)
        rectangle_height = y_rectangle[i]
        ax.add_patch(
            Rectangle(rectangle_bottom_left, interval.slice_width, rectangle_height,
                 facecolor=color_scale[i],
                 fill=True,
                 lw=1)
        )


def plot_trapezoidal_rule(start=-5, end=5, num_slices=10, graph_resolution=500):
    interval = create_interval(start, end, num_slices)
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)
    
    x_trapezoid = np.linspace(interval.start, interval.end, interval.num_slices + 1, endpoint=True)
    y_trapezoid = f(x_trapezoid)
    
    color_scale = create_color_scale(interval.num_slices + 1, (0, 0, 1), (0, 1, 0.6))
    fig, ax = plt.subplots(figsize=(20, 12))
    ax.plot(x, y, color=(1, 0, 0), linewidth=4)
    
    for i in range(interval.num_slices):
        ax.fill_between(x_trapezoid[i: i+2], 0, y_trapezoid[i: i+2], facecolor=color_scale[i], edgecolor=color_scale[i])

class Parabola:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    
    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c


def parabola_from_points(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    a = ( (y3 - y1) / (x3 - x1) ) - ( (y2 - y1) / (x2 - x1) )
    a = a / (x3 - x2)
    b = ( ( y2 - y1 ) / ( x2 - x1 ) ) - a * (x2 + x1)
    c = y1 - a * x1**2 - b * x1
    
    return Parabola(a, b, c)

                                                       
def plot_barrel_rule(start=-5, end=5, num_slices=1, graph_resolution=500, parabola_resolution=100):
    interval = create_interval(start, end, num_slices)
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)
    x_slices = np.linspace(interval.start, interval.end, num_slices + 1, endpoint=True)
    
    fig, ax = plt.subplots(figsize=(20, 12))
    ax.plot(x, y, color=(1, 0, 0), linewidth=4)
    
    for i in range(len(x_slices) - 1):
        a = x_slices[i]
        b = x_slices[i + 1]
        mid = (a + b) / 2
        p1 = (a, f(a))
        p2 = (mid, f(mid))
        p3 = (b, f(b))
        parabola = parabola_from_points(p1, p2, p3) 
        x_parabola = np.linspace(a, b, parabola_resolution, endpoint=True)
        y_parabola = parabola(x_parabola)
        ax.plot(x_parabola, y_parabola, color=(1, 0.647058823529, 0), linewidth=4)
    
    
    