import logging

from message_handler.rabbit_message_queue import RabbitMessageQueue
from utilities.utils import MessageHandlers, Selectors, __set_selector, get_pga_id

logging.basicConfig(level=logging.DEBUG)  # TODO: remove and reduce to INFO

MESSAGE_HANDLER = MessageHandlers.RabbitMQ
SELECTOR = Selectors.RouletteWheel


def listen_for_selection():
    pga_id = get_pga_id()

    message_handler = get_message_handler(pga_id)
    message_handler.receive_messages()


def get_message_handler(pga_id):
    if MESSAGE_HANDLER == MessageHandlers.RabbitMQ:
        return RabbitMessageQueue(pga_id)
    else:
        raise Exception("No valid MessageHandler defined!")


if __name__ == "__main__":
    __set_selector(SELECTOR)
    listen_for_selection()
