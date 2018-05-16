import string 
import re

def is_pangram(s):
    s = (re.sub('[,.\';@#?!$\d\s]', '', s).lower())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in s:
            return False
    return True

s = "This isn't a pangram!"
print is_pangram(s)