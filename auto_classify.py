import matplotlib.pyplot as plt
import random


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


# Get the number of trials from the user
trials = int(input("Enter number of trials: "))


# Store the best result
best_score = 0
best_m = 0
best_c = 0
best_score_type = 0


# Random search
for trial in range(trials):

    # Randomly choose m and c
    m = random.uniform(-5, 5)
    c = random.uniform(-100, 100)

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


    # Convert scores to percentages
    score_1 = score_1_correct / len(x_values) * 100
    score_2 = score_2_correct / len(x_values) * 100

    # Find the best score for this trial
    trial_best_score = max(score_1, score_2)

    # Keep the best result
    if trial_best_score > best_score:

        best_score = trial_best_score
        best_m = m
        best_c = c

        if score_1 >= score_2:
            best_score_type = 1
        else:
            best_score_type = 2


# Display the best result
print()
print("RANDOM SEARCH COMPLETE")
print("----------------------")
print("Number of trials:", trials)
print("Best gradient (m):", best_m)
print("Best y-intercept (c):", best_c)
print("Best score:", best_score, "%")


# Create the best line
x_line = [min(x_values), max(x_values)]
y_line = [
    best_m * x_line[0] + best_c,
    best_m * x_line[1] + best_c
]


# Display the final graph
plt.figure(figsize=(10, 7))

plt.scatter(
    x_values,
    y_values,
    c=colours,
    s=60,
    edgecolors="black"
)

plt.plot(
    x_line,
    y_line,
    linewidth=2,
    label=f"Best line: y = {best_m:.2f}x + {best_c:.2f}"
)

plt.xlabel("x")
plt.ylabel("y")
plt.title(
    f"Linear Classification - Random Search\n"
    f"Best Score: {best_score:.2f}% | Trials: {trials}"
)

plt.legend()
plt.grid(True, alpha=0.3)

plt.show()