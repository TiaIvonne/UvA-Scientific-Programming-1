# PLOT
# name: Ivonne Mendoza email: ivonne@imendoza.io
# This code creates a plot based on a formula

from matplotlib import pyplot as plt
import numpy as np


def plot_function(x:float)->float:
    """
    This function calculates the result of this formula
    12.38·x⁴ - 84.38·x³ + 165.19·x² - 103.05·x
    """
    formula = 12.38 * x ** 4 - 84.38 * x ** 3 + 165.19 * x ** 2 - 103.05 * x
    return formula

x_values = np.arange(0, 4, 0.01)
y_values = plot_function(x_values)
plt.xlabel("x")
plt.ylabel("plot function(x)")
plt.title("Plot ")
plt.grid(False)

plt.plot(x_values, y_values, color='blue', linewidth=2)
plt.show()






