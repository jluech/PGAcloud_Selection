import math
import random
from abc import ABC, abstractmethod


class AbstractSelection(ABC):
    @ abstractmethod
    def perform_selection(self, population):
        # Perform the selection on the population, a list of individuals in the form of a dictionary.
        # Returns a list of Pair
        pass


class RouletteWheelSelection(AbstractSelection):
    def perform_selection(self, population):
        size = population.__len__()
        iterations = math.ceil(size / 2)
        parents = []

        fitness_sum = 0
        for individual in population:
            fitness_sum += individual.get("fitness")

        for i in range(iterations):
            pair = Pair()
            pair.p1 = self.__spin_the_wheel(population, fitness_sum)
            pair.p2 = self.__spin_the_wheel(population, fitness_sum)
            parents.append(pair)

        return parents

    def __spin_the_wheel(self, population, fitness_sum):
        partial_fitness_sum = 0
        wheel_spin = random.randint(0, fitness_sum)  # select individual at random
        selected = population[0]  # select first individual if wheel_spin=0
        for individual in population:  # retrieve selected individual
            if partial_fitness_sum >= wheel_spin:  # consider fitness boundaries can also be selected
                break
            selected = individual
            partial_fitness_sum += individual.get("fitness")
        return selected


class TournamentSelection(AbstractSelection):
    def perform_selection(self, population):
        pass


class RankSelection(AbstractSelection):
    def perform_selection(self, population):
        pass


class Pair(object):
    p1: None
    p2: None
