
def xo(s):
    S = s.lower()
    if s.count('x') == s.count('o'):
        return True
    else:
        return False
s = 'xox'
print (xo(s))

""" If letters appear the same # of times, function 
returns true. If they appear a different # of times,
function returns false. """

