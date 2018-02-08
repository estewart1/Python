def duplicate_encode(word):
    word = word.lower()
    emptystring = ""
    for lett in word:
        if word.count(lett) == 1:
            emptystring += '(' 
        else:
            emptystring += ')'
    return emptystring  
wordy = "Success"
print duplicate_encode(wordy)
# Codewars kata