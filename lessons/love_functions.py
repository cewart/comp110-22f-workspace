"""Some tender, loving functions 9/8/22."""

def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

# print(love("chris"))


def spread_love(to: str, n: int) -> str:
    """Generates a string sepeating a loving message n times"""
    love_note = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note