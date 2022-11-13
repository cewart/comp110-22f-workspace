"""Examples pf optional parameters and Union types"""

from typing import Union

def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else:
        greeting += "ALien Life from Sector " + str(name)
    return greeting


#Single-argument
print(hello("Sally"))

# No argument
print(hello())

# int argument works too
print(hello(110))
print(hello(3.14))

def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result

print(add(110.0, "100.0"))