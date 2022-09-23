import random

number = random.randint(1, 100)
guesses = []
print("This is a guesssing game. You guess a number between 1 and 100 and it tells you if you are close.")


guess = int(input("What is your first guess: "))
guesses.append(guess)
while guess != number:
    if abs(guess-number) <= 3:
        print("You are BURNING!")
    elif abs(guess-number) <= 10:
        print("You are warm")
    else:
        print("You are cold.")
    guess = int(input("What is your next guess: "))
    guesses.append(guess)

print(f"You got the number in {len(guesses)} tries.\n Your guesses were: \n {guesses}")