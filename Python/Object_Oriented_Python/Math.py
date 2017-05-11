class Math(object):

    def __init__(self):
        pass
        self.total = 0

    def add(self, *args):
        for ar in args:
            if type(ar) is list or type(ar) is tuple:
                for j in range(0,len(ar)):
                    self.total += ar[j]
            else:
                self.total += ar
        return self

    def sub(self, *args):
        for ar in args:
            if type(ar) is list or type(ar) is tuple:
                for j in range(0,len(ar)):
                    self.total -= ar[j]
            else:
                self.total -= ar
        return self

    def total(self):
        print self.total()

print Math().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).sub(2, [2,3], [1.1, 2.3]).total
