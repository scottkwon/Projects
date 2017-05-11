class Caller(object):

    def __init__(self, id, name, phonenum, timecalled, reason):
        self.id = id
        self.name = name
        self.phonenum = phonenum
        self.timecalled = timecalled
        self.reason = reason

    def printall(self):
        print "Hello {}!".format(self.name)
        print "Your unique id is: {}".format(self.id)
        print "You are calling from the number: {}".format(self.phonenum)
        print "Your time of call was at: {}".format(self.timecalled)
        print """
        The reason you called today was:
        {}
        """.format(self.reason)
        return self

class CallCenter(object):

    def __init__(self):
        self.calls = []
        self.qsize = 0

    def add(self, caller):
        self.calls.append(caller)
        self.qsize += 1
        return self

    def delete(self, caller):
        self.calls.pop(0)
        self.qsize -= 1
        return self

    def callerinfo(self):
        for val in self.calls:
            print "Name: {}".format(val.name)
            print "Phone number: {}".format(val.phonenum)
        print "People in Queue: {}".format(self.qsize)
        return self

caller1 = Caller("a1b2c3", "scott", "6616616666", "12:30AM", "headache")
caller2 = Caller("a1b2c3", "steve", "6616616666", "12:30AM", "headache")
caller3 = Caller("a1b2c3", "phil", "6616616666", "12:30AM", "headache")
CallCenter = CallCenter()
CallCenter.add(caller1).add(caller2).add(caller3)
CallCenter.callerinfo()
