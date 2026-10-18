
import matplotlib.pyplot as plt

# Get the quadratic equation
equation = input("Enter a quadratic equation (e.g. 40*x - 2*x**2): ")

# Get the graph scale from the user
x_min = float(input("Enter minimum x value: "))
x_max = float(input("Enter maximum x value: "))
y_min = float(input("Enter minimum y value: "))
y_max = float(input("Enter maximum y value: "))

# Generate the x and y coordinates
x_values = []
y_values = []

x = x_min

while x <= x_max:
    x_values.append(x)
    y_values.append(eval(equation))
    x += 0.1

# Plot the quadratic
plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Graph")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.grid(True)
plt.show()
