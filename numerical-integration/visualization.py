import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

from numerical_integration import NumericalIntegration
from integration_rules.rectangle_rule import rectangle_rule_start, rectangle_rule_midpoint, rectangle_rule_end
from integration_rules.trapezoid_rule import trapezoid_rule
from integration_rules.barrel_rule import barrel_rule_1_3

numerical_integration_rectangle_start = NumericalIntegration(rectangle_rule_start)
numerical_integration_rectangle_midpoint = NumericalIntegration(rectangle_rule_midpoint)
numerical_integration_rectangle_end = NumericalIntegration(rectangle_rule_end)

numerical_integration_trapezoid = NumericalIntegration(trapezoid_rule)

numerical_integration_barrel = NumericalIntegration(barrel_rule_1_3)

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


def create_grid(ax):
    # create gray background grid
    ax.grid(b=True, which='major', color='#666666', linestyle='-')
    
    # create the cartesian coordinate system lines with origin (0, 0)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set(linewidth=2)
    ax.spines['left'].set(linewidth=2)
    
    # disable unused spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # create the arrow markers
    ax.plot((1), (0), marker=">", ms=8, color='black', transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), marker="^", ms=8, color='black', transform=ax.get_xaxis_transform(), clip_on=False)


def plot_rectangle_rule_start(f, start=-5, end=5, num_slices=10, graph_resolution=500):
    interval = create_interval(start, end, num_slices)
    
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)
    
    x_rectangle = np.linspace(interval.start, interval.end, interval.num_slices, endpoint=False)
    y_rectangle = f(x_rectangle)

    plot_rectangle_rule(f, interval, x, y, x_rectangle, y_rectangle, 'start')


def plot_rectangle_rule_mid(f, start=-5, end=5, num_slices=10, graph_resolution=500):
    interval = create_interval(start, end, num_slices)
    
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)

    x_rectangle = np.linspace(interval.start, interval.end, interval.num_slices, endpoint=False)
    y_rectangle = f(x_rectangle + interval.slice_width / 2)

    plot_rectangle_rule(f, interval, x, y, x_rectangle, y_rectangle, 'midpoint')


def plot_rectangle_rule_end(f, start=-5, end=5, num_slices=10, graph_resolution=500):
    interval = create_interval(start, end, num_slices)
    
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)

    x_rectangle = np.linspace(interval.start, interval.end, interval.num_slices, endpoint=False)
    y_rectangle = f(x_rectangle + interval.slice_width)

    plot_rectangle_rule(f, interval, x, y, x_rectangle, y_rectangle, 'end')


def create_color_scale(num_shades, start_color, end_color):
    colors = []
    
    r = np.linspace(start_color[0], end_color[0], num=num_shades, endpoint=True)
    g = np.linspace(start_color[1], end_color[1], num=num_shades, endpoint=True)
    b = np.linspace(start_color[2], end_color[2], num=num_shades, endpoint=True)

    for i in range(num_shades):
        color = (r[i], g[i], b[i])
        colors.append(color)

    return colors


def plot_rectangle_rule(f, interval, x, y, x_rectangle, y_rectangle, rectangle_type):
    if rectangle_type == 'start':
        area = numerical_integration_rectangle_start.approximate_integration(
            f, interval.start, interval.end, interval.num_slices
        )
    elif rectangle_type == 'midpoint':
        area = numerical_integration_rectangle_midpoint.approximate_integration(
            f, interval.start, interval.end, interval.num_slices
        )
    elif rectangle_type == 'end':
        area = numerical_integration_rectangle_end.approximate_integration(
            f, interval.start, interval.end, interval.num_slices
        )
    else:
        raise ValueError('rectangle_type does not have a valid value!')

    fig, ax = plt.subplots(figsize=(20, 12))
    ax.title.set_text(f'Numerical integration using the rectangle rule ({rectangle_type}) with area {area}')
    create_grid(ax)
    
    color_scale = create_color_scale(interval.num_slices, (0, 0, 1), (0, 1, 0.6))

    # draw all rectangles
    for i in range(interval.num_slices):
        rectangle_bottom_left = (x_rectangle[i], 0)
        rectangle_height = y_rectangle[i]
        ax.add_patch(
            Rectangle(rectangle_bottom_left, interval.slice_width, rectangle_height,
                      facecolor=color_scale[i],
                      fill=True,
                      lw=1)
        )
    
    # draw graph
    ax.plot(x, y, color=(1, 0, 0), linewidth=4)


def plot_trapezoidal_rule(f, start=-5, end=5, num_slices=10, graph_resolution=500):
    interval = create_interval(start, end, num_slices)
    
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)

    x_trapezoid = np.linspace(interval.start, interval.end, interval.num_slices + 1, endpoint=True)
    y_trapezoid = f(x_trapezoid)

    area = numerical_integration_trapezoid.approximate_integration(f, start, end, num_slices)

    color_scale = create_color_scale(interval.num_slices + 1, (0, 0, 1), (0, 1, 0.6))
    fig, ax = plt.subplots(figsize=(20, 12))
    ax.title.set_text(f'Numerical integration using the trapezoidal rule with area {area}')
    create_grid(ax)
    
    # draw all trapezoids
    for i in range(interval.num_slices):
        ax.fill_between(x_trapezoid[i: i + 2], 0, y_trapezoid[i: i + 2], facecolor=color_scale[i],
                        edgecolor=color_scale[i])
    
    # draw graph
    ax.plot(x, y, color=(1, 0, 0), linewidth=4)


class Parabola:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


def parabola_from_points(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    a = ((y3 - y1) / (x3 - x1)) - ((y2 - y1) / (x2 - x1))
    a = a / (x3 - x2)
    b = ((y2 - y1) / (x2 - x1)) - a * (x2 + x1)
    c = y1 - a * x1 ** 2 - b * x1

    return Parabola(a, b, c)


def plot_barrel_rule(
        f,
        start=-5,
        end=5,
        num_slices=1,
        graph_resolution=500,
        parabola_resolution=100
):
    interval = create_interval(start, end, num_slices)
    
    x = np.linspace(interval.start, interval.end, graph_resolution)
    y = f(x)
    
    x_slices = np.linspace(interval.start, interval.end, num_slices + 1, endpoint=True)

    area = numerical_integration_barrel.approximate_integration(f, start, end, num_slices)

    fig, ax = plt.subplots(figsize=(20, 12))
    ax.title.set_text(f'Numerical integration using the barrel rule with area {area}')
    create_grid(ax)

    color_scale = create_color_scale(interval.num_slices, (0, 0, 1), (0, 1, 0.6))
    
    # draw all parabolas
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
        ax.plot(x_parabola, y_parabola, color=color_scale[i], linewidth=2)
        ax.fill_between(x_parabola, 0, y_parabola, facecolor=color_scale[i],
                        edgecolor=color_scale[i])
    
    # draw graph
    ax.plot(x, y, color=(1, 0, 0), linewidth=4)
