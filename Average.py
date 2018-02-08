def find_average(array):
    try:
       numlist =  sum(array) / int(len(array))
       return numlist
    except ZeroDivisionError:
        return 0

# Adds numbers in a list together and finds average