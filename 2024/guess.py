# Students review the code and identify the bugs in the code and improvements that can be made.

import random
import math

lower = 1
upper = 50
attempts = 6

x = random.randint(lower, upper)

print("\n\tYou have ", attempts," chances to guess the number!\n")

count = 1

while count < attempts:
    count += 1
    guess = int(input("Attemp #" + str(count) + " guess a number:- "))

    if x == guess:
        print("Congratulations you did it in %d attempts" % count)
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

if count > attempts:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
