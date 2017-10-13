

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "Price: $" + str(self.price)
        print "Maximum speed: " + str(self.max_speed) + " MPH"
        print "Miles ridden: " + str(self.miles)

    def ride(self):
        print "Riding..."
        self.miles +=10

    def reverse(self):
        print "Reversing..."
        self.miles -=5

bike1 = Bike(4000, 265)
bike2 = Bike(43, 9)
bike3 = Bike(250, 35)


bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()


bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()
