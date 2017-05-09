#Find words with a particular character and print it in a new list!
#Please enter a list with only strings!

def find_char(list, char):
    new_list = []
    for item in list:
        for letter in item:
            if letter == char:
                new_list.append(item)
    print new_list

find_char(["hi", "scott", "you","zebra", "apple"], "o")

#output
#["scott", "you"]
