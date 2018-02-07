def maskify(cc):
    cc = str(cc)
    info = '#' * (len(cc[:-4]))
    return info + cc[-4:]

c = raw_input('Enter Private Information: ' )
print maskify(c)

# codewars kata
# Hides Private Info, except for the last 4 