# PLOT
# name: Ivonne Mendoza email: ivonne@imendoza.io
# This code creates a plot based on a formula

from matplotlib import pyplot as plt
import numpy as np


def calculate_polynomial(x:float)->float:
    """
    This function calculates the result of this formula
    12.38·x⁴ - 84.38·x³ + 165.19·x² - 103.05·x
    """
    formula = 12.38 * x ** 4 - 84.38 * x ** 3 + 165.19 * x ** 2 - 103.05 * x
    return formula

x_values = np.arange(0,4, 0.01)
#print(x_values)
y_values = calculate_polynomial(x_values)

min_index = 0
# Calculates minimum
for i in range(0,len(x_values)):
    if y_values[i] <= y_values[min_index]:
        min_index = i
print(x_values[min_index], y_values[min_index])
print(min_index)

plt.xlabel('x')
plt.ylabel('plot function(x)')
plt.title('Plot')
plt.grid(False)
plt.plot(x_values, y_values, color='blue', linewidth=2)
# plot minimum values, ro red circle
plt.plot(x_values[min_index], y_values[min_index],'ro', markersize=10)
plt.annotate(f'xmin, ymin: ({x_values[min_index]:.2f},{y_values[min_index]:.2f})',
             xy = (x_values[min_index], y_values[min_index]),
             xytext=(0,5),
             textcoords='offset points',
             ha='right')
plt.show()









