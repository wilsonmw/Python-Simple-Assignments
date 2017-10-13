
def typelist(myList):
    sum = 0
    line = ""
    kind = 0
    for item in myList:
        if isinstance(item, int):
            sum += item
            kind = 1
        if isinstance(item, str):
            line += item
    if line == "" and sum != 0:
        print "The array you entered is of integer type."
        print "The sum of all your integers is " + str(sum)
        
    if line != "" and sum == 0 and kind == 0:
        print "The array you entered is of string type."
        print "Your strings all concatenated is " + line + ", which is ridiculous."
    if line != "" and kind == 1:
        print "The array you entered is of mixed type."
        print "The sum of all your integers is " + str(sum)
        print "Your strings all concatenated is " + line + ", which is ridiculous."


typelist([])
