def sumDigits(number): 
    sumy = int(abs(number))
    total = list(sumy[0]) 
    total2 = list(sumy[1])
    return total
num = int(raw_input('Enter a number: '))
print sumDigits(num)
# split num + add abs val
# Need to fix, doesn't work right now