import re
def camel_case(string):
     string = string.title()
     string = "".join([str(let) for let in string] )
     space = re.compile(r'\s')
     newstring = re.sub(space, '', string)
     return newstring

print camel_case('hello world')