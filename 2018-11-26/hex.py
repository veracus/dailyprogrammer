def intToHex(value):
    return str(format(value, '02x')).upper()

def hexcolor(red, green, blue):
    return '#' + intToHex(red) + intToHex(green) + intToHex(blue)

def main():
    print (hexcolor(255, 99, 71))
    print (hexcolor(184, 134, 11))
    print (hexcolor(189, 183, 107))
    print (hexcolor(0, 0, 205))

main()