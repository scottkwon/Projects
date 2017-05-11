def give_name():
    students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ]
    for i in students:
        full = " "
        for key in i:
            full = full + i[key] + " "
            #full+=" "
        print full
give_name()

def name_info():
    users = {
     'Students': [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
      ],
     'Instructors': [
         {'first_name' : 'Michael', 'last_name' : 'Choi'},
         {'first_name' : 'Martin', 'last_name' : 'Puryear'}
      ]
     }
    print "Students:"
    count1 = 1
    for i in users['Students']:
        full = ""
        for key in i:
             full = full + i[key] + " "
        print "{}".format(count1) + "-" + full+"-"+"{}".format(len(full)-2)
        count1+=1

    print "Instructors:"
    count2 = 1
    for i in users['Instructors']:
        full = ""
        for key in i:
             full = full + i[key] + " "
        print "{}".format(count2) + "-" + full+"-"+"{}".format(len(full)-2)
        count2+=1

name_info()

#output
#Students:
#1-Michael Jordan -13
#2-John Rosales -11
#3-Mark Guillen -11
#4-KB Tonel -7
#Instructors:
#1-Michael Choi -11
#2-Martin Puryear -13#
