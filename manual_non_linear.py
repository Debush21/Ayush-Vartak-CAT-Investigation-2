import matplotlib.pyplot as plt
import math

# Create empty lists to store the x coordinates, y coordinates and
# the actual colour/classification of each data point.
x_values = []
y_values = []
labels = []
 
# Open the CSV file and read each data point.
with open("non_linear_1.csv", "r") as file:
    for line in file:
        # Split each row into its x value, y value and colour.
        x, y, label = line.strip().split(",")

        # Convert the coordinates to numbers before storing them.
        x_values.append(float(x))
        y_values.append(float(y))
        labels.append(label)

# Ask the user to enter the radius of the circle they want to use
# for classifying the data.
radius = float(input("Enter the radius of the circle: "))

# Keep track of how many points are classified correctly.
correct = 0

# Create the graph where the data points and classification circle
# will be displayed.
fig, ax = plt.subplots(figsize=(9, 9))

# Go through every data point and classify it based on its distance
# from the centre of the circle, which is at (0, 0).
for x, y, label in zip(x_values, y_values, labels):

    # Calculate the distance from the point to the centre of the
    # circle using the distance formula.
    distance = math.sqrt(x ** 2 + y ** 2)

    # Points inside the circle are classified as red, while points
    # outside the circle are classified as blue.
    if distance <= radius:
        predicted = "red"
    else:
        predicted = "blue"

    # Compare the predicted classification with the actual
    # classification stored in the CSV file.
    if predicted == label:
        correct += 1

    # Plot the point using its actual colour from the data.
    if label == "red":
        ax.scatter(x, y, color="red", s=60)
    else:
        ax.scatter(x, y, color="blue", s=60)

# Calculate the percentage of points that were classified correctly.
percentage = (correct / len(labels)) * 100

# Create a circle centred at (0, 0) using the radius entered by
# the user.
circle = plt.Circle(
    (0, 0),
    radius,
    fill=False,
    color="black",
    linewidth=2
)

# Add the circle to the graph.
ax.add_patch(circle)

# Set the graph limits based on the possible range of the data.
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

# Add labels and a title to make the graph easier to understand.
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Manual Non-Linear Classification")

# Add x and y axes through the centre of the graph.
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# Add a grid to make the coordinates easier to read.
ax.grid(True, alpha=0.3)

# Make sure the x and y scales are equal so the circle is displayed
# as a true circle rather than being stretched.
ax.set_aspect("equal")

# Display the radius and classification score on the graph.
ax.text(
    -95,
    92,
    f"Radius: {radius}\nScore: {percentage:.2f}%",
    fontsize=12,
    bbox=dict(facecolor="white", edgecolor="black")
)

# Display the graph.
plt.show()

# Also display the results in the terminal.
print(f"Correct classifications: {correct}/{len(labels)}")
print(f"Classification score: {percentage:.2f}%")