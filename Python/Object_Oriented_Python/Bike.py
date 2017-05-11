class bike(object):
    def __init__(self, name, price, max_speed):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.name
        print "The price of this bike is ${}".format(self.price)
        print "The max speed is {} mph".format(self.max_speed)
        print "This bike went {} miles".format(self.miles)
        return self
    def ride(self):
        print "Taking a joyride..."
        self.miles += 10
        return self
    def reverse(self):
        print "SCCRRTTT! Went the wrong way. Reversing..."
        self.miles -= 5
        return self

street_bike = bike("street_bike",10000,250)
street_bike.ride().ride().ride().reverse().displayInfo()
print "-"*10
cruiser = bike("cruiser",30000, 300)
cruiser.ride().ride().ride().reverse().displayInfo()
print "-"*10
indian = bike("indian", 50000, 300)
indian.ride().ride().ride().reverse().displayInfo()
