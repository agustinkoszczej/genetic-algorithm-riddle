# -*- coding: utf-8 -*-
import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import csv
from flow.chromosome import Chromosome
from flow.crossover import SimpleCrossOver, ComplementBinomialCrossOver, DoubleBinomialCrossOver
from flow.mutation import SimpleMutation
from flow.selectors import RandomSelection, RankingSelection, TournamentSelection

random.seed(42)  # To reproduce a random (for testing)

# Number of possible solutions
n_chromosomes = 100

# Input parameters
# SELECTOR = ['random, ranking, tournament']
# CROSS-OVER = ['simple, complement_binomial, double_binomial']
# MUTATION = ['simple']

in_parameters = ['ranking', 'simple', 'simple']

# Main Problem: ¿Who is the merchant? ¿Juan, Omar, Antonella, Santiago or Sonia?

def init_logs():
    with open('logs.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=';')
        writer.writerow(['MÉTODO SELECCIÓN', 'MÉTODO CRUZAMIENTO', 'MÉTODO MUTACIÓN'])
        writer.writerow(in_parameters)


def log_iteration(iterations, population, best_aptitude):
    with open('logs.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=';', )
        writer.writerow([''])
        writer.writerow(['ITERACIÓN #', str(iterations)])
        writer.writerow(['MEJOR APTITUD:', str(best_aptitude)])
        writer.writerow(['Persona', 'Profesión', 'Medio de transporte', 'Horario de entrada', 'Lo que mira en TV'])
        for person in population.people:
            writer.writerow(person.description())
        writer.writerow(['REGLAS:'])
        writer.writerow(range(1,16))
        writer.writerow(population.calculate_points())

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
    "tournament": TournamentSelection(),
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
    init_logs();
    population = generate_chromosomes()
    print("Population size:", len(population))
    best_aptitude = max(map(lambda c: c.aptitude(), population))
    iterations = 0
    aptitudes = list([best_aptitude])
    while best_aptitude < 15:
        try:
            print("Best aptitude:", best_aptitude)
            population.sort(key=lambda chromosome: chromosome.aptitude(), reverse=True)
            for person in population[0].people:
                print(person.description())
            population[0].describe_points()

            # 1 - Selection
            selected = selectors[in_parameters[0]].select(population)

            # 2 - Cross Over
            new_population = cross_overs[in_parameters[1]].cross_over(selected)

            # 3 - Mutation
            population = mutations[in_parameters[2]].mutate(new_population) + selected

            best_aptitude = max(map(lambda c: c.aptitude(), population))
            aptitudes.append(best_aptitude)
            print("------------------------------- End of iteration", iterations)
            log_iteration(iterations, population[0], best_aptitude)

            iterations += 1
        except:
            plot(aptitudes)

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
