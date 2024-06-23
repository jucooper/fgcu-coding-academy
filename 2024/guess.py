# Students review the code and identify the bugs in the code and improvements that can be made.
# The code is a simple number guessing game where the user has to guess a number between 1 and 50.

import random
import math

lower = 1
upper = 50
attempts = 6

x = random.randint(lower, upper)

print("\n\tYou have ", attempts," attempts to guess the number.\n")

count = 1

while count < attempts:
    count += 1
    guess = int(input("Attemp #" + str(count) + " guess a number:- "))

    if x == guess:
        print("Congratulations! You guessed correctly.")
        break
    elif x > guess:
        print("You guessed too small.")
    elif x < guess:
        print("You guessed too high.")

if count >= attempts:
    print("Better luck next time! The number was %d." % x)
