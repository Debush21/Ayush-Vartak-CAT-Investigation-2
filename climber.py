import numpy as np
import matplotlib.pyplot as plt
import random

equation = input("Enter a quadratic (e.g. y=40*x-2*x**2): ")

if "=" in equation:
    equation = equation.split("=", 1)[1]

def calculate_y(x):
    return eval(equation, {"__builtins__": {}}, {"x": x})

# Start at a random x-value
x = random.uniform(-1000, 1000)

step = 100
minimum_step = 0.001

path_x = [x]
path_y = [calculate_y(x)]

# Hill-climbing algorithm
while step > minimum_step:
    current_y = calculate_y(x)

    left_x = x - step
    right_x = x + step

    left_y = calculate_y(left_x)
    right_y = calculate_y(right_x)

    if left_y > current_y and left_y >= right_y:
        x = left_x
    elif right_y > current_y and right_y >= left_y:
        x = right_x
    else:
        step = step / 2

    path_x.append(x)
    path_y.append(calculate_y(x))

maximum_x = x
maximum_y = calculate_y(maximum_x)

print("\nApproximate maximum:")
print("x =", maximum_x)
print("y =", maximum_y)

# Graph the quadratic
graph_x = np.linspace(-1000, 1000, 2000)
graph_y = [calculate_y(value) for value in graph_x]

plt.plot(graph_x, graph_y, label="Quadratic")
plt.plot(path_x, path_y, "ro-", markersize=3,
         label="Hill-climbing path")
plt.scatter(maximum_x, maximum_y, color="green",
            s=80, label="Approximate maximum")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Hill-Climbing Optimisation")
plt.grid(True)
plt.legend()
plt.show()