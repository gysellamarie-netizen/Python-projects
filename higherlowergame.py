import random
from enum import nonmember

print("Welcome to the higher/lower game")

# Get valid lower and upper bounds
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

while lower_bound >= upper_bound:
    print("Invalid range")
    lower_bound = int(input("Re-enter the lower bound: "))
    upper_bound = int(input("Re-enter the upper bound: "))

# Generate random number
random_num = random.randint(lower_bound, upper_bound)
# Get guess
guess = None
while guess != random_num:
    guess = int(input("Guess the number: "))
    while guess < lower_bound or guess > upper_bound:
        print("Invalid guess")
        guess = int(input("Re-enter your guess: "))
    if guess < random_num:
        print("Your guess is too low")
    elif guess > random_num:
        print("Your guess is too high")
    else:
        print("You go it!")