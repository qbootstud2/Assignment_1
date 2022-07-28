from math import floor
from numpy.typing import NDArray


def print_chart(canvas: NDArray) -> None:
    """ This method prints the plot canvas """

    for row in canvas:
        print("".join(row))


def normalize_data(x: list, y: list) -> (list, list):
    """ This method applies min-max normalization to the input coordinates """

    x_normalized = [(i - min(x)) / (max(x) - min(x)) for i in x]
    y_normalized = [(j - min(y)) / (max(y) - min(y)) for j in y]

    return x_normalized, y_normalized


def scale_data(x: list, y: list, height: int, width: int) -> (list, list):
    """ This method scales the input data by the width and height of the canvas """

    x_scaled = [floor(i * (width - 1)) for i in x]
    y_scaled = [floor(i * (height - 1)) for i in y]

    return x_scaled, y_scaled


def get_labels_info(data: list) -> (int, int):
    """ This method gets the labels and the length of the string labels that will be shown on a given axis """

    # Find min and max values in data to display on axis
    data_min = round(min(data))
    data_max = round(max(data))

    # Count length of the string that displays these values
    length_label_min = len(str(data_min))
    length_label_max = len(str(data_max))

    return data_min, data_max, length_label_min, length_label_max
