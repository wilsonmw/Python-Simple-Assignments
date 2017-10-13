class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *num):
        numadd = 0
        for i in range(0,len(num)):
            if isinstance(num[i],list) or isinstance(num[i],tuple):
                addEmUp = 0
                for k in range(0, len(num[i])):
                    addEmUp = addEmUp + num[i][k]
                numadd=numadd+addEmUp
                i = i+1
            else:
                numadd=numadd+num[i]
        self.total = self.total + numadd
        return self

    def subtract(self, *num2):
        numsub = 0
        for i in range(0,len(num2)):
            if isinstance(num2[i],list) or isinstance(num2[i],tuple):
                addEmUp = 0
                for k in range(0, len(num2[i])):
                    addEmUp = addEmUp + num2[i][k]
                numsub=numsub+addEmUp
                i = i+1
            else:
                numsub=numsub+num2[i]
        self.total = self.total - numsub
        return self

    def result(self):
        print self.total
        return self


MathDojo().add(2).add(2,5).subtract(3,2).result()

MathDojo().add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result()

MathDojo().add((1,2)).add([3,5,7,9],[1,6,9]).subtract((5,7,9)).result()

