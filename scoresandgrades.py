def grades():
    import random
    count = 1
    while count <= 10:
        score = random.randint(60, 100)
        print "Score: " + str(score) + ";",
        if score >= 60 and score<70:
            print "Your grade is D"
        if score >= 70 and score<80:
            print "Your grade is C"
        if score >= 80 and score<90:
            print "Your grade is B"
        if score >= 90 and score<=100:
            print "Your grade is A"
        count = count+1


grades()