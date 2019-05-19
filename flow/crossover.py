# -*- coding: utf-8 -*-
import copy
import itertools
from flow.chromosome import Chromosome


class SimpleCrossOver:

    @staticmethod
    def cross_over(chromosomes):
        cut = 3  # Cannot be higher than 5 (max of person's characteristics)
        children = []
        for mother, father in pairwise(map(lambda c: c.people, chromosomes)):
            child_m = Chromosome(copy.deepcopy(mother[:cut] + father[cut:]))
            child_f = Chromosome(copy.deepcopy(mother[cut:] + father[:cut]))
            children.append(child_m)
            children.append(child_f)

        return children

class ComplementBinomialCrossOver:

    @staticmethod
    def cross_over(chromosomes):
        mask = [1,0,1,0,1] #Mask that will define child A (1: coming from M, 0: coming from F)
        children = []
        for mother, father in pairwise(map(lambda c: c.people, chromosomes)):
            child_a = Chromosome(copy.deepcopy([mother[i] if gen else father[i] for i, gen in enumerate(mask)]))            
            child_b = Chromosome(copy.deepcopy([mother[i] if not gen else father[i] for i, gen in enumerate(mask)]))
            children.append(child_a)
            children.append(child_b)

        return children

class DoubleBinomialCrossOver:

    @staticmethod
    def cross_over(chromosomes):
        mask_child_a = [0,1,1,0,1] #[random.choice([0,1]) for i in range(5)]  # This is the mask defining child A (1: coming from M, 0: coming from F)
        mask_child_b = [1,1,0,0,1] #[random.choice([0,1]) for i in range(5)]  # This is the mask defining child B (1: coming from M, 0: coming from F)
        children = []
        for mother, father in pairwise(map(lambda c: c.people, chromosomes)):
            child_a = Chromosome(copy.deepcopy([mother[i] if gen else father[i] for i, gen in enumerate(mask_child_a)])) 
            child_b = Chromosome(copy.deepcopy([mother[i] if gen else father[i] for i, gen in enumerate(mask_child_b)])) 
            children.append(child_a)
            children.append(child_b)

        return children

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
