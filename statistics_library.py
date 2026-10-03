#function for mean 
def mean(data):
    #this function finds the average of a list of numbers that is provided to it
    if len(data) == 0: #if the list is empty without anything we can't calculate anything
        return None
    total = 0 #start a running total at zero
    for value in data: #go through every number in the list one by one
        total = total + value #add the current number to our running total
    return total / len(data) #divide the total by how many numbers there are to get

#function for minimum
def minimum(data): 
    if len(data) == 0: #if the list is empty without anything we can't calculate anything
        return None
    smallest = data[0] #assume the first value is the smallest
    for value in data:#check if the current value is smaller than our current smallest
        if value < smallest:
            smallest = value
    return smallest #return the smallest value we found

# function for maximum
def maximum(data):
    if len(data) == 0: # if the list is empty, we can't find a maximum
        return None
    largest = data[0] # assume the first value is the largest
    for value in data: # check every value in the list
        if value > largest: # check if the current value is larger
            largest = value # if it is larger, make it the new largest
    return largest # return the largest value we found

# function for range
def data_range(data):
    if len(data) == 0: # if the list is empty, we can't calculate the range
        return None
    largest = maximum(data) # find the largest value
    smallest = minimum(data) # find the smallest value
    return largest - smallest # subtract the smallest value from the largest

# function for median
def median(data):
    if len(data) == 0: # if the list is empty, we can't calculate the median
        return None
    values = [] # make a new list so we don't change the original data
    for value in data: # go through every value in the original list
        values.append(value) # add each value to the new list
    for i in range(len(values)): # go through each position in the list
        for j in range(i + 1, len(values)): # compare it with the values after it
            if values[j] < values[i]: # check if the values are in the wrong order
                temporary = values[i] # temporarily save the first value
                values[i] = values[j] # move the smaller value into the first position
                values[j] = temporary # move the saved value into the other position
    middle = len(values) // 2 # find the middle position
    if len(values) % 2 == 0: # check if there is an even number of values
        return (values[middle - 1] + values[middle]) / 2 # average the two middle values
    return values[middle] # return the middle value

# function for lower quartile
def lower_quartile(data):
    if len(data) == 0: # if the list is empty, we can't calculate the lower quartile
        return None
    values = [] # make a new list so we don't change the original data
    for value in data: # go through every value in the original list
        values.append(value) # add each value to the new list
    for i in range(len(values)): # go through each position in the list
        for j in range(i + 1, len(values)): # compare it with the values after it
            if values[j] < values[i]: # check if the values are in the wrong order
                temporary = values[i] # temporarily save the first value
                values[i] = values[j] # move the smaller value into the first position
                values[j] = temporary # move the saved value into the other position
    middle = len(values) // 2 # find the middle position
    lower_half = values[:middle] # take the lower half of the data
    return median(lower_half) # find the median of the lower half

# function for upper quartile
def upper_quartile(data):
    if len(data) == 0: # if the list is empty, we can't calculate the upper quartile
        return None

    values = [] # make a new list so we don't change the original data

    for value in data: # go through every value in the original list
        values.append(value) # add each value to the new list

    for i in range(len(values)): # go through each position in the list
        for j in range(i + 1, len(values)): # compare it with the values after it
            if values[j] < values[i]: # check if the values are in the wrong order
                temporary = values[i] # temporarily save the first value
                values[i] = values[j] # move the smaller value into the first position
                values[j] = temporary # move the saved value into the other position

    middle = len(values) // 2 # find the middle position

    if len(values) % 2 == 0: # check if there is an even number of values
        upper_half = values[middle:] # take the upper half

    else: # if there is an odd number of values
        upper_half = values[middle + 1:] # leave out the middle value

    return median(upper_half) # find the median of the upper half

# function for interquartile range
def interquartile_range(data):
    if len(data) == 0: # if the list is empty, we can't calculate the interquartile range
        return None

    q1 = lower_quartile(data) # find the lower quartile
    q3 = upper_quartile(data) # find the upper quartile

    return q3 - q1 # subtract the lower quartile from the upper quartile

# function for variance
def variance(data):
    if len(data) == 0: # if the list is empty, we can't calculate the variance
        return None

    average = mean(data) # find the mean of the data

    total = 0 # start a running total at zero

    for value in data: # go through every value in the list
        difference = value - average # find how far the value is from the mean
        squared_difference = difference ** 2 # square the difference
        total = total + squared_difference # add it to the running total

    return total / len(data) # divide by the number of values to get the variance

# function for standard deviation
def standard_deviation(data):
    if len(data) == 0: # if the list is empty, we can't calculate the standard deviation
        return None

    data_variance = variance(data) # find the variance of the data

    return data_variance ** 0.5 # find the square root of the variance