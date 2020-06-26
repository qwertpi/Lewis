
import random
number = random.randint(1, 100)

turns = 1
score = 0

guess = int(input("Guess a number between 1 and 100:"))
while guess != number:
    if guess < number:
        print("Too low, try again.")
        print("")
        guess = int(input("Guess a number betwwen 1 and 50:"))
        turns += 1
    elif guess > number:
        print("Too high, try again.")
        print("")
        guess = int(input("Guess a number betwwen 1 and 50:"))
        turns += 1
    if guess == number:
        print("Well Done! You guessed correctly.")
        print("You completed the game in", turns, "turns")

if turns == 1:
    score = 50
    print("Your score is", score)
    
elif turns == 2:
    score = 45
    print("Your score is", score)
    
elif turns == 3:
    score = 40
    print("Your score is", score)

elif turns == 4:
    score = 35
    print("Your score is", score)

elif turns == 5:
    score = 30
    print("Your score is", score)

elif turns == 6:
    score = 25
    print("Your score is", score)

elif turns == 7:
    score = 20
    print("Your score is", score)

elif turns == 8:
    score = 15
    print("Your score is", score)

elif turns == 9:
    score = 10
    print("Your score is", score)

elif turns >10:
    print("Your score is", score)
    score = 5
