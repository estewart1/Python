
def xo(s):
    S = s.lower()
    if s.count('x') == s.count('o'):
        return True
    else:
        return False
s = 'xox'
print (xo(s))

