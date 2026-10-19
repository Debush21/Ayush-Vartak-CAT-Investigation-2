
import numpy as np
import matplotlib.pyplot as plt
import re

# Get the quadratic from the user
equation = input("Enter a quadratic (e.g. -x^2 - 6x + 5): ")
equation = equation.replace(" ", "").replace("^", "**")

# Convert the quadratic into coefficients a, b and c
equation = equation.replace("-", "+-")
if equation.startswith("+"):
    equation = equation[1:]

terms = equation.split("+")
a, b, c = 0.0, 0.0, 0.0

for term in terms:
    if "x**2" in term:
        coefficient = term.replace("x**2", "")
        a = float(coefficient) if coefficient not in ("", "+") else 1.0
        if coefficient == "-":
            a = -1.0
    elif "x" in term:
        coefficient = term.replace("x", "")
        b = float(coefficient) if coefficient not in ("", "+") else 1.0
        if coefficient == "-":
            b = -1.0
    elif term:
        c = float(term)

if a == 0:
    print("Error: Please enter a quadratic with an x^2 term.")
else:
    # Define the quadratic function
    def f(x):
        return a * x**2 + b * x + c

    # Hill climbing settings
    x = 0.0
    step_size = 1.0
    iterations = 0
    max_iterations = 1000
    tolerance = 0.0001

    # Store the points visited
    visited_x = [x]
    visited_y = [f(x)]

    # Hill climbing algorithm
    while iterations < max_iterations:
        current_y = f(x)

        left_x = x - step_size
        right_x = x + step_size

        left_y = f(left_x)
        right_y = f(right_x)

        if left_y > current_y and left_y >= right_y:
            x = left_x
        elif right_y > current_y:
            x = right_x
        else:
            step_size /= 2

        iterations += 1
        visited_x.append(x)
        visited_y.append(f(x))

        if step_size < tolerance:
            break

    # Display the results
    print("\nOptimisation Results")
    print("--------------------")
    print(f"Maximum x value: {x:.6f}")
    print(f"Maximum y value: {f(x):.6f}")
    print(f"Iterations: {iterations}")

    # Generate values for plotting
    x_values = np.linspace(x - 10, x + 10, 500)
    y_values = f(x_values)

    # Plot the quadratic and the search path
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="Quadratic function")
    plt.scatter(visited_x, visited_y, color="orange",
                s=20, label="Hill-climbing iterations")
    plt.scatter(x, f(x), color="red", s=100,
                label="Estimated maximum", zorder=5)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Quadratic Optimisation Using Hill Climbing")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
