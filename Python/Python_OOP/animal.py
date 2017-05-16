class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        if isinstance(self, Dragon):
            print "This is a DRAGON!"
        print "The current health of {} is: {}%".format(self.name,self.health)
        return self
class Dog(Animal):
    def __init__(self,health):
        super(Dog, self).__init__(health)
        self.health = 150
    def pet(self):
        self.health += 50
        return self
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self

Tiger = Animal("Tiger", 100)
Tiger.walk().walk().walk().run().run().displayHealth()
Dog = Dog("Puppy")
Dog.walk().walk().walk().run().run().pet().displayHealth()
Draco = Dragon("Draco")
Draco.walk().walk().walk().run().run().fly().fly().displayHealth()
