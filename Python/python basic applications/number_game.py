import random
def game():
    secret_number = random.randint(1,10)
    guesses = []

    while len(guesses) < 5:
        try:
            guess = int(input("Guess a number 1-10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            if guess == secret_number:
                print("Hit")
            else:
                print("Miss")
            guesses.append(guess)
game()
