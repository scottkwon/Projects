#find and print the position of the first instance of the word "day"
str = "It's thanksgiving day. It's my birthday,too!"
print "The first usage of day in this string started at the {}th position".format(str.find("day"))
#create a new string and replace the word "day" with "month"
new_string = str.replace("day", "month")
print new_string

#Define and call a function to find the min and max of any list.
def minmax(list):
    print min(list)
    print max(list)
print minmax([2,54,-2,7,12,98])

#Define and call a function to print/store the first and last items in a given list to make a new list containing said items.
def firstlast(list):
    x = []
    x.extend([list.pop(0),list.pop()])
    print x
print firstlast(["hello",2,54,-2,7,12,98,"world"])

#Sort a list, then split it in half. The first half of the list should be the first index of the second list.
def switcharoo(list):
    sorted_list = sorted(list)
    half = len(list)/2
    list1 = sorted_list[:half]
    print list1
    list2 = sorted_list[half-1:]
    print list2
    list2[0] = list1
    print list2
print switcharoo([19,2,54,-2,7,12,98,32,10,-3,6])
