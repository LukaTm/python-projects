# TODO easy un hard leveli
# TODO easy ir 10 guessi un HARD ir 5

import random

print("Welcome to the Number Guessing Game!")
print("I am Thinking of a number between 1 and 100.")

random_number = random.choice(range(1, 101))


def easy():
    x = 0
    for guess in range(1, 15):  # vai arī vienkārsi skaiti 10 reizes if 10= 10 break
        make_guess = int(input("Make a guess: "))
        if make_guess > random_number:
            print("Too high")
        elif make_guess < random_number:
            print("Too low")
        if make_guess == random_number:
            print("You win")
            break
        x += 1
        if x == 10:
            print("You lost loser")
            break


def hard():
    x = 0
    for guess in range(1, 15):  # vai arī vienkārsi skaiti 10 reizes if 10= 10 break
        make_guess = int(input("Make a guess: "))
        if make_guess > random_number:
            print("Too high")
        elif make_guess < random_number:
            print("Too low")
        if make_guess == random_number:
            print("You win")
            break
        x += 1
        if x == 5:
            print("You lost loser")
            break


quest = input("Easy or hard: ")
if quest == "easy":
    easy()
else:
    hard()
