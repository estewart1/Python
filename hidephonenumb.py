def hide_phone_number(n):
        if n[0] == '+' or n[0] == '0':
            return ( str(n[0:9]) + 'xx.xxxx' )
        elif n[0] == '1':
            return ( str(n[0:7]) + 'xx-xxxx' )
        else:
            return False

print hide_phone_number("1-123-456-1234")