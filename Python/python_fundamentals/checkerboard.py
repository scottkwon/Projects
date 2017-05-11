#Make a checkerboard with stars and spaces!
#Make it populate by itself.

def check():
  for i in range(1,8):
    if i % 2 != 0:
      print "* * * *"
    elif i % 2 == 0:
      print " * * * *"

check()

#output
#* * * *
# * * * *
#* * * *
# * * * *
#* * * *
# * * * *
#* * * *
# * * * *
