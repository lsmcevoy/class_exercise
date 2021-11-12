# classes_exercise.py

"""1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:

Attributes/properties:
    name: str
    max_speed: int
    capacity: int

    Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
"""


class Vehicle:
    def __init__(self):
        self.name = ""
        self.max_speed = 0
        self.capacity = 0

    def vroom(self):

"""This a vehicle that has the following 
      name: the vehicle name
      max_speed: the vehicle's maximum speed
      capacity: the amount of people the vehicle can carry"""


def vroom(self) -> None:
    print("Vroom" * self.max_speed)

"""Vroom multiplied by the speed of the vehicle"""



"""2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free"""


class Bus(Vehicle):
    """This is a kind of vehicle called bus that can carry people"""

    def fare(self, age: int) -> None:
        """Given the age it will tell the fare."""

        if 18 <= age <= 60:
            print("The fare of this bus ride is $5.00")
            """if someone is between the ages of 18 and 60, it will tell them the fare is $5"""
        else:
            print("Your ride is free.")
            """if someone is under 18 or over 60, it will tell the their ride is free"""


vehicle1 = Vehicle()
vehicle1.name = "Car"
vehicle1.max_speed = 100
vehicle1.capacity = 4
vehicle1.vroom()


bus1 = Bus()
bus1.name = 'A bus'
bus1.max_speed = 100
bus1.capacity = 40
bus1.vroom()
bus1.fare(20)
