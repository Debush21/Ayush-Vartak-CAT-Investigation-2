#funtion for mean 
def mean(data):
    #this function finds the average of a list of numbers that is provided to it
    if len(data) == 0: #if the list is empty without anything we can't calculate anything
        return None
    total = 0 #start a running total at zero
    for value in data: #go through every number in the list one by one
        total = total + value #add the current number to our running total
    return total / len(data) #divide the total by how many numbers there are to get

#funtion for minimum
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