def to_weird_case(string):
    newlist = ''
    up = True
    for let in string:
        newlist += let.upper() if up else let.lower()
        if let.isalpha():
            up = not up
    return newlist
strt = ("cats are awesome")
print to_weird_case(strt)

