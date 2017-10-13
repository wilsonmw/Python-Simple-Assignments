class Car(object):       
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        def display_all(self):
            print "Price: $" + str(self.price)
            print "Speed: " + str(self.speed) + " mph"
            print "Fuel: " + str(self.fuel) 
            print "Mileage: " + str(self.mileage) + " mpg"
            print "Tax: " + str(self.tax)
        display_all(self)


car1 = Car(25000, 250, "Full tank", 17)
car2 = Car(5000, 55, "Empty", 27)
car3 = Car(7000, 56, "Full", 98)
car4 = Car(78000, 674, "Half Full", 58)
car5 = Car(548, 9, "Quarter tank", 59)
car6 = Car(158000, 987, "Empty", 2)
