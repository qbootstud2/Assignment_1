from math import floor
import numpy as np
from numpy.typing import NDArray
from src.utils import get_labels_info


def generate_empty_canvas(height: int, width: int, use_grid: bool = True) -> NDArray:
    """ This method initializes the plot canvas """

    # Initialize the canvas array
    canvas = np.empty((height, width), dtype="str")

    # Fill corners
    canvas[0, 0], canvas[0, -1],  canvas[-1, 0], canvas[-1, -1] = '+', '+', '+', '+'

    # Fill borders
    canvas[1:-1, 0], canvas[1:-1, -1] = '|', '|'  # vertical
    canvas[0, 1:-1], canvas[-1, 1:-1] = '-', '-'  # horizontal

    # Add grid or leave blank
    if use_grid:
        canvas[1:-1, 1:-1] = '·'
    else:
        canvas[1:-1, 1:-1] = ' '

    return canvas


def add_x_axis(x: list, x_size: int, legend: str = ' ') -> NDArray:
    """ This method generates the main canvas for the x axis and adds the labels and the legend """

    assert len(legend) <= x_size

    # Find min and max values and length of the strings that will be displayed on x axis labels
    x_min, x_max, length_x_min, length_x_max = get_labels_info(x)

    # Fill margin
    x_axis = np.empty((1, x_size), dtype="str")
    x_axis[:] = ' '
    test_spaces = floor((x_size - len(legend)) / 2)

    for elem in range(len(legend)):
        x_axis[0, test_spaces + elem] = list(legend)[elem]

    x_axis[0, :length_x_min] = [char for char in str(x_min)]
    x_axis[0, -length_x_max:] = [char for char in str(x_max)]

    return x_axis


def add_y_axis(y: list, y_size: int) -> NDArray:
    """ This method generates the main canvas for the y axis and adds the labels """

    # Find min and max values and length of the strings that will be displayed on y axis labels
    y_min, y_max, length_y_min, length_y_max = get_labels_info(y)

    # Fill margin
    y_axis = np.empty((y_size, max(length_y_min, length_y_max)), dtype="str")
    y_axis[:] = ' '
    y_axis[-1, :length_y_min] = [char for char in str(y_min)]
    y_axis[0, :length_y_max] = [char for char in str(y_max)]

    return y_axis


def add_title(x_size: int, title: str = ' ') -> NDArray:
    """ This method generates the main canvas for the title and adds the title """

    assert len(title) <= x_size

    # Fill margin
    title_axis = np.empty((1, x_size), dtype="str")
    title_axis[:] = ' '
    test_spaces = floor((x_size - len(title)) / 2)

    for elem in range(len(title)):
        title_axis[0, test_spaces + elem] = list(title)[elem]

    return title_axis
