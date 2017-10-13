words = "It's Thanksgiving day. It's my birthday, too!"
print words.find("day")

words2 = words.replace("day", "month")
print words2

x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

y = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print y[0], y[len(y)-1]
newlist = [y[0], y[len(y)-1]]
print newlist

z = [19,2,54,-1,7,12,98,32,10,-3,6]
z.sort()
w = z[0:len(z)/2]
v = z[len(z)/2:]
v.insert(0, w)
print v
