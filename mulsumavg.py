
for odd in range(1, 1000, 2): #A loop that iterates through the range 1 to 1000, with a step of 2
    print odd   #prints the variable odd
  
for fives in range(5, 1000000, 5): # A loop that iterates through the range 5 to 1,000,000, with a step of 5
    print fives #prints the variable 'fives'

a = [1,2,5,10,255,3]    #creates the list 'a'
add = 0                 #creates the variable 'add'
for something in a:     #starts a loop, going through each iteration in list 'a'
    add=add+something   #adds the value of each index in list 'a' to the variable 'add'
print add               #prints the variable 'add', which is now the sum of all the values in list 'a'

a = [1,2,5,10,255,3]    #creates the list 'a'
add = 0                 #creates the variable 'add'
for something in a:     #starts a loop, going through each iteration in list 'a'
    add=add+something   #adds the value of each index in list 'a' to the variable 'add'
avg = add/len(a)        #creates the variable 'avg' and makes it equal to the 'add' divided by the length of list 'a'
print avg               #prints the variable 'avg', which is now the average of all the values in list 'a'
