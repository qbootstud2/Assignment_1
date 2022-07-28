import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from src.canvas_template import generate_empty_canvas, add_x_axis, add_y_axis, add_title
from src.utils import print_chart, normalize_data, scale_data, get_labels_info


def plot_data(x: list, y: list, canvas: NDArray, use_grid: bool = False) -> NDArray:
    """ This method plots the input data in the canvas """

    # Determine max height
    y_max = len(canvas) - 1

    # Set origin at the bottom of the y axis
    y = [y_max - y_cord for y_cord in y]

    # Plot data
    if use_grid:
        for i, j in zip(x, y):
            canvas[j, i] = '*'
    else:
        for i, j in zip(x, y):
            canvas[j, i] = '•'

    return canvas


def make_plot(x: list,
              y: list,
              display_grid: bool = False,
              height: int = 15,
              width: int = 100,
              legend: str = ' ',
              add_title_option: bool = True,
              title: str = ' ') -> None:
    """ This method generates an empty canvas, adds the data and the labels, and makes the plot """

    assert len(x) == len(y)

    # Generate canvas
    empty_canvas = generate_empty_canvas(height, width, use_grid=display_grid)

    # Normalize and scaled the data
    x_normalized, y_normalized = normalize_data(x, y)
    x_scaled, y_scaled = scale_data(x_normalized, y_normalized, height=height, width=width)

    # Plot data
    canvas = plot_data(x_scaled, y_scaled, empty_canvas, use_grid=display_grid)

    # Find length of the strings that will be displayed on y axis labels
    _, _, length_y_min, length_y_max = get_labels_info(y)

    # Generate y axis canvas
    y_margin = np.empty((height, 1), dtype="str")
    y_margin[:] = ' '
    y_axis_canvas = np.hstack((add_y_axis(y, height), y_margin))

    # Generate x axis canvas
    x_margin = np.empty((1, max(length_y_min, length_y_max) + 1), dtype="str")
    x_margin[:] = ' '
    x_axis_canvas = np.hstack((x_margin, add_x_axis(x, width, legend)))

    # Generate title canvas
    if add_title_option:
        title_margin = np.empty((1, max(length_y_min, length_y_max) + 1), dtype="str")
        title_margin[:] = ' '
        title_canvas = np.hstack((title_margin, add_title(width, title)))

    # Add y axis to the canvas
    canvas_with_y_axis = np.hstack((y_axis_canvas, canvas))

    # Add x axis to the canvas
    canvas_with_x_axis = np.vstack((canvas_with_y_axis, x_axis_canvas))

    # Add title to the canvas
    if add_title_option:
        filled_canvas = np.vstack((title_canvas, canvas_with_x_axis))
    else:
        filled_canvas = canvas_with_x_axis

    # Print the final plot
    print_chart(filled_canvas)


def plot_check(x: list,
               y: list,
               display_grid: bool = False,
               height: int = 15,
               width: int = 100,
               legend: str = ' ',
               add_title_option: bool = True,
               title: str = ' ') -> None:
    """ This method generates the plot using matplotlib """

    # Normalize and scaled the data
    x_normalized, y_normalized = normalize_data(x, y)
    x_scaled, y_scaled = scale_data(x_normalized, y_normalized, height=height, width=width)

    # Make plot
    plt.scatter(x_scaled, y_scaled)
    plt.xlabel(legend)

    if add_title_option:
        plt.title(title)
    if display_grid:
        plt.grid()

    plt.savefig("data/matplotlib_check.pdf", bbox_inches='tight', pad_inches=0)
    plt.show()
