import matplotlib.pyplot as plt
import random
import re

# Get the quadratic equation
equation = input("Enter the quadratic equation: ")

# Convert the equation into Python syntax
equation = equation.replace(" ", "")
if "=" in equation:
    equation = equation.split("=")[1]
    
equation = re.sub(r'(\d)x', r'\1*x', equation)
equation = equation.replace("^", "**")

# Calculate y for a given x
def calculate_y(x):
    return eval(equation, {"__builtins__": {}}, {"x": x})

# Choose a random starting x value
x = random.uniform(-1000, 1000)
y = calculate_y(x)

# Store the climbing path
path_x = [x]
path_y = [y]

step = 1.0
minimum_step = 0.001

# Climb towards the maximum
while step >= minimum_step:
    left_x = x - step
    right_x = x + step
    left_y = calculate_y(left_x)
    right_y = calculate_y(right_x)
    
    if left_y > y:
        x = left_x
        y = left_y
        path_x.append(x)
        path_y.append(y)
    elif right_y > y:
        x = right_x
        y = right_y
        path_x.append(x)
        path_y.append(y)
    else:
        step = step / 2

# Display the approximate maximum
print("Maximum x-value:", x)
print("Maximum y-value:", y)

# Generate points for the quadratic graph
graph_x = []
graph_y = []
value = -1000
while value <= 1000:
    graph_x.append(value)
    graph_y.append(calculate_y(value))
    value += 1

# Plot the quadratic and climbing path
plt.plot(graph_x, graph_y, label=f"Quadratic: y = {equation}")
plt.plot(path_x, path_y, color="orange", marker="o", linestyle="-", markersize=4, label="Climbing path")
plt.plot(x, y, "go", markersize=8, label=f"Maximum ({x:.2f}, {y:.2f})")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Hill Climbing")
plt.grid()
plt.legend()
plt.show()