import matplotlib.pyplot as plt

# Ask the user for the quadratic equation
equation = input("Enter the quadratic equation (e.g. y=40x-2x^2): ")

# Clean the equation so Python can understand it
equation = equation.replace(" ", "")          # remove spaces
if "=" in equation:                           # keep only the right side
    equation = equation.split("=")[1]
equation = equation.replace("^", "**")        # turn ^ into **
equation = equation.replace("x", "*x")        # turn 2x into 2*x
equation = equation.replace("**x", "**x")     # fix any double stars
# (simple clean-up – works for the usual forms students enter)

# Ask for the axis limits
x_min = float(input("Enter minimum x value: "))
x_max = float(input("Enter maximum x value: "))
y_min = float(input("Enter minimum y value: "))
y_max = float(input("Enter maximum y value: "))

# Create lists to store the points
x_values = []
y_values = []

# Generate many points across the chosen x range
x = x_min
while x <= x_max:
    x_values.append(x)
    y_values.append(eval(equation))           # calculate y for this x
    x += 0.1                                  # small step for a smooth curve

# Draw the graph
plt.plot(x_values, y_values, color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Graph")
plt.xlim(x_min, x_max)                        # set x-axis scale
plt.ylim(y_min, y_max)                        # set y-axis scale
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.8)  # draw x-axis
plt.axvline(0, color="black", linewidth=0.8)  # draw y-axis
plt.show()