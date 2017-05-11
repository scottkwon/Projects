#Compare two arrays and see if they are identical or not.
list1 = ['celery','carrots','bread','milk']
list2 = ['celery','carrots','bread','cream']

def compare_list(list1,list2):
    if list1 == list2:
        print "The lists are the same!"
    else:
        print "The lists are NOT the same"

compare_list(list1, list2)

#output
#"The lists are NOT the same"
