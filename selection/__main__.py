import logging

from message_handler.rabbit_message_queue import RabbitMessageQueue
from selection.selectors import RouletteWheelSelection, TournamentSelection, RankSelection
from utilities.utils import MessageHandlers, Selectors

MESSAGE_BROKER = MessageHandlers.RabbitMQ
SELECTOR = Selectors.RouletteWheel


def apply_selection(population):
    # Applies the chosen selection operator on the population and returns a list of pairs [{p1: x, p2: y}]
    logging.debug("Performing selection on population: {pop_}".format(
        pop_=population
    ))
    selector = get_selector()
    return selector.perform_selection(population)


def listen_for_selection():
    message_handler = get_message_handler()
    message_handler.receive_messages()


def get_message_handler():
    if MESSAGE_BROKER == MessageHandlers.RabbitMQ:
        return RabbitMessageQueue()
    else:
        raise Exception("No valid MessageHandler defined!")


def get_selector():
    if SELECTOR == Selectors.RouletteWheel:
        return RouletteWheelSelection()
    elif SELECTOR == Selectors.Tournament:
        selector = TournamentSelection()
        raise Exception("TournamentSelection not implemented yet!")
    elif SELECTOR == Selectors.Rank:
        selector = RankSelection()
        raise Exception("RankSelection not implemented yet!")
    else:
        raise Exception("No valid Selector defined!")


if __name__ == "__main__":
    listen_for_selection()
