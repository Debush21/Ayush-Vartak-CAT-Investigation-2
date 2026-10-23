# Import libraries for plotting, random numbers and text processing
import matplotlib.pyplot as plt
import random
import re

def clean_equation(raw):
    eq = raw.strip()
    # Remove everything on the left of the last '=' (handles "y = ...")
    if "=" in eq:
        eq = eq.split("=")[-1].strip()
    # Drop any remaining "y" that might be left (rare)
    eq = re.sub(r'\by\b', '', eq)
    # Remove all spaces
    eq = eq.replace(" ", "")
    # Replace ^ with ** (Python power)
    eq = eq.replace("^", "**")
    # Insert * between number and x  (e.g. 2x → 2*x, 3.5x → 3.5*x)
    eq = re.sub(r'(\d)x', r'\1*x', eq)
    # Also handle .x  (rare but possible after a decimal)
    eq = re.sub(r'(\.)x', r'\1*x', eq)
    # Insert * between ) and x or number and ( if needed (simple cases)
    eq = re.sub(r'\)x', r')*x', eq)
    eq = re.sub(r'x\(', r'x*(', eq)
    # Handle bare "x2" style if someone writes x2 instead of x^2 (optional)
    # eq = re.sub(r'x2\b', 'x**2', eq)
    # If the expression is empty after cleaning, raise a clear error
    if not eq:
        raise ValueError("Could not extract a usable expression from the input.")
    return eq

# Ask the user to enter a quadratic equation
print("Enter a quadratic (examples: y = x**2 + 2*x + 5   or   x^2+2x+5   or   -0.5x^2 - 3x + 1)")
raw_equation = input("Equation: ")

try:
    equation = clean_equation(raw_equation)
    print(f"Using expression: {equation}")
except ValueError as e:
    print(e)
    exit()

# Define a function to calculate y for any x value
def calculate_y(x):
    # Evaluate the equation using the given x value (safe-ish globals)
    return eval(equation, {"__builtins__": {}}, {"x": x})

# Quick sanity check that the expression works
try:
    _ = calculate_y(0)
except Exception as e:
    print(f"Error evaluating the expression: {e}")
    print("Please check the equation and try again.")
    exit()

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
    left_x = x - step
    right_x = x + step   
    left_y = calculate_y(left_x)
    right_y = calculate_y(right_x)

    # Check whether moving left increases the y value
    if left_y > y:
        # Move one step to the left
        x = left_x
        y = left_y
        path_x.append(x)
        path_y.append(y)

    # Otherwise, check whether moving right increases the y value
    elif right_y > y:
        # Move one step to the right
        x = right_x
        y = right_y
        path_x.append(x)
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
    graph_x.append(value)
    graph_y.append(calculate_y(value))
    value += 1

# Plot the quadratic curve and label it
plt.plot(graph_x, graph_y, label=f"y = {equation}")

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