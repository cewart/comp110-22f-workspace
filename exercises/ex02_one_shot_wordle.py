"""This is my one shot wordle 9/6/22!"""

__author__ = "730551195"

secret_word = "python"

"""Define named constants for whte, green, and yellow boxes."""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""User inputs their guess here, which must match the length of secret_word."""
user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not { len(secret_word) } letters! Try again: ")

i = 0
index_of_guess = i
emoji_sequence = ""

"""The real meat of the program: the loop that evaluates the user's guess.
The first else statement runs through each index of the guess and compares it to secret_word in order to print yellow emojis."""
while i < len(secret_word):
    if user_guess[i] == secret_word[i]:
        emoji_sequence = emoji_sequence + GREEN_BOX
    else:
        letter_anywhere = bool(False)
        other_indicies = int(0)
        while letter_anywhere is not True and other_indicies < len(secret_word):
            if secret_word[other_indicies] == user_guess[i]:
                letter_anywhere = bool(True)
            else:
                other_indicies = other_indicies + int(1)
        if letter_anywhere is True:
            emoji_sequence = emoji_sequence + YELLOW_BOX
        else:
            emoji_sequence = emoji_sequence + WHITE_BOX
    i = i + 1
print(emoji_sequence)

if user_guess != secret_word:
    print("Not quite. Play again soon!")

if user_guess == secret_word:
    print("Woo! You got it!")