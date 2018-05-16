def make_readable(seconds):
    if seconds >= 0 and seconds <= 359999:
        HH = str(seconds)[0:2]
        MM = str(seconds)[2:4]
        SS = str(seconds)[4:6]
        return (HH + ":" + MM + ":" + SS)
    else:
        return "It is not a number!"
sets = input("Give me a numbers for the time: ")
print make_readable(sets)
