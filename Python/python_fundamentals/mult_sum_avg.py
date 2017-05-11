#multiples
#pt1 print all odd numbers 1-1000 without using a list
def oddnum():
    for num in range(1,1000):
        if num%2 != 0:
            print num
print oddnum()
#pt2 print all multiples of 5 from 5-1,000,000
def fives():
    for x in range(5,100,5):
            print x
print fives()

#create a function that adds up all values in a list.
def summer(list):
    sum = 0
    for number in list:
        sum+=number
        print "The current sum is {}".format(sum)
summer([1, 2, 5, 10, 255, 3])

#create a function that finds the average of a given list.
def averager(list):
    sum = 0
    total_items = len(list)
    for number in list:
        sum+=number
    avg = int(sum/total_items)
    print "The average of the current list is {}".format(avg)
averager([1, 2, 5, 10, 255, 3])
