def validate_pin(pin):
    if not pin.isdigit():
        return False
    elif len(pin) == 4:
        return True
    elif len(pin) == 6:
        return True
    else: 
        return False
num = raw_input("Enter a number: ")
print validate_pin(num)
# Determines if pin number is 4 or 6 digits