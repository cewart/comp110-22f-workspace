"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730551195"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> int:
        """Returns distance between the point object the method was called upon and another point passed as a parameter."""
        distance_between: int = sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return distance_between


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassign to the location attribute: the result of adding current location with self.direction"""
        self.location = self.location.add(self.direction)
        if self.is_infected() == True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Assign infected constant to the sickness attribute of the Cell object the method is called on."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns True if the cell's sickness is VULNERABLE, but is False otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Will return True if the cell is INFECTED and returns False otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
        
    def color(self) -> str:
        """Returns "gray" if the cell is vulnerable and "maroon" if the cell is infected."""
        if self.is_vulnerable() == True:
            return "gray"
        if self.is_infected() == True:
            return "maroon"
        if self.is_immune() == True:
            return "aquamarine"

    def contact_with(self, other: Cell) -> None:
        """If either cell of the parameter is infected while the other is vulnerable, the other cell will become infected."""
        if self.is_infected() == True and other.is_vulnerable() == True:
            other.contract_disease()
        if other.is_infected() == True and self.is_vulnerable() == True:
            self.contract_disease()

    def distance(self, other: Cell) -> int:
        """Returns distance between the cell object the method was called upon and another cell passed as a parameter."""
        distance_between: int = sqrt((other.location.x - self.location.x)**2 + (other.location.y - self.location.y)**2)
        return distance_between

    def immunize(self) -> None:
        """Method which assigns the immube constant to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True when the cell's sickness attribute is equal to the immune constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
        
class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int):
        """Initialize the cells with random locations and directions."""
        self.population = []
        infected = constants.START_INFECTED
        if infected >= cells or infected <= 0:
            raise ValueError("Some number of cells, but not all of the cells must be infected to begin.")
        immune = constants.START_IMMUNE 
        if immune >= cells or immune < 0:
            raise ValueError("Some number of cells, but not all of the cells must be immune to begin.")
        for i in range(0, cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            if i in range(infected):
                self.population[i].contract_disease()
            if i in range(infected, infected + immune):
                self.population[i].immunize()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in range(len(self.population)):
            if self.population[i].is_infected() == True:
                return False
        return True

    def check_contacts(self) -> None:
        """Compares the distance between every teo cell's locations, and if their distance is less than their radius, then they have had contact."""
        for i in range(len(self.population)):
            for j in range(len(self.population)):
                if j != i:
                    if self.population[i].distance(self.population[j]) < constants.CELL_RADIUS:
                        self.population[i].contact_with(self.population[j])