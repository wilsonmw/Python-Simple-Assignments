def multiplicationTable():
    x = 1
    mult = 1
    while mult<=12:
        while x <=12:
            digit = x * mult
            print digit,
            x+=1
        mult+=1
        x=1
        print ""

multiplicationTable()