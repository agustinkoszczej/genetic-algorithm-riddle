from flow.person import Person, x_dim
from decimal import *
import numpy as np


class Chromosome:

    def __init__(self, custom_people=None):
        self.people = self.random_fill(custom_people)

    @staticmethod
    def random_fill(custom_people):
        if custom_people is None:
            new_people = []
            for _ in range(x_dim):
                new_people.append(Person())
            return new_people
        return custom_people

    def aptitude(self):
        return sum(self.calculate_points()) - self.penalization()

    def mutate(self):
        self.people[np.random.randint(0, x_dim)].mutate()

    def calculate_points(self):
        points = [
            self.rule_one(), self.rule_two(), self.rule_three(), self.rule_four()
            , self.rule_five(), self.rule_six(), self.rule_seven(), self.rule_eight()
            , self.rule_nine(), self.rule_ten(), self.rule_eleven(), self.rule_twelve()
            , self.rule_thirteen(), self.rule_fourteen(), self.rule_fifteen()
        ]
        return points

    def penalization(self):
        names = list(map(lambda person: person.name, self.people))
        professions = list(map(lambda person: person.profession, self.people))
        vehicles = list(map(lambda person: person.vehicle, self.people))
        checkins = list(map(lambda person: person.checkin, self.people))
        watchings = list(map(lambda person: person.watching, self.people))

        names_penalization = 0 if len(names) == len(set(names)) else 1
        professions_penalization = 0 if len(professions) == len(set(professions)) else 1
        vehicles_penalization = 0 if len(vehicles) == len(set(vehicles)) else 1
        checkins_penalization = 0 if len(checkins) == len(set(checkins)) else 1
        watchings_penalization = 0 if len(watchings) == len(set(watchings)) else 1

        return names_penalization + professions_penalization + \
               vehicles_penalization + checkins_penalization + watchings_penalization

    def describe_points(self):
        print(self.calculate_points())

    def rule_one(self):
        # 1. Who goes in a Motorbike is an Accountant
        for person in self.people:
            if person.vehicle == "Motorbike" and person.profession == "Accountant":
                return 1
        return 0

    def rule_two(self):
        # 2. The person who arrives earlier than everybody uses a car.
        for person in self.people:
            if person.checkin == Decimal(7) and person.vehicle == "Car":
                return 1
        return 0

    def rule_three(self):
        # 3. Santiago arrives one hour later than the person who watches comedy.
        who_watches_comedy = \
            next((person for person in self.people if person.name != "Santiago" and person.watching == "Comedy"), None)
        if who_watches_comedy is not None:
            for person in self.people:
                if person.name == "Santiago" and person.checkin - who_watches_comedy.checkin == Decimal(1):
                    return 1

        return 0

    def rule_four(self):
        # 4. Sonia arrives one hour and a half after the person who is a police.
        sonia = next((person for person in self.people if person.name == "Sonia"), None)
        if sonia is not None:
            for person in self.people:
                if person.profession == "Police" and sonia.checkin - person.checkin == Decimal(1.5):
                    return 1

        return 0

    def rule_five(self):
        # 5. The person who watches comedy is a professor.
        for person in self.people:
            if person.watching == "Novel" and person.profession == "Professor":
                return 1

        return 0

    def rule_six(self):
        # 6. The merchant goes to work after the person who goes in a car.
        who_goes_in_a_car = next((person for person in self.people if person.vehicle == "Car"), None)
        if who_goes_in_a_car is not None:
            for person in self.people:
                if person.profession == "Merchant" and who_goes_in_a_car.checkin < person.checkin:
                    return 1

        return 0

    def rule_seven(self):
        # 7. The person who goes in a van arrives one hour later than Juan.
        who_goes_in_a_van = next((person for person in self.people if person.vehicle == "Van"), None)
        if who_goes_in_a_van is not None:
            for person in self.people:
                if person.name == "Juan" and who_goes_in_a_van.checkin - person.checkin == Decimal(1):
                    return 1

        return 0

    def rule_eight(self):
        # 8. Who arrives at 8.00 hs arrives at an average hour.
        return 1

    def rule_nine(self):
        # 9. The person who watches movies arrives later than everybody.
        max_checkin = max(map(lambda person: person.checkin, self.people))
        for person in self.people:
            if person.watching == "Movies" and person.checkin == max_checkin:
                return 1
        return 0

    def rule_ten(self):
        # 10. The person who goes in a bicycle arrives 30 minutes after Sonia.
        sonia = next((person for person in self.people if person.name == "Sonia"), None)
        if sonia is not None:
            for person in self.people:
                if person.name != "Sonia" and person.vehicle == "Bicycle" and person.checkin - sonia.checkin == Decimal(
                        0.5):
                    return 1

        return 0

    def rule_eleven(self):
        # 11. Who watches Soccer arrives at 8.30hs at work.
        for person in self.people:
            if person.watching == "Soccer" and person.checkin == Decimal(8.50):
                return 1

        return 0

    def rule_twelve(self):
        # 12. Who watches a soap opera arrives 1 hour earlier than Antonella.
        who_sees_soap = next((person for person in self.people if person.watching == "Novel"), None)
        if who_sees_soap is not None:
            for person in self.people:
                if person.name == "Antonella" and who_sees_soap.checkin - person.checkin == Decimal(-1):
                    return 1

        return 0

    def rule_thirteen(self):
        # 13. Omar arrives at 7hs.
        for person in self.people:
            if person.name == "Omar" and person.checkin == Decimal(7):
                return 1

        return 0

    def rule_fourteen(self):
        # 14. Who watches a series goes to work before the person who goes in a bus.
        who_sees_series = next((person for person in self.people if person.watching == "Series"), None)
        who_goes_in_bus = next((person for person in self.people if person.vehicle == "Bus"), None)

        if who_sees_series is not None and who_goes_in_bus is not None:
            if who_sees_series.checkin < who_goes_in_bus.checkin:
                return 1

        return 0

    def rule_fifteen(self):
        # 15. The person who is an engineer goes to work one hour after the person who is an Accountant.
        engineer = next((person for person in self.people if person.profession == "Engineer"), None)
        if engineer is not None:
            for person in self.people:
                if person.profession == "Accountant" and engineer.checkin - person.checkin == Decimal(1):
                    return 1

        return 0
