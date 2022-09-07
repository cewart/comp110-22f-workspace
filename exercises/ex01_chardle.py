"""Exercise 1: Chardle (Wordle's little sister)!"""

__author__ = "730551195"

five_character_word: str = input("Enter a 5-character word: ")

if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

input_character: str = input("Enter a single character: ")

if len(input_character) != 1:
    print("Error: Character must be a single character.")
    exit()

instance_count: int = 0

print("Searching for " + input_character + " in " + five_character_word)

if input_character == five_character_word[0]:
    print(input_character + " found at index 0")
    instance_count = instance_count + 1

if input_character == five_character_word[1]:
    print(input_character + " found at index 1")
    instance_count = instance_count + 1

if input_character == five_character_word[2]:
    print(input_character + " found at index 2")
    instance_count = instance_count + 1

if input_character == five_character_word[3]:
    print(input_character + " found at index 3")
    instance_count = instance_count + 1

if input_character == five_character_word[4]:
    print(input_character + " found at index 4")
    instance_count = instance_count + 1

if instance_count == 1:
    print(str(instance_count) + " instance of " + input_character + " found in " + five_character_word)

if instance_count > 1:
    print(str(instance_count) + " instances of " + input_character + " found in " + five_character_word)

if instance_count < 1:
    print("No instances of " + input_character + " found in " + five_character_word)