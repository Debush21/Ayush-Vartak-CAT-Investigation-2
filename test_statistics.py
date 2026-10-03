from statistics_library import *

# Open the normal dataset
file = open("normal.txt", "r")

# Create an empty list to store the data
data = []

# Go through each line in the file
for line in file:
    # Convert the line from text into a number
    value = float(line)

    # Add the number to our data list
    data.append(value)

# Close the file
file.close()

# Display all of the statistics
print("Mean:", mean(data))
print("Median:", median(data))
print("Minimum:", minimum(data))
print("Maximum:", maximum(data))
print("Range:", data_range(data))
print("Lower quartile:", lower_quartile(data))
print("Upper quartile:", upper_quartile(data))
print("IQR:", interquartile_range(data))
print("Variance:", variance(data))
print("Standard deviation:", standard_deviation(data))