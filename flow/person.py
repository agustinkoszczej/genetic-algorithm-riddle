import numpy as np
from decimal import *

# How many values are possible in each category
x_dim = 5

people = ["Juan", "Omar", "Antonella", "Santiago", "Sonia"]
professions = ["Accountant", "Police", "Professor", "Merchant", "Engineer"]
vehicles = ["Motorbike", "Car", "Van", "Bicycle", "Bus"]
checkins = [Decimal(7), Decimal(7.50), Decimal(8), Decimal(8.50), Decimal(9)]
watchings = ["Comedy", "Novel", "Movies", "Soccer", "Series"]


class Person:
    def __init__(self):
        self.name = people[np.random.randint(0, x_dim)]
        self.profession = professions[np.random.randint(0, x_dim)]
        self.vehicle = vehicles[np.random.randint(0, x_dim)]
        self.checkin = checkins[np.random.randint(0, x_dim)]
        self.watching = watchings[np.random.randint(0, x_dim)]

    def description(self):
        return [self.name, self.profession, self.vehicle, self.checkin, self.watching]

    def mutate(self):
        # print("--- Mutating ---")
        description = self.description()
        # print("Previous values:", description)
        mutation_idx = np.random.randint(0, x_dim)
        while True:
            random_values = Person().description()
            if description[mutation_idx] != random_values[mutation_idx]:
                break
        # print("Mutating:", description[mutation_idx], random_values[mutation_idx])
        description[mutation_idx] = random_values[mutation_idx]
        # print("Mutated:", description)
        self.name = description[0]
        self.profession = description[1]
        self.vehicle = description[2]
        self.checkin = description[3]
        self.watching = description[4]
