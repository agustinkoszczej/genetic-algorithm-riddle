import random

from flow.chromosome import Chromosome
from flow.crossover import SimpleCrossOver
from flow.mutation import SimpleMutation
from flow.selectors import RandomSelection, RankingSelection

random.seed(42)  # To reproduce a random (for testing)

# Hyper-parameters
n_chromosomes = 100


# ¿Who is the merchant? ¿Juan, Omar, Antonella, Santiago or Sonia?

def generate_chromosomes():
    chromosomes = []
    for number in range(n_chromosomes):
        chromosomes.append(Chromosome())
    return chromosomes


# Tools
selectors = {
    "random": RandomSelection(),
    "ranking": RankingSelection(),
}

cross_overs = {
    "simple": SimpleCrossOver()
}

mutations = {
    "simple": SimpleMutation()
}


def main():
    population = generate_chromosomes()
    print("Population size:", len(population))
    best_aptitude = max(map(lambda c: c.aptitude(), population))
    iter = 0
    while best_aptitude < 15:
        print("Best aptitude:", best_aptitude)
        population.sort(key=lambda chromosome: chromosome.aptitude(), reverse=True)
        for person in population[0].people:
            print(person.description())
        population[0].describe_points()

        # 1 - Selection
        selected = selectors['ranking'].select(population)

        # 2 - Cross Over
        new_population = cross_overs['simple'].cross_over(selected)

        # 3 - Mutation
        population = mutations['simple'].mutate(new_population) + selected

        best_aptitude = max(map(lambda c: c.aptitude(), population))
        print("------------------------------- End of iteration", iter)
        iter += 1

    population.sort(key=lambda chromosome: chromosome.aptitude(), reverse=True)
    print("*******************************")
    print("Final aptitude", best_aptitude)
    for person in population[0].people:
        print(person.description())
    print("*")
    print("**")
    print("***")
    print(">>> Artificial Intelligence baby ;) <<<")


if __name__ == '__main__':
    main()