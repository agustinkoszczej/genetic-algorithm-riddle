import random

mutation_rate = .6


class SimpleMutation:

    @staticmethod
    def mutate(chromosomes):
        for chromosome in chromosomes:
            if random.random() < mutation_rate:
                chromosome.mutate()
        return chromosomes

# TODO: Other mutation methods
