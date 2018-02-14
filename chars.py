def remove_char(s):
    s = list(s)
    del s[0]
    del s[-1]
    s = "".join(s)
    return s
string = "cats"
print remove_char(string)
#Codewars kata 
# Removes 1st and last character of a word