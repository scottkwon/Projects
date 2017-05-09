#Create random "scores" and grade them using the standard ABCDF rubric scale.
import random
test_score = int(raw_input("Please enter your test score:  "))

if test_score >= 90:
    grade = "A"
    print "Score: {}; Your grade is {}".format(test_score, grade)
elif test_score >= 80:
    grade = "B"
    print "Score: {}; Your grade is {}".format(test_score, grade)
elif test_score >= 70:
    grade = "C"
    print "Score: {}; Your grade is {}".format(test_score, grade)
elif test_score >= 60:
    grade = "D"
    print "Score: {}; Your grade is {}".format(test_score, grade)
else:
    grade = "F"
    print "You failed.. better luck next time!"
