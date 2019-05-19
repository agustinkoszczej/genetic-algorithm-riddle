import random
import copy
import numpy as np
from threading import Thread


class RandomSelection:

    @staticmethod
    def select(chromosomes):
        total_size = len(chromosomes)
        random.shuffle(chromosomes)
        quantity = np.random.randint(0, total_size)
        return chromosomes[:quantity]


class RankingSelection:

    @staticmethod
    def select(chromosomes):
        take = 100
        chromosomes.sort(key=lambda chromosome: chromosome.aptitude(), reverse=True)
        return chromosomes[:take]


class TournamentSelection:

    @staticmethod
    def select(chromosomes):
        winners = []
        threads = []
        tournament_iterations = 10

        for _ in range(tournament_iterations):
            thread = Thread(target=TournamentSelection.iteration, args=(chromosomes, winners))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return winners

    @staticmethod
    def iteration(chromosomes, winners):
        tournament = copy.deepcopy(chromosomes)
        random.shuffle(tournament)
        while len(tournament) > 1:
            candidates = [tournament.pop(), tournament.pop()]
            candidates.sort(key=lambda chromosome: chromosome.aptitude(), reverse=True)
            winner = candidates[0]
            tournament.insert(0, winner)
        winners.append(tournament[0])
