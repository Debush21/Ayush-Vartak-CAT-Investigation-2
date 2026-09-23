#funtion for mean 
def mean(data):
    #this function finds the average of a list of numbers that is provided to it
    if len(data) == 0: #if the list is empty without anything we can't calculate anything
        return None
    total = 0 #start a running total at zero
    for value in data: #go through every number in the list one by one
        total = total + value #add the current number to our running total
    return total / len(data) #divide the total by how many numbers there are to get