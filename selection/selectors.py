from abc import ABC, abstractmethod


class AbstractSelection(ABC):
    @ abstractmethod
    def perform_selection(self, population):
        # Perform the selection on the population, a list of individuals in the form of a dictionary.
        # Returns a list of Pair
        pass


class RouletteWheelSelection(AbstractSelection):
    def perform_selection(self, population):
        pass


class TournamentSelection(AbstractSelection):
    def perform_selection(self, population):
        pass


class RankSelection(AbstractSelection):
    def perform_selection(self, population):
        pass


class Pair(object):
    p1: None
    p2: None
