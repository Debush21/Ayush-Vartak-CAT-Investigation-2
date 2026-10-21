import csv
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# ------------------------------------------------------------------
# Load the data  (x, y, colour)
# ------------------------------------------------------------------
points = []
with open("non_linear_1.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 3:
            continue
        try:
            x = float(row[0].strip())
            y = float(row[1].strip())
            colour = row[2].strip().lower()
            if colour not in ("red", "blue"):
                continue
            points.append((x, y, colour))
        except ValueError:
            continue

if not points:
    raise SystemExit("No valid data found in non_linear_1.csv")

print(f"Loaded {len(points)} points")

# ------------------------------------------------------------------
# Scoring function (identical to the manual version)
# ------------------------------------------------------------------
def score(radius, points):
    correct_A = 0
    correct_B = 0
    for x, y, colour in points:
        dist = math.hypot(x, y)
        inside = dist <= radius
        if (inside and colour == "red") or (not inside and colour == "blue"):
            correct_A += 1
        if (inside and colour == "blue") or (not inside and colour == "red"):
            correct_B += 1
    best = max(correct_A, correct_B)
    return 100.0 * best / len(points)

# ------------------------------------------------------------------
# Superior search – systematic grid (step 0.1)
# ------------------------------------------------------------------
best_radius   = 0.0
best_accuracy = -1.0

for r in [i * 0.1 for i in range(0, 1501)]:   # 0.0 → 150.0
    acc = score(r, points)
    if acc > best_accuracy:
        best_accuracy = acc
        best_radius   = r

print(f"Best radius found : {best_radius:.1f}")
print(f"Classification accuracy: {best_accuracy:.1f}%")

# ------------------------------------------------------------------
# Display everything
# ------------------------------------------------------------------
xs_red   = [p[0] for p in points if p[2] == "red"]
ys_red   = [p[1] for p in points if p[2] == "red"]
xs_blue  = [p[0] for p in points if p[2] == "blue"]
ys_blue  = [p[1] for p in points if p[2] == "blue"]

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(xs_red,  ys_red,  c="red",  label="Red",  s=50)
ax.scatter(xs_blue, ys_blue, c="blue", label="Blue", s=50)

circle = Circle((0, 0), best_radius, fill=False, edgecolor="green",
                linewidth=2.5, label=f"Best radius = {best_radius:.1f}")
ax.add_patch(circle)

ax.set_xlim(-110, 110)
ax.set_ylim(-110, 110)
ax.set_aspect("equal")
ax.grid(True)
ax.legend()
ax.set_title(f"Automatic non-linear classification  –  Accuracy {best_accuracy:.1f}%")
plt.show()