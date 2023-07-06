import random as rnd

number = rnd.randint(1, 100)
guess = 0
score = 0

while guess != number:
    try:
        guess = int(input("Enter guess: "))
    except ValueError:
        score += 1
        print("Please enter a valid number!")
    
    if(guess < number):
        print("Guess higher!")
    elif(guess > number):
        print("Guess lower!")
    else:
        print(f"You won! Your score is {score}")
