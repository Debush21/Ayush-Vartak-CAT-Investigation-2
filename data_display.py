import matplotlib.pyplot as plt

# Open the CSV file
file = open("linear_1 .csv", "r")

# Lists to store the x values, y values and colours
x_values = []
y_values = []
colours = []
# Read each line in the file
for line in file:
    # Remove the newline and split the line at each comma
    data = line.strip().split(",")
    # Store the x value
    x_values.append(float(data[0]))
    # Store the y value
    y_values.append(float(data[1]))
    # Store the colour
    colours.append(data[2])
# Close the file
file.close()

# Find the minimum and maximum x values
x_min = min(x_values)
x_max = max(x_values)

# Find the minimum and maximum y values
y_min = min(y_values)
y_max = max(y_values)

# Create a scatterplot using the data
plt.scatter(x_values, y_values, c=colours)

# Set the range of the x-axis using the minimum and maximum values
plt.xlim(x_min, x_max)

# Set the range of the y-axis using the minimum and maximum values
plt.ylim(y_min, y_max)

# Label the axes
plt.xlabel("X")
plt.ylabel("Y")

# Add a title
plt.title("Linear Classification Data")

# Display the graph
plt.show()