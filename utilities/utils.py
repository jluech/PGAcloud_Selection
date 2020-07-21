from enum import Enum

__SELECTOR = None


class MessageHandlers(Enum):
    RabbitMQ = "rabbitMQ",


class Selectors(Enum):
    RouletteWheel = "roulette",
    Tournament = "tournament",
    Rank = "rank",


def forward_selector():
    return __SELECTOR


def __set_selector(selector):
    global __SELECTOR
    __SELECTOR = selector
