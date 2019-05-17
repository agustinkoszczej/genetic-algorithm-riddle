# -*- coding: utf-8 -*-
import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from flow.chromosome import Chromosome
from flow.crossover import SimpleCrossOver, ComplementBinomialCrossOver, DoubleBinomialCrossOver
from flow.mutation import SimpleMutation
from flow.selectors import RandomSelection, RankingSelection

random.seed(42)  # To reproduce a random (for testing)

# Number of possible solutions
n_chromosomes = 100


# Main Problem: ¿Who is the merchant? ¿Juan, Omar, Antonella, Santiago or Sonia?

def generate_chromosomes():
    chromosomes = []
    for number in range(n_chromosomes):
        chromosomes.append(Chromosome())
    return chromosomes


def plot(aptitudes):
    records = []
    for idx, aptitude in enumerate(aptitudes):
        records.append(
            {
                'iteration': idx,
                'aptitude': aptitude
            }
        )
    df = pd.DataFrame.from_records(records)
    sns.lineplot(x="iteration", y="aptitude", data=df)
    plt.show()


# Tools
selectors = {
    "random": RandomSelection(),
    "ranking": RankingSelection(),
}

cross_overs = {
    "simple": SimpleCrossOver(),
    "complement_binomial": ComplementBinomialCrossOver(),
    "double_binomial": DoubleBinomialCrossOver()
}

mutations = {
    "simple": SimpleMutation()
}


def main():
    population = generate_chromosomes()
    print("Population size:", len(population))
    best_aptitude = max(map(lambda c: c.aptitude(), population))
    iterations = 0
    aptitudes = list([best_aptitude])
    while best_aptitude < 15:
        print("Best aptitude:", best_aptitude)
        population.sort(key=lambda chromosome: chromosome.aptitude(), reverse=True)
        for person in population[0].people:
            print(person.description())
        population[0].describe_points()

        # 1 - Selection
        selected = selectors['ranking'].select(population)

        # 2 - Cross Over
        new_population = cross_overs['complement_binomial'].cross_over(selected)

        # 3 - Mutation
        population = mutations['simple'].mutate(new_population) + selected

        best_aptitude = max(map(lambda c: c.aptitude(), population))
        aptitudes.append(best_aptitude)
        print("------------------------------- End of iteration", iterations)
        iterations += 1

    population.sort(key=lambda chromosome: chromosome.aptitude(), reverse=True)
    print("*******************************")
    print("Final aptitude", best_aptitude)
    for person in population[0].people:
        print(person.description())
    print("*")
    print("**")
    print("***")
    print(">>> Artificial Intelligence baby ;) <<<")

    plot(aptitudes)


if __name__ == '__main__':
    main()
