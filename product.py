class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def addTax(self, tax):
        self.tax = tax
        self.price = (self.price*self.tax)+self.price
        return self

    def bringBack(self, reason):
        if reason == "Defective":
            self.status = "Defective"
            self.price = 0
        if reason == "Unopened":
            self.status = "For Sale"
        if reason == "Opened":
            self.status = "Used"
            self.price = self.price *0.80
        return self

    def display_all(self):
        print "Item: " + str(self.name)
        print "Brand: " + str(self.brand)
        print "Price: $" + str(self.price)
        print "Weight: " + str(self.weight) + "lb"
        print "Cost: $" + str(self.cost)
        print "Status: " + str(self.status)
        return self


rice = Product(5, "Rice", 5, "Uncle Ben's", 3,)
caviar = Product(349, "Caviar", 0.2, "Super Expensive", 9)

rice.sell().display_all().bringBack("Opened").addTax(.35).display_all()
caviar.display_all().sell().display_all().bringBack("Defective").display_all()


