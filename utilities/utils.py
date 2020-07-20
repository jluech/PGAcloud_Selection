from enum import Enum


class MessageHandlers(Enum):
    RabbitMQ = "rabbitMQ",


class Selectors(Enum):
    RouletteWheel = "roulette",
    Tournament = "tournament",
    Rank = "rank",
