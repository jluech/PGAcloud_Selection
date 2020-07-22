import math
import random
from abc import ABC, abstractmethod
from enum import Enum


class Selectors(Enum):
    RouletteWheel = "roulette",
    Tournament = "tournament",
    Rank = "rank",


class AbstractSelection(ABC):
    @ abstractmethod
    def perform_selection(self, population):
        # Perform the selection on the population, a list of Individual's.
        # Returns a list of Pair's.
        pass


class RouletteWheelSelection(AbstractSelection):
    def perform_selection(self, population):
        size = population.__len__()
        iterations = math.ceil(size / 2)
        parents = []

        fitness_sum = 0
        for individual in population:
            fitness_sum += individual.fitness

        for i in range(iterations):
            parent1 = self.__spin_the_wheel(population, fitness_sum)
            parent2 = self.__spin_the_wheel(population, fitness_sum)
            parents.append(Pair(parent1, parent2))

        return parents

    @staticmethod
    def __spin_the_wheel(population, fitness_sum):
        partial_fitness_sum = 0
        wheel_spin = random.randint(0, fitness_sum)  # select individual at random
        selected = population[0]  # select first individual if wheel_spin=0
        for individual in population:  # retrieve selected individual
            if partial_fitness_sum >= wheel_spin:  # consider fitness boundaries can also be selected
                break
            selected = individual
            partial_fitness_sum += individual.fitness
        return selected


class TournamentSelection(AbstractSelection):
    def perform_selection(self, population):
        pass


class RankSelection(AbstractSelection):
    def perform_selection(self, population):
        pass


class Pair(object):
    def __init__(self, parent1, parent2):
        self.p1 = parent1
        self.p2 = parent2
