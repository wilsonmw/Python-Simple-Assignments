
def compare(list_one,list_two):
    if len(list_one)!=len(list_two):
        print "The lists are not the same."
        return

    index = 0
    while index<len(list_one):
        if list_one[index]!=list_two[index]:
            print "The lists are not the same."
            return
        index += 1
    print "The lists are identical."


compare(['celery','carrots','bread','milk',],['celery','carrots','bread','milk',])