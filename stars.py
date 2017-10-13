def draw_stars(starList):
    for index in starList:
        num=0
        while num < index:
            print "*",
            num = num+1
        print ""
draw_stars([2,6,1,4,8,2,4])

def stars2(starList):
    for item in starList:
        if isinstance(item, int):
            num=0
            while num<item:
                print "*",
                num = num +1
            print ""
        if isinstance(item, str):
            num = 0
            while num<len(item):
                print item[0],
                num=num+1
            print ""

stars2([5,"hello","yo",2,5,"spectacular",3,"seriously"])

