def create_phone_number(n):
        n = "".join([str(num) for num in n] )
        return ("(" + str(n[0:3]) + ")" + str(n[3:6]) + "-" + str(n[6:10]))
inte = str(input("Give me numbers: ")) 
print create_phone_number(inte)
