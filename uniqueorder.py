import re
def unique_in_order(iterable):
    it = list(iterable)
    num = len(it)
    z = 0
    new = []
    while z < num:
        count = z + 1
        while count < num and it[z] == it[count]:
            count +=1
        new.append(it[z]) 
        z = count
    return new  
print unique_in_order('AAAABBBCCDAABBB')