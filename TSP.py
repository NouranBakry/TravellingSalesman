import random
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# This is just a dictionary containing 10 cities and their distances from each other.

Cities = ["Istanbul", "Sicily", "London", "Madrid", "Venice", "Vienna", "Ontario",
          "Brighton", "Berlin", "Tokyo"]
Distances = {Cities[0]: [(Cities[0], 0), (Cities[1], 1838), (Cities[2], 3048), (Cities[3], 3537),
                         (Cities[4], 1718), (Cities[5], 1564), (Cities[6], 7945), (Cities[7], 3087),
                         (Cities[8], 2194), (Cities[9], 8939)],
             Cities[1]: [(Cities[0], 1838), (Cities[1], 0), (Cities[2], 1709), (Cities[3], 2845),
                         (Cities[4], 1409), (Cities[5], 2005), (Cities[6], 7413), (Cities[7], 2794),
                         (Cities[8], 2385), (Cities[9], 10124)],
             Cities[2]: [(Cities[0], 3048), (Cities[1], 1709), (Cities[2], 0), (Cities[3], 1070),
                         (Cities[4], 986), (Cities[5], 916), (Cities[6], 3451), (Cities[7], 67),
                         (Cities[8], 680), (Cities[9], 5936)],
             Cities[3]: [(Cities[0], 3537), (Cities[1], 2845), (Cities[2], 1070), (Cities[3], 0),
                         (Cities[4], 1829), (Cities[5], 2396), (Cities[6], 6100), (Cities[7], 1758),
                         (Cities[8], 2314), (Cities[9], 10755)],
             Cities[4]: [(Cities[0], 1718), (Cities[1], 1409), (Cities[2], 1070), (Cities[3], 1829),
                         (Cities[4], 0), (Cities[5], 609), (Cities[6], 6687), (Cities[7], 1600),
                         (Cities[8], 1130), (Cities[9], 9557)],
             Cities[5]: [(Cities[0], 1564), (Cities[1], 2005), (Cities[2], 986), (Cities[3], 2396),
                         (Cities[4], 609), (Cities[5], 0), (Cities[6], 6690), (Cities[7], 1517),
                         (Cities[8], 681), (Cities[9], 9122)],
             Cities[6]: [(Cities[0], 7945), (Cities[1], 7413), (Cities[2], 3451), (Cities[3], 6100),
                         (Cities[4], 6687), (Cities[5], 6690), (Cities[6], 0), (Cities[7], 5598),
                         (Cities[8], 6208), (Cities[9], 9391)],
             Cities[7]: [(Cities[0], 3087), (Cities[1], 2794), (Cities[2], 67), (Cities[3], 1758),
                         (Cities[4], 1600), (Cities[5], 1517), (Cities[6], 5598), (Cities[7], 0),
                         (Cities[8], 706), (Cities[9], 5976)],
             Cities[8]: [(Cities[0], 2194), (Cities[1], 2385), (Cities[2], 680), (Cities[3], 2314),
                         (Cities[4], 1130), (Cities[5], 681), (Cities[6], 6208), (Cities[7], 706),
                         (Cities[8], 0), (Cities[9], 8911)],
             Cities[9]: [(Cities[0], 8939), (Cities[1], 10124), (Cities[2], 5936), (Cities[3], 10755),
                         (Cities[4], 9557), (Cities[5], 9122), (Cities[6], 9391), (Cities[7], 5976),
                         (Cities[8], 8911), (Cities[9], 0)]}


def fitness():
    for city in Distances:
        Distances[city].sort(key=lambda tup: tup[1])
    stack = deque()
    for c in Cities:
        distance = 0
        visited = []
        path = list()
        stack.append(Distances[c])
        first = Distances[c][0]
        path.append(first)
        while stack:
            current = stack.pop()
            temp = current[0]
            current_city = temp[0]
            visited.append(current_city)
            for city in current:
                if city[0] != current_city and city[0] not in visited:
                    path.append(city)
                    stack.append(Distances[city[0]])
                    break
        journey.append(path)
        for p in path:
            distance += p[1]
        fittest.append(distance)
    print(fittest)
    print(journey)


def breed(first_parent, second_parent):
    child = []
    child_a = []
    child_b = []
    taken = []
    #  choose a random subset
    gene_a = random.randint(0, len(first_parent)-1)
    gene_b = random.randint(0, len(first_parent)-1)
    start = min(gene_a, gene_b)
    end = max(gene_a, gene_b)
    for i in range(start, end):
        if i == start:
            child_a.append(Distances[first_parent[i][0]][0])
        else:
            for item in Distances[first_parent[i - 1][0]]:
                if item[0] == first_parent[i][0]:
                    child_a.append(item)
    if len(child_a) != 0:
        length = len(child_a)
        # print(length)
        previous = child_a[length-1][0]
    else:
        previous = second_parent[0][0]
    for i in range(len(child_a)):
        taken.append(child_a[i][0])
    for item in second_parent:
        if item[0] not in taken:
            for city in Distances[previous]:
                if city[0] == item[0]:
                    child_b.append(city)
                    previous = city[0]
    for item in child_a:
        child.append(item)
    for item in child_b:
        child.append(item)
    # print("Child:")
    # print(child)
    return child


def mutate(chromosome):
    index = random.randint(0, len(chromosome)-1)
    index2 = random.randint(0, len(chromosome)-1)
    # print(index)
    # print(index2)
    first = chromosome[index][0]
    second = chromosome[index2][0]
    # print(first)
    # print(second)

    if index == 0:
        chromosome[index] = Distances[second][0]
    else:
        previous = chromosome[index - 1][0]
        # print("previous: ", previous)
        for item in Distances[previous]:
            if item[0] == second:
                # print(item)
                chromosome[index] = item
            if index != len(chromosome) - 1:
                next_city = chromosome[index + 1][0]
                # print("next city: ", next_city)
                for t in Distances[second]:
                    if t[0] == next_city:
                        chromosome[index + 1] = t
    if index2 == 0:
        chromosome[index2] = Distances[first][0]
    else:
        previous = chromosome[index2 - 1][0]
        for item in Distances[previous]:
            if item[0] == first:
                chromosome[index2] = item
        if index2 < 9:
            next_city = chromosome[index2 + 1][0]
            for item in Distances[first]:
                if item[0] == next_city:
                    chromosome[index2 + 1] = item

    print("After mutation:")
    print(chromosome)
    return chromosome


def selection():
    scores = list()
    first_parent = list()
    second_parent = list()
    wheel = list()
    total = 0
    for f in fittest:
        total += f

    #  Roulette-wheel Selection
    for i in range(len(fittest)):
        fitness_score = fittest[i] / total
        probability = (fittest[i] / total) * 100
        scores.append(round(fitness_score, 2))
        print("path: ", journey[i])
        print("probability of choosing this path: %.3f" % probability, "%")
    print("Fitness Scores: ", scores)

    # Selection process
    wheel.append(0)
    for i in range(len(scores)):
        v = wheel[i] + scores[i]
        wheel.append(round(v, 1))
    print("Wheel: ", wheel)
    random_number = random.random()
    for i in range(len(wheel)):
        if wheel[i] <= random_number <= wheel[i+1]:
            first_parent = journey[i-1]
    random_number = random.random()
    for i in range(len(wheel)):
        if wheel[i] <= random_number <= wheel[i+1]:
            second_parent = journey[i-1]
    print("First Parent")
    print(first_parent)
    print("Second Parent")
    print(second_parent)
    return first_parent, second_parent


journey = list()
fittest = list()
fitness()
# x = np.arange(0, 10, 1)
# plt.xlabel('paths')
# plt.ylabel('Distances')
# plt.plot(x, fittest)
# plt.grid
# plt.show()
# parent1, parent2 = selection()
# two offsprings from parents
# first_offspring = breed(parent1, parent2)
# second_offspring = breed(parent1, parent2)
# mutate(first_offspring)
# mutate(second_offspring)
total_population = list()
# parent1, parent2 = selection()
# parent3, parent4 = selection()
first_generation = list()
new_scores = list()
# creating a pool of population by crossing over the first chosen four parents
# and mutating their offsprings then making the new parents
for i in range(20):
    print(i)
    # mutation of first generation child
    distance = 0
    # parent1, parent2 = selection()
    parent1, parent2 = selection()
    parent3, parent4 = selection()
    first_offspring = breed(parent1, parent2)
    second_offspring = breed(parent2, parent1)
    third_offspring = breed(parent3, parent4)
    fourth_offspring = breed(parent4, parent3)
    chromosome1 = mutate(first_offspring)
    chromosome2 = mutate(second_offspring)
    chromosome3 = mutate(third_offspring)
    chromosome4 = mutate(first_offspring)
    for c in chromosome1:
        distance += c[1]
    print(distance)
    first_generation.append(distance)
    total_population.append(chromosome1)
    distance = 0
    for c in chromosome2:
        distance += c[1]
    print(distance)
    first_generation.append(distance)
    total_population.append(chromosome2)
    distance = 0
    for c in chromosome3:
        distance += c[1]
    print(distance)
    first_generation.append(distance)
    total_population.append(chromosome3)
    distance = 0
    for c in chromosome4:
        distance += c[1]
    print(distance)
    first_generation.append(distance)
    total_population.append(chromosome4)
    journey.append(chromosome1)
    journey.append(chromosome2)
    journey.append(chromosome3)
    journey.append(chromosome4)
    # parent1 = chromosome1
    # parent2 = chromosome2
    # parent3 = chromosome3
    # parent4 = chromosome4
print(total_population)
total = 0
for i in first_generation:
    total += i
for i in first_generation:
    fitness_score = i / total
    new_scores.append(round(fitness_score, 2))
print(new_scores)

for i in range(len(new_scores)):
    print("Path: ", total_population[i])
    print("probability of choosing this path: ")
    probability = new_scores[i] * 100
    print(probability, "%")

generations = np.arange(0, 80, 1)
plt.xlabel('generations')
plt.ylabel('Distances')
plt.plot(generations, first_generation)
plt.grid()
plt.show()

