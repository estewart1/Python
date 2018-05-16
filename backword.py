def backwards(word):
    word = word.split()
    word.reverse()
    return " ".join(word)
#    return back
msg = "I love New York"
print backwards(msg)