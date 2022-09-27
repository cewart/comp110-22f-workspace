"""Example of for in syntax 9/26/22"""

names: list[str] = ["Chris", "Kush", "Jake", "Dylan"] 

# Example of iterating through names using a while loop
print("while output")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for ... in loop is the same as the while loop above.
print("for...in output")
for name in names:
    print(name)