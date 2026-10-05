import matplotlib.pyplot as plt


# Read the data
file = open("linear_1 .csv", "r")

x_values = []
y_values = []
colours = []

for line in file:
    data = line.strip().split(",")

    x_values.append(float(data[0]))
    y_values.append(float(data[1]))
    colours.append(data[2])

file.close()


# Display the original data
plt.scatter(x_values, y_values, c=colours)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Original Data")
plt.show()


# Get the line from the user
m = float(input("Enter gradient (m): "))
c = float(input("Enter y-intercept (c): "))


# Calculate the two scores
score_1_correct = 0
score_2_correct = 0

for i in range(len(x_values)):

    line_y = m * x_values[i] + c

    # Point is above the line
    if y_values[i] >= line_y:

        # Score 1: red above, blue below
        if colours[i] == "red":
            score_1_correct += 1

        # Score 2: blue above, red below
        if colours[i] == "blue":
            score_2_correct += 1

    # Point is below the line
    else:

        # Score 1: blue below
        if colours[i] == "blue":
            score_1_correct += 1

        # Score 2: red below
        if colours[i] == "red":
            score_2_correct += 1


# Convert to percentages
score_1 = score_1_correct / len(x_values) * 100
score_2 = score_2_correct / len(x_values) * 100

best_score = max(score_1, score_2)


# Display scores
print("Score 1:", score_1, "%")
print("Score 2:", score_2, "%")
print("Best score:", best_score, "%")


# Create the line
x_line = [min(x_values), max(x_values)]
y_line = [m * x_line[0] + c, m * x_line[1] + c]


# Display the final graph
plt.scatter(x_values, y_values, c=colours)
plt.plot(x_line, y_line)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Classification")

plt.show()