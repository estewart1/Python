def is_palindrome(string):
    string = str(string)
    if (string == string[::-1]):
        return True
    else:
        return False

st = 123456
print is_palindrome(st)