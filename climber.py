
# climber.py
# Finds the approximate maximum of a downward-opening quadratic.

import re  # Parses the equation.
import random  # Chooses a random starting point.
import matplotlib.pyplot as plt  # Draws the graph.

def to_number(s):  # Converts a coefficient into a number.
    if s == "" or s == "+":  # Handles a missing positive coefficient.
        return 1.0  # The coefficient is positive one.
    if s == "-":  # Handles a missing negative coefficient.
        return -1.0  # The coefficient is negative one.
    return float(s)  # Converts the coefficient to a number.

def parse_quadratic(text):  # Extracts a, b and c from the equation.
    s = text.lower().replace(" ", "").replace("*", "")  # Normalises the input.
    if s.startswith("y="):  # Checks for y= at the start.
        s = s[2:]  # Removes y=.
    s = s.replace("²", "^2")  # Supports the squared symbol.
    terms = re.findall(r"[+-]?[^+-]+", s)  # Splits the equation into terms.
    a = b = c = 0.0  # Initialises the coefficients.
    for term in terms:  # Processes each term.
        if "x" in term:  # Checks whether the term contains x.
            if "x^2" in term:  # Identifies the squared term.
                coefficient = term.replace("x^2", "")  # Removes x squared.
                a += to_number(coefficient)  # Adds to a.
            else:  # Handles the linear term.
                coefficient = term.replace("x", "")  # Removes x.
                b += to_number(coefficient)  # Adds to b.
        else:  # Handles the constant term.
            c += float(term)  # Adds to c.
    return a, b, c  # Returns the coefficients.

while True:  # Repeats until a valid equation is entered.
    text = input("Enter a quadratic (e.g. -x^2 - 6x + 5): ")  # Gets the equation.
    try:  # Attempts to parse the equation.
        a, b, c = parse_quadratic(text)  # Extracts the coefficients.
        if a >= 0:  # Checks that the parabola opens downwards.
            print("The x^2 coefficient must be negative.")  # Explains the issue.
            continue  # Requests another equation.
        break  # Accepts the equation.
    except (ValueError, AttributeError):  # Handles parsing errors.
        print("Invalid equation. Try something like -x^2 - 6x + 5.")  # Gives an example.

print(f"Parsed coefficients: a={a}, b={b}, c={c}")  # Displays the coefficients.

def f(x):  # Defines the quadratic function.
    return a * x**2 + b * x + c  # Calculates y.

x = random.uniform(-1000, 1000)  # Chooses a random starting x.
y = f(x)  # Calculates the starting height.
start_x = x  # Saves the starting x-coordinate.
start_y = y  # Saves the starting y-coordinate.

step = 10.0  # Sets the initial step size.
tolerance = 0.001 / abs(a)  # Sets the stopping tolerance.
path_x = [x]  # Stores visited x-coordinates.
path_y = [y]  # Stores visited y-coordinates.
max_iter = 10000  # Prevents an endless loop.
iteration = 0  # Starts the iteration counter.

while step > tolerance and iteration < max_iter:  # Searches until sufficiently close.
    left_x = max(-1000, x - step)  # Tests left without crossing the boundary.
    right_x = min(1000, x + step)  # Tests right without crossing the boundary.
    left_y = f(left_x)  # Calculates the left height.
    right_y = f(right_x)  # Calculates the right height.

    if left_y > y and left_y >= right_y:  # Checks whether left is better.
        x = left_x  # Moves left.
        y = left_y  # Updates the height.
        path_x.append(x)  # Records the new x.
        path_y.append(y)  # Records the new y.
    elif right_y > y:  # Checks whether right is better.
        x = right_x  # Moves right.
        y = right_y  # Updates the height.
        path_x.append(x)  # Records the new x.
        path_y.append(y)  # Records the new y.
    else:  # Runs when neither neighbour is higher.
        step /= 2  # Halves the step size.

    iteration += 1  # Counts this iteration.

print("\nApproximate maximum:")  # Displays the results heading.
print(f"x = {x:.6f}")  # Prints the estimated x-coordinate.
print(f"y = {f(x):.6f}")  # Prints the estimated maximum height.
print(f"Iterations = {iteration}")  # Shows how many iterations were used.

margin = max(5, abs(x) * 0.1)  # Sets the graph zoom.
graph_min = max(-1000, x - margin)  # Sets the left graph boundary.
graph_max = min(1000, x + margin)  # Sets the right graph boundary.
xs = [graph_min + i * (graph_max - graph_min) / 999 for i in range(1000)]  # Creates smooth graph x-values.
ys = [f(value) for value in xs]  # Calculates graph y-values.

plt.figure(figsize=(10, 6))  # Sets the graph size.
plt.plot(xs, ys, color="blue", linewidth=2, label="Quadratic curve")  # Draws the parabola.
plt.plot(path_x, path_y, "o-", color="red", markersize=4, linewidth=1, label="Climbing path")  # Connects the search points.
plt.scatter([start_x], [start_y], color="green", s=70, label="Starting point", zorder=3)  # Marks the start.
plt.scatter([x], [f(x)], marker="*", color="gold", edgecolors="black", s=200, label="Estimated maximum", zorder=4)  # Marks the estimated peak.

plt.xlim(graph_min, graph_max)  # Zooms the horizontal axis.
plt.ylim(min(ys) - 2, max(ys) + 2)  # Fits the vertical axis to the curve.
plt.title("Hill Climbing on a Quadratic")  # Adds the graph title.
plt.xlabel("x")  # Labels the horizontal axis.
plt.ylabel("y")  # Labels the vertical axis.
plt.legend()  # Displays the legend.
plt.grid(True)  # Adds grid lines.
plt.tight_layout()  # Improves spacing.
plt.show()  # Displays the graph.
