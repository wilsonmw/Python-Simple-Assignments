def coinToss():
    import random
    count = {"heads":0, "tails":0}
    while count["heads"]+count["tails"]<5000:
        tossinit = random.random()
        toss = round(tossinit)
        if toss == 0:
            count["heads"]=count["heads"]+1
            print "Attempt #" + str(count["heads"]+count["tails"]) + ": It's heads! ... Got " +str(count["heads"]) +" heads so far and " + str(count["tails"]) + " tails so far."
        if toss == 1:
            count["tails"]=count["tails"]+1
            print "Attempt #" + str(count["heads"]+count["tails"]) + ": It's tails! ... Got " +str(count["heads"]) +" heads so far and " + str(count["tails"]) + " tails so far."
        
coinToss()
