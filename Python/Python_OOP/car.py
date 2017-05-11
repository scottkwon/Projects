class car(object):
    def __init__(self, name, price, speed, fuel, mileage):
        self.speed = speed
        self.fuel_level = fuel
        self.mileage = mileage
        self.price = price
        if self.price >= 10000:
            print "Tax: {}".format(.15)
        else:
            print "Tax: {}".format(.12)
        self.name = name
        self.price = price
    def display_all(self):
        print "Car Make: {}".format(self.name)
        print "Price: ${}".format(self.price)
        print "Speed: {} mph".format(self.speed)
        print "Fuel: {}".format(self.fuel_level)
        print "Mileage: {} mpg".format(self.mileage)
        print "-" * 10
        return self

toyota = car("Toyota", 30000, 120, "Full", 30)
toyota.display_all()

honda = car("Honda", 20000, 110, "Almost Empty", 32)
honda.display_all()

smart = car("Smart", 9000, 65, "Full", 35)
smart.display_all()
