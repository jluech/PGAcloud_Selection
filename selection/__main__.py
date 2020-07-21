from message_handler.rabbit_message_queue import RabbitMessageQueue
from utilities.utils import MessageHandlers, Selectors, __set_selector

MESSAGE_HANDLER = MessageHandlers.RabbitMQ
SELECTOR = Selectors.RouletteWheel


def listen_for_selection():
    message_handler = get_message_handler()
    message_handler.receive_messages()


def get_message_handler():
    if MESSAGE_HANDLER == MessageHandlers.RabbitMQ:
        return RabbitMessageQueue()
    else:
        raise Exception("No valid MessageHandler defined!")


if __name__ == "__main__":
    __set_selector(SELECTOR)
    listen_for_selection()
