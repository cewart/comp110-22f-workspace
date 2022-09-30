"""Examples od the tuple and range sequences, 9/29/22."""

# An example of a tuple without range aliasing
goat: tuple[str, int] = ("M3", 23)

#Tuples are sequences, so they're 0-indexed
print(goat[0])
print(goat[1])

#Sequences have lengths
print(len(goat))

#print both items on same line
print(f"{goat[0]} is number ... ")
#Sequences are iterable with for... in loops
# Meaning you can loop over them with for...in
for item in goat:
    print(item)

# Tuples, unlike lists, are inmutable
# which means we cannot reassign items, or append, nor pop, etc.
# goat[0] = "LBJ"

# We cannot "invent" our own type without a type alias
Player = tuple[str, int]

# Once we've aliased a type, we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# In a strnage world where jersey numers change...
unc_poy = (unc_poy[0], unc_poy[1] + 1)



# A range is another common sequence type
zero_to_nine: range = range(0, 10, 1)

print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

# Can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)


names: list[str] = ["Kris", "Alyssa", "Michael", "Lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")

for i in range(0, len(names), 2):
     print(f"{i}. {names[i]}")

     print(odds_to_99.stop)