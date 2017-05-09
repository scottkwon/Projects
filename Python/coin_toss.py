import random

def start():
    print """
    Starting the Coin flipping program...
    -------------------------------------
    """

def coin_flipper(num):
    start()
    head_count = 0
    tail_count = 0
    for flips in range(1,num+1):
        toss = random.randint(0,1)
        if toss == 1:
            face = "heads"
            head_count += 1
            print "Attempt # {}: Throwing a coin... It's {}! ... Got {} head(s) so far and {} tail(s) so far".format(flips, face, head_count, tail_count)
        else:
            face = "tails"
            tail_count += 1
            print "Attempt # {}: Throwing a coin... It's {}! ... Got {} head(s) so far and {} tail(s) so far".format(flips, face, head_count, tail_count)
coin_flipper(5)
