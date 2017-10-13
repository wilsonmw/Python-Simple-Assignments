def odd_even():
    count = 1
    while count <= 2000:
        print "Number is " + str(count)
        if count%2 == 0:
            print "This is an even number."
        else:
            print "This is an odd number."
        count = count+1

odd_even()

def multiply(myList, mult):
    newList = []
    for myNum in myList:
        newList.append(myNum*mult)
    print newList
    return newList

multiply([2,5,10,20],5)


def layered_multiples(arr):
    new_array=[]
    for index in arr:
        newindex = 0
        subarr = []
        while newindex <index:
            subarr.append(1)
            newindex = newindex +1
        new_array.append(subarr)
    print new_array
    return new_array

layered_multiples(multiply([2,4,5,],3))
