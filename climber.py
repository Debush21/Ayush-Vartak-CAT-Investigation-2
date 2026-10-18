
import random  # Picks a random number.
import numpy as np  # Helps make graph points.
import matplotlib.pyplot as plt  # Draws the graph.

equation = input("Enter a quadratic (e.g. -x**2 + 10*x + 3): ")  # Gets the equation.
equation = equation.replace("^", "**")  # Changes ^ into Python's power symbol.

def calculate_y(x):  # Finds y for a given x.
    return eval(equation, {"__builtins__": {}}, {"x": x})  # Calculates y using the equation.

a = (calculate_y(1) + calculate_y(-1) - 2 * calculate_y(0)) / 2  # Finds the x**2 coefficient.

if a >= 0:  # Checks if the graph opens downwards.
    print("Error: The x**2 coefficient must be negative.")  # Shows an error message.
    raise SystemExit  # Stops the program.

x = random.uniform(-1000, 1000)  # Picks a random starting x-value.
y = calculate_y(x)  # Finds the starting y-value.
start_x = x  # Saves the starting x-value.
start_y = y  # Saves the starting y-value.

step = 1000  # Sets the first step size.
tolerance = 1 / abs(a)  # Sets the target step size.

path_x = [x]  # Saves the starting x-value for the graph.
path_y = [y]  # Saves the starting y-value for the graph.

while step > tolerance:  # Keeps searching while the steps are too large.
    left_x = x - step  # Tests a point to the left.
    right_x = x + step  # Tests a point to the right.
    left_y = calculate_y(left_x)  # Finds the left point's height.
    right_y = calculate_y(right_x)  # Finds the right point's height.

    if left_y > y and left_y >= right_y:  # Checks if the left point is higher.
        x = left_x  # Moves to the left point.
        y = left_y  # Updates the height.
    elif right_y > y:  # Checks if the right point is higher.
        x = right_x  # Moves to the right point.
        y = right_y  # Updates the height.
    else:  # Runs when neither point is higher.
        step = step / 2  # Makes the steps smaller.

    path_x.append(x)  # Saves the current x-value.
    path_y.append(y)  # Saves the current y-value.

print("\nEstimated maximum:")  # Prints a heading.
print(f"x = {x:.6f}")  # Prints the estimated x-value.
print(f"y = {y:.6f}")  # Prints the estimated maximum y-value.

graph_x = np.linspace(-1000, 1000, 2000)  # Makes x-values for the graph.
graph_y = [calculate_y(value) for value in graph_x]  # Calculates their y-values.

plt.figure(figsize=(10, 6))  # Sets the graph size.
plt.plot(graph_x, graph_y, label="Quadratic")  # Draws the quadratic.
plt.plot(path_x, path_y, "o-", label="Climbing path")  # Draws the search path.
plt.scatter(start_x, start_y, color="green", label="Start")  # Marks the starting point.
plt.scatter(x, y, color="red", marker="*", s=200, label="Maximum")  # Marks the estimated maximum.

plt.title("Quadratic Hill Climbing")  # Adds a graph title.
plt.xlabel("x")  # Labels the horizontal axis.
plt.ylabel("y")  # Labels the vertical axis.
plt.grid(True)  # Adds grid lines.
plt.legend()  # Shows what each colour means.
plt.tight_layout()  # Keeps the graph layout neat.
plt.show()  # Displays the graph.
