"""My full Wordle program 9/13/22!"""

__author__: 730551195

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""Prior to code that runs wordle, I am defining functions which build upon one another and be called on in my main area later on."""

def contains_char(input_word: str, character_present: str) -> bool:
    """input_word can be any length and character_present must be len 1, will return true if the single character is present at any index of input_word; otherwise false."""
    assert len(character_present) == 1
    i:int = 0
    while i < len(input_word):
        if character_present == input_word[i]:
           return True
        i += 1
    return False

def emojified(input_word: str, secret_word: str) -> str:
    """This compares the guess word with the secret word and uses contains_char to contatonate a string of yellow or white boxes."""
    assert len(input_word) == len (secret_word)
    emoji_sequence = ""
    i: int = 0
    while i < len(input_word):
        if input_word[i] == secret_word[i]:
            emoji_sequence = emoji_sequence + GREEN_BOX
        else: 
            if contains_char(secret_word, input_word[i]) is True:
                emoji_sequence = emoji_sequence + YELLOW_BOX
            else:
                emoji_sequence = emoji_sequence + WHITE_BOX
        i += 1
    return emoji_sequence 

def input_guess (expected_length: int) -> str:
    """This function returns the user's guess until it matches the length of the secret word."""
    input_word: str = input(f"Enter a {expected_length} character word: ")
    while len(input_word) != expected_length:
        input_word = input(f"That was not { expected_length } letters! Try again: ")
    return input_word

def main() -> None:
    """Location of the Wordle program main game loop. The loop starts with a count of the turn, then invokes input_guess to match the word, then emojified to print the result, and finally tells if any guesses are left."""
    i: int = 0
    secret_word: str = "codes"
    input_result: str = ""
    while i < 6 and input_result != secret_word:
        print(f"=== Turn {i + 1}/6 ===")
        input_result = input_guess(len(secret_word)) 
        print(emojified(input_result, secret_word))
        if input_result == secret_word:
            print(f"You won in {i + 1}/6 turns!")
        if input_result != secret_word and i == 5:
            print("X/6 - Sorry, try again tomorrow!")
        i += 1

"""This statement allows this program to run as a module rather than inporting and calling a function."""
if __name__ == "__main__":
    main()