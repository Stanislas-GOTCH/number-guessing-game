import random as rnd

number = rnd.randint(1, 100)
guess = 0
score = 0

while guess != number:
    guess = int(input("Enter guess: "))
    score += 1
    
    if(guess < number):
        print("Guess higher!")
    elif(guess > number):
        print("Guess lower!")
    else:
        print(f"You won! Your score is {score}")
