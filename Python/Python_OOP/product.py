class product(object):
    def __init__(self, item, weight, brand, cost, status):
        self.item = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold!"
        return self
    def tax(self, float):
        total_with_tax = self.cost + (float * self.cost)
        print "Your total with tax is ${}".format(total_with_tax)
        return self
    def Return(self):
        reason = input("> ")
        if "defect" in reason:
            self.status = "Defective"
            self.cost = 0
        elif "in box" in reason:
            self.status = "Like New, For Sale"
        elif "open" in reason:
            self.status = "USED"
            self.cost = self.cost - (self.cost * .20)
        return self
    def display(self):
        print "Your item is {} {}".format(self.brand,self.item)
        print "The condition of your item is: {}".format(self.status)
        print "The price of your item is ${}".format(self.cost)
        print "The weight of your item is {} lbs".format(self.weight)
        return self

Shoes = product("Ultraboost", 0.2, "Adidas", 200, "For Sale")
Shoes.Return().display()
