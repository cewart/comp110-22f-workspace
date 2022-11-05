"""Example of a class and objects instantiation 10/25/22"""



class Pizza:
    """Models the idea of a Pizza"""

    # Attribute definitions
    size: str = "small"
    toppings: int = 0
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialiation of attributes."""
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float:
        """Calculate the price of a pizza"""
        total: float = 0.0
        if self.size == "large":
            total += 10.00
        else:
            total += 8.00

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        
        total *= tax

        return total


a_pizza: Pizza = Pizza("large", 3)
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")