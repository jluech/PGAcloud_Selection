import logging

from selection.selectors import RouletteWheelSelection, TournamentSelection, RankSelection
from utilities.utils import Selectors, forward_selector


def apply_selection(population):
    # Applies the chosen selection operator on the population and returns a list of pairs [{p1: x, p2: y}]
    logging.debug("Performing selection on population: {pop_}".format(
        pop_=population
    ))
    selector = get_selector()
    return selector.perform_selection(population)


def get_selector():
    selector = forward_selector()
    if selector == Selectors.RouletteWheel:
        return RouletteWheelSelection()
    elif selector == Selectors.Tournament:
        __selector = TournamentSelection()
        raise Exception("TournamentSelection not implemented yet!")
    elif selector == Selectors.Rank:
        __selector = RankSelection()
        raise Exception("RankSelection not implemented yet!")
    else:
        raise Exception("No valid Selector defined!")
