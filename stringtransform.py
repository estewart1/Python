import re
def string_transformer(s):
    newlist = []
    comp = re.compile(r's/^\s+|\s+$|\s+(?=\s)//g')
    s = re.sub(comp, '', s)
    for char in s:
        if char.islower():
            up = char.upper()
            newlist.append(up)
        else:
            low = char.lower()
            newlist.append(low)
    transform = ''.join(newlist)
    back = transform.split()
    back.reverse()
    return " ".join(back)
word = "IdInA  mEnZeL "
print string_transformer(word)