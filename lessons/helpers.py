"""Demonstrate defining a moduole imported elsewhere"""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as moduole")



def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


# Idiom for making a modole able to run as a program
# or have its global defs imported elsewhere
if __name__ == "__main__":
    main()
else:
    # It is not idiomatic to have an else branch
    print(f"helpers.py was imported: {__name__}")
#print("helpers.py was evaluated")