w = input("Please enter a string :") 
#here, w will be the string enterrd by the user
def most_frequent(string):
  # most_frequent is the function used to evaluate the string
    d = dict()
  # dictionary d is initialised  
    for key in string :
        if key not in d :
            d[key] = 1
        else :
            d[key] += 1
    # condition is applied so that if the element is present only once then it returns 1 else it adds how many times the element is repeated and returns the sum
    return d 
print(most_frequent(w))                
