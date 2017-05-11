def draw_stars(list):
    for item in list:
        if type(item) == int:
            print "*" * item
        elif type(item) == str:
            print item[:1] * len(list)
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

#output
#****
#ttt
#*
#mmmmmmm
#*****
#*******
#jjjjjjjjjjj
