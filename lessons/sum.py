"""Example of testing a test subject"""


def sum(xs: list[float]) -> float:
    """Compute sum of a list."""
    total: float = 0.0
    # i: int = 0
    # while i < len(xs):
    #     total += xs[i]
    # i += 1
    for x in xs:
        total += x
    return total

