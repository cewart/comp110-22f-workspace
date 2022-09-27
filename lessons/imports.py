"""Examples of importing in Python"""


from lessons import helpers

#Alias a moduole / imported name as another name
from lessons import helpers as hp

#import names defined globally in a moduole
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2,4))
    print(f"The answer {helpers.THE_ANSWER}")
    print(powerful(2,4))
    print(THE_ANSWER)


if __name__ == "__main__":
    main()