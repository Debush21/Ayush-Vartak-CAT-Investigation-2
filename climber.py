
# Import libraries for plotting, random numbers and text processing
import matplotlib.pyplot as plt
import random
import re

# Ask the user to enter a quadratic equation
equation = input("Enter the quadratic equation: ")

# Remove spaces from the equation
equation = equation.replace(" ", "")

# Check whether the equation contains an equals sign
if "=" in equation:
    # Keep only the expression on the right side
    equation = equation.split("=")[1]

# Insert multiplication signs between numbers and x
equation = re.sub(r'(\d)x', r'\1*x', equation)

# Replace ^ with ** so Python can calculate powers
equation = equation.replace("^", "**")

# Define a function to calculate y for any x value
def calculate_y(x):
    # Evaluate the equation using the given x value
    return eval(equation, {"__builtins__": {}}, {"x": x})

# Choose a random starting x value between -1000 and 1000
x = random.uniform(-1000, 1000)

# Calculate the starting y value
y = calculate_y(x)

# Store the starting x coordinate of the climbing path
path_x = [x]

# Store the starting y coordinate of the climbing path
path_y = [y]

# Set the initial step size
step = 1.0

# Set the smallest allowed step size
minimum_step = 0.001

# Continue climbing while the step size is large enough
while step >= minimum_step:
    # Calculate the x coordinate one step to the left
    left_x = x - step

    # Calculate the x coordinate one step to the right
    right_x = x + step

    # Calculate the y value to the left
    left_y = calculate_y(left_x)

    # Calculate the y value to the right
    right_y = calculate_y(right_x)

    # Check whether moving left increases the y value
    if left_y > y:
        # Move one step to the left
        x = left_x

        # Update the current y value
        y = left_y

        # Record the new x coordinate
        path_x.append(x)

        # Record the new y coordinate
        path_y.append(y)

    # Otherwise, check whether moving right increases the y value
    elif right_y > y:
        # Move one step to the right
        x = right_x

        # Update the current y value
        y = right_y

        # Record the new x coordinate
        path_x.append(x)

        # Record the new y coordinate
        path_y.append(y)

    # If neither direction improves the y value
    else:
        # Halve the step size to search more precisely
        step = step / 2

# Display the approximate maximum x value
print("Maximum x-value:", x)

# Display the approximate maximum y value
print("Maximum y-value:", y)

# Create an empty list to store graph x coordinates
graph_x = []

# Create an empty list to store graph y coordinates
graph_y = []

# Set the starting x value for the graph
value = -1000

# Generate graph points until x reaches 1000
while value <= 1000:
    # Store the current x coordinate
    graph_x.append(value)

    # Calculate and store the corresponding y coordinate
    graph_y.append(calculate_y(value))

    # Increase x by 1 for the next graph point
    value += 1

# Plot the quadratic curve and label it
plt.plot(graph_x, graph_y, label=f"Quadratic: y = {equation}")

# Plot the climbing path with orange points connected by a line
plt.plot(path_x, path_y, color="orange", marker="o",
         linestyle="-", markersize=4, label="Climbing path")

# Mark the estimated maximum with a green point
plt.plot(x, y, "go", markersize=8,
         label=f"Maximum ({x:.2f}, {y:.2f})")

# Label the horizontal axis
plt.xlabel("x")

# Label the vertical axis
plt.ylabel("y")

# Add a title to the graph
plt.title("Hill Climbing")

# Display grid lines on the graph
plt.grid()

# Display the graph legend
plt.legend()

# Show the completed graph
plt.show()
