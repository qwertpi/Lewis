
import random
number = random.randint(1, 100)

turns = 1
score = 55

guess = int(input("Guess a number between 1 and 100:"))
while guess != number:
    if guess < number:
        print("Too low, try again.")
        print("")
        guess = int(input("Guess a number betwwen 1 and 50:"))
        turns += 1
        if turns < 10:
        	score -= 5
    elif guess > number:
        print("Too high, try again.")
        print("")
        guess = int(input("Guess a number betwwen 1 and 50:"))
        turns += 1
		if turns < 10:
			score -= 5
    if guess == number:
        print("Well Done! You guessed correctly.")
        print("You completed the game in", turns, "turns")

print("Your score is", score)
