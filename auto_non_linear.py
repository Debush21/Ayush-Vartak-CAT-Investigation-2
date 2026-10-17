
import matplotlib.pyplot as plt  # Import matplotlib to display the graph.
import math  # Import math to calculate distances.
import bisect  # Import bisect to find candidate radii efficiently.

# Create empty lists to store the coordinates and actual classifications.
x_values = []  # Store the x-coordinates of the data points.
y_values = []  # Store the y-coordinates of the data points.
labels = []  # Store the actual colours of the data points.

# Open the CSV file and read each data point.
with open("non_linear_1.csv", "r") as file:  # Open the dataset.
    for line in file:  # Process each line in the file.
        x, y, label = line.strip().split(",")  # Separate the coordinates and label.
        x_values.append(float(x))  # Convert x to a number and store it.
        y_values.append(float(y))  # Convert y to a number and store it.
        labels.append(label.strip().lower())  # Store the label in lowercase.

# Calculate each point's distance from the origin (0, 0).
distances = []  # Create a list to store the distances.
for x, y in zip(x_values, y_values):  # Process each coordinate pair.
    distance = math.sqrt(x ** 2 + y ** 2)  # Calculate the distance using Pythagoras.
    distances.append(distance)  # Add the distance to the list.

# Sort the unique distances to identify where classifications can change.
unique_distances = sorted(set(distances))  # Remove duplicates and sort the distances.

# Create candidate radii representing every possible classification boundary.
candidate_radii = [0.0]  # Start with a radius of zero.
for i in range(len(unique_distances) - 1):  # Examine consecutive unique distances.
    midpoint = (unique_distances[i] + unique_distances[i + 1]) / 2  # Find the midpoint.
    candidate_radii.append(midpoint)  # Add the midpoint as a candidate radius.

# Include a radius larger than every point's distance from the origin.
candidate_radii.append(unique_distances[-1] + 1)  # Ensure all points can be inside.

# Find the radius that correctly classifies the greatest number of points.
best_radius = 0.0  # Initialise the best radius.
best_correct = -1  # Initialise the highest correct classification count.
best_errors = float("inf")  # Initialise the lowest classification error.

# Sort the distances of points labelled red for an efficient search.
red_distances = sorted(  # Sort distances belonging to actual red points.
    distances[i] for i in range(len(distances)) if labels[i] == "red"  # Select red points.
)  # Finish creating the sorted red-distance list.

# Test each candidate radius systematically.
for radius in candidate_radii:  # Examine every meaningful candidate radius.
    red_inside = bisect.bisect_right(red_distances, radius)  # Count red points inside.
    total_inside = bisect.bisect_right(unique_distances, radius)  # Count all points inside.
    actual_red = labels.count("red")  # Count the actual red points in the dataset.
    correct = red_inside + (len(labels) - total_inside - (actual_red - red_inside))  # Count correct predictions.
    errors = len(labels) - correct  # Calculate the number of incorrect predictions.

    # Update the best result if this radius improves accuracy.
    if correct > best_correct:  # Check whether this radius is more accurate.
        best_correct = correct  # Save the improved correct count.
        best_radius = radius  # Save the improved radius.
        best_errors = errors  # Save the improved error count.

# Calculate the final classification accuracy as a percentage.
percentage = (best_correct / len(labels)) * 100  # Convert correct predictions to a percentage.

# Create the graph and its axes.
fig, ax = plt.subplots(figsize=(9, 9))  # Create a square graph.

# Plot every point using its actual colour from the dataset.
for x, y, label in zip(x_values, y_values, labels):  # Process each data point.
    ax.scatter(x, y, color=label, s=60)  # Plot the point in its actual colour.

# Draw the automatically calculated classification circle.
circle = plt.Circle(  # Create a circle centred at the origin.
    (0, 0),  # Set the centre coordinates to (0, 0).
    best_radius,  # Use the automatically selected radius.
    fill=False,  # Leave the inside of the circle transparent.
    color="black",  # Draw the circle in black.
    linewidth=2  # Set the circle's line thickness.
)  # Finish creating the circle.
ax.add_patch(circle)  # Add the circle to the graph.

# Configure the graph's appearance.
ax.set_xlim(-100, 100)  # Set the horizontal graph limits.
ax.set_ylim(-100, 100)  # Set the vertical graph limits.
ax.set_xlabel("X")  # Label the horizontal axis.
ax.set_ylabel("Y")  # Label the vertical axis.
ax.set_title("Automatic Non-Linear Classification")  # Add a descriptive title.
ax.axhline(0, color="black", linewidth=0.8)  # Draw the horizontal axis.
ax.axvline(0, color="black", linewidth=0.8)  # Draw the vertical axis.
ax.grid(True, alpha=0.3)  # Display a lightly shaded grid.
ax.set_aspect("equal")  # Keep the circle's horizontal and vertical scales equal.

# Display the selected radius and classification accuracy on the graph.
ax.text(  # Add a text box to the graph.
    -95,  # Set the text box's horizontal position.
    92,  # Set the text box's vertical position.
    f"Radius: {best_radius:.2f}\nScore: {percentage:.2f}%",  # Display the results.
    fontsize=12,  # Set the text size.
    bbox=dict(facecolor="white", edgecolor="black")  # Add a bordered white background.
)  # Finish adding the text box.

# Display the completed graph.
plt.show()  # Open the graph window.

# Print the final results in the terminal.
print(f"Best radius: {best_radius:.2f}")  # Display the selected radius.
print(f"Correct classifications: {best_correct}/{len(labels)}")  # Display correct predictions.
print(f"Incorrect classifications: {best_errors}")  # Display incorrect predictions.
print(f"Classification score: {percentage:.2f}%")  # Display the final accuracy.
