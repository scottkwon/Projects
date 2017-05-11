l = ['magical unicorns',19,'hello',98.98,'world']
l1 = [2,3,1,7,4,12]
l2 = ['magical','unicorns']

def show():
    print("""
    Please enter a list to transform!
    """)

def list_sorter(list):
    show()
    #usr_input = input("> ")
    sum = 0
    new_string = ""
    is_str = False
    is_num = False
    for item in list:
        if type(item) == str:
            new_string += " " + item
            is_str = True
        elif type(item) == int or float:
            sum += item
            is_num = True
    print "Your sum is {}".format(sum)
    print 'Your new string is "{}"'.format(new_string)
    if is_str == True and is_num == False:
        print "Your input is of string type"
    elif is_num == True and is_str == False:
        print "Your input is of integer/float type"
    elif is_str == True and is_num == True:
        print "Your input is of mixed type"

list_sorter(l)
list_sorter(l1)
list_sorter(l2)
