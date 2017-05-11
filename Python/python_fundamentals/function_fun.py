#create a function that counts from 1-2000.
#have it print the number (of current iteration) and specify whether it's odd or even
def even_odd():
    for i in range(1,2001):
        if i % 2 != 0:
            print "Number is {}. This is an ODD number".format(i)
        elif i % 2 == 0:
            print "Number is {}. This is an EVEN number".format(i)
even_odd()

#Create a function that iterates through each value in a list and returns a list where each value has been multiplied by num.
def multiply(l,num):
    for i in range(0,len(l)):
        l[i] = l[i]*num
    print l
    return l
multiply([2,4,10,16],10)

#use a function above to multiply two lists together to create a layered list! Use the multiply function above as an argument!

def layered_multiples(arr):
    new_list =[]
    for i in arr:
        new_input = []
        for j in range(i):
            new_input.append(1)
        new_list.append(new_input)
    return new_list
x = layered_multiples(multiply([2,4,5],3))
print x
#[6, 12, 15]
#[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
