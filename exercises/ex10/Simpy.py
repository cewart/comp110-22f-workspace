"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730551195"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor that initilizes the values of thr Simpy arguments."""
        self.values = values

    def __repr__(self) -> str:
        """Automagically called when a Simpy object is converted to its str representation."""
        return f"Simpy({self.values})"

    def fill(self, values: float, number: int) -> None:
        """Fills Simpy's values with a specific number of repeating values."""
        self.values = []
        for _ in range(number):
            self.values.append(values)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with range of values- works like range function, but with floats."""
        self.values = []
        assert step != 0.0
        i: float = start
        j: int = 0
        if stop < start:
             while i > stop:
                if len(self.values) == 0:
                    self.values.append(start)
                else: 
                    self.values.append(self.values[j - 1] + step)
                i += step
                j += 1
        else:
            while i < stop:
                if len(self.values) == 0:
                    self.values.append(start)
                else: 
                    self.values.append(self.values[j - 1] + step)
                i += step
                j += 1

    def sum(self) -> float:
        """Compute then return the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Returns a new Simpy object that is the sum of each index of two lists."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Returns a new Simpy object whose values are the power of the another Simpy at the same index, or a float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask whose values represent True if the values of two Simpys match or a Simpy and a float, and False otherwise."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.values.append(True)
                else:
                    result.values.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.values.append(True)
                else:
                    result.values.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask whose values represent True if the value of a Simpy is greater than a second Simpy's corresponding value, or a float; False otherwise."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.values.append(True)
                else:
                    result.values.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.values.append(True)
                else:
                    result.values.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Uses index subsription to return the item in a Simpy at a certain index."""
        if isinstance(rhs, int):
            i: int = 0
            while i < len(self.values):
                if i == rhs:
                    return self.values[i]
                i += 1
        else:
            result: Simpy = Simpy([]) 
            for j in range(len(self.values)):
                if rhs.values[j] == True:
                    result.values.append(self.values[j])
            return result

