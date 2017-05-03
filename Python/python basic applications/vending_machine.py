sodas = ['mountain dew', 'pepsi', '7up']
chips = ['fritos', 'doritos', 'cheetos']
candy = ['sour patch kids', 'gummy worms', 'chocolates']

while True:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()
    try:
        if choice.lower() == 'soda':
            snack = sodas.pop()
        elif choice.lower() == 'chips':
            snack = chips.pop()
        elif choice.lower() == 'candy':
            snack  = candy.pop()
        else:
            print("Not a valid option")
            continue
    except IndexError:
        print("We're all out of {}".format(choice))
    else:
        print("Here's your {}: {}".format(choice,snack))
