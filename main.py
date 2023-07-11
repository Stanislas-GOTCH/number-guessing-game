import time
import random as rnd

print("\nHello and welcome!")
time.sleep(1)
print("\nMy name is CPU.")
time.sleep(1)
name = input("What's yours? ")

print(f"\nOkay {name}, I'm thinking of a number between 0 and 20.")
time.sleep(1)

number = rnd.randint(1, 20)
guess = 0
score = 0

while guess != number:
    try:
        guess = int(input("Enter guess: "))
        score += 1
    except ValueError:
        print("Please enter a valid number!")
        continue

    if(guess < number):
        print("Guess higher!")
    elif(guess > number):
        print("Guess lower!")
    else:
        print(f"\nYou won! Your score is {score}.")
        print("Bye!\n")
