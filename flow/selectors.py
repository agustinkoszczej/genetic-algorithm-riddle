import random
import numpy as np


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
        take = 40
        chromosomes.sort(key=lambda chromosome: chromosome.aptitude(), reverse=True)
        return chromosomes[:take]

# TODO: Other selection methods
