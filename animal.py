
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.name + "'s Health: " + str(self.health)
        return self

myPet = Animal("Spot", 5000)

myPet.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):
    def __init__(self,name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health+=5
        return self

    
myDog = Dog("Rover", 3000)

myDog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170

    def fly(self):
        self.health -=10
        return self
    
    def dispHealth(self):
        super(Dragon,self).displayHealth()
        print "I am a Dragon."
        return self

drogo = Dragon("Drogo", 55000)

drogo.walk().run().fly().dispHealth()


myDog.run().displayHealth().pet().pet().pet().pet().displayHealth()

