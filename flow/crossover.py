import copy
import itertools

from flow.chromosome import Chromosome


class SimpleCrossOver:

    @staticmethod
    def cross_over(chromosomes):
        cut = 3  # Cannot be higher than 5
        children = []
        for mother, father in pairwise(map(lambda c: c.people, chromosomes)):
            child_m = Chromosome(copy.deepcopy(mother[:cut] + father[cut:]))
            child_f = Chromosome(copy.deepcopy(mother[cut:] + father[:cut]))
            children.append(child_m)
            children.append(child_f)

        return children


# TODO: Other crossover methods

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
