import random

comp_guess = random.randint(1,100)

guesses = 0
LIMIT = 5

while guesses < LIMIT:
    your_guess = int(input("Guess a number 1-100: "))
    if your_guess == comp_guess:
        print("You got it! Good job!")
        guesses = 10000
    elif your_guess < comp_guess:
        print("Your guess is too low.")
        guesses += 1
        if guesses == LIMIT:
            print("You ran out of guesses.")
    elif your_guess > comp_guess:
        print("Your guess is too high.")
        guesses += 1
        if guesses == LIMIT:
            print("You ran out of guesses.")


