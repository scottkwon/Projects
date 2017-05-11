def mult_table():
    i = 1
    while i < 13:
        n = 1
        while n < 13:
            print "%4d" % (i*n),
            n+=1
        print()
        i+=1
mult_table()
