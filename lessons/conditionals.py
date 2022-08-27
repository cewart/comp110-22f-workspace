"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a value between 1-5, what is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guesses correctly!!!")
    print("Have a wonderful day!!!")
else:
    print("Sorry, you guesses incorrectly :(")
    if guess > SECRET:
        print("you guessed too high!")
    else:
        print ("You guesses too low!")  

print("Game over.")