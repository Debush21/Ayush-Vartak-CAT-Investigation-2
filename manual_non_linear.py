import matplotlib.pyplot as plt
import math

# Create empty lists for the data
x_values = []
y_values = []
labels = []

# Read every line from the CSV file
with open("non_linear_1.csv", "r") as file:
    for line in file:
        x, y, label = line.strip().split(",")   # split into 3 parts
        x_values.append(float(x))               # store x as number
        y_values.append(float(y))               # store y as number
        labels.append(label.strip().lower())    # store colour

# Ask the user for a radius
radius = float(input("Enter the radius of the circle: "))

# Count correct predictions for both possible orientations
correct_A = 0   # inside = red, outside = blue
correct_B = 0   # inside = blue, outside = red

# Create the graph
fig, ax = plt.subplots(figsize=(9, 9))

# Go through every point
for x, y, label in zip(x_values, y_values, labels):
    distance = math.sqrt(x**2 + y**2)           # distance from (0,0)

    # Orientation A
    predicted_A = "red" if distance <= radius else "blue"
    if predicted_A == label:
        correct_A += 1

    # Orientation B
    predicted_B = "blue" if distance <= radius else "red"
    if predicted_B == label:
        correct_B += 1

    # Plot the point in its real colour
    ax.scatter(x, y, color=label, s=60)

# Use the better of the two orientations
correct = max(correct_A, correct_B)
percentage = (correct / len(labels)) * 100

# Draw the circle
circle = plt.Circle((0, 0), radius, fill=False, color="black", linewidth=2)
ax.add_patch(circle)

# Set up the graph
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_aspect("equal")                          # keep circle round
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Manual Non-Linear Classification")
ax.axhline(0, color="black", linewidth=0.8)     # x-axis
ax.axvline(0, color="black", linewidth=0.8)     # y-axis
ax.grid(True, alpha=0.3)

# Show radius and score on the graph
ax.text(-95, 92, f"Radius: {radius}\nScore: {percentage:.2f}%",
        fontsize=12, bbox=dict(facecolor="white", edgecolor="black"))

plt.show()

# Also print the results
print(f"Correct classifications: {correct}/{len(labels)}")
print(f"Classification score: {percentage:.2f}%")