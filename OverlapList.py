alist = [1,1,2,3,5,8,13,21,34,55,89]
blist = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def twolists(x,y):
    listy = []
    for num in set(x) & set(y):
        listy.append(num)
    return listy


print twolists(alist, blist)

""" Combines lists, taking out numbers if they
    appear multiple times """ 
