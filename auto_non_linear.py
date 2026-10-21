import csv
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Load the data from the CSV file
points = []
with open("non_linear_1.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 3:                    # skip incomplete rows
            continue
        try:
            x = float(row[0].strip())       # get x value
            y = float(row[1].strip())       # get y value
            colour = row[2].strip().lower() # get colour (red/blue)
            if colour not in ("red", "blue"):
                continue
            points.append((x, y, colour))   # store the point
        except ValueError:
            continue                        # skip bad rows

if not points:
    raise SystemExit("No valid data found in non_linear_1.csv")

print(f"Loaded {len(points)} points")

# Function that calculates accuracy for a given radius
def score(radius, points):
    correct_A = 0                           # score if inside=red
    correct_B = 0                           # score if inside=blue
    for x, y, colour in points:
        dist = math.hypot(x, y)             # distance from origin
        inside = dist <= radius             # is point inside circle?
        if (inside and colour == "red") or (not inside and colour == "blue"):
            correct_A += 1
        if (inside and colour == "blue") or (not inside and colour == "red"):
            correct_B += 1
    best = max(correct_A, correct_B)        # keep the better score
    return 100.0 * best / len(points)       # turn into percentage

# Search for the best radius (step of 0.1)
best_radius   = 0.0
best_accuracy = -1.0

for r in [i * 0.1 for i in range(0, 1501)]: # try radii from 0 to 150
    acc = score(r, points)                  # test this radius
    if acc > best_accuracy:                 # better than current best?
        best_accuracy = acc
        best_radius   = r

print(f"Best radius found : {best_radius:.1f}")
print(f"Classification accuracy: {best_accuracy:.1f}%")

# Separate the points by colour for plotting
xs_red   = [p[0] for p in points if p[2] == "red"]
ys_red   = [p[1] for p in points if p[2] == "red"]
xs_blue  = [p[0] for p in points if p[2] == "blue"]
ys_blue  = [p[1] for p in points if p[2] == "blue"]

# Create the graph
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(xs_red,  ys_red,  c="red",  label="Red",  s=50)
ax.scatter(xs_blue, ys_blue, c="blue", label="Blue", s=50)

# Draw the best circle
circle = Circle((0, 0), best_radius, fill=False, edgecolor="green",
                linewidth=2.5, label=f"Best radius = {best_radius:.1f}")
ax.add_patch(circle)

# Set graph limits and style
ax.set_xlim(-110, 110)
ax.set_ylim(-110, 110)
ax.set_aspect("equal")                      # keep circle round
ax.grid(True)
ax.legend()
ax.set_title(f"Automatic non-linear classification  –  Accuracy {best_accuracy:.1f}%")
plt.show()