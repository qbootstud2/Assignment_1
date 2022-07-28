import math

from src.generate_plots import make_plot, plot_check


if __name__ == "__main__":

    # Generate cross-check plots with matplotlib
    check_plot = False

    # Example 1
    scale = 0.1
    n = int(8 * math.pi / scale)
    x = [scale * i for i in range(n)]
    y = [math.sin(scale * i) for i in range(n)]
    make_plot(x, y, display_grid=True, height=15, title="The sine function",
              legend="f(x) = sin(x), where 0 <= x <= 8π")

    if check_plot:
        plot_check(x, y, display_grid=True, height=15, title="The sine function",
                   legend="f(x) = sin(x), where 0 <= x <= 8π")

    # Example 2
    scale = 0.1
    n = int(2 * math.pi / scale)
    x = [scale * i for i in range(n)]
    y = [math.cos(scale * i) for i in range(n)]
    make_plot(x, y, width=50, title="The cosine function", legend="f(x) = cos(x), where 0 <= x <= 2π")

    # Example 3
    y = [ord(c) for c in 'ASCII Plotter example']
    n = len(y)
    x = [i for i in range(n)]
    make_plot(x, y, title="Plotting Random Data", legend="f(x) = random data")
