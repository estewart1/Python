# def maps(a):
#     return a * 2
# pass
# listy = [1,2]
# func = list(map(maps, listy))
# print func

def maps(a):
    lst = []
    for i in a:
        lst.append(i*2)
    return lst
print maps([1,2,3])