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

