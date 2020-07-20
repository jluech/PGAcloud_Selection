from abc import ABC, abstractmethod


class MessageHandler(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def receive_message(self, action_on_receive):
        pass

    @abstractmethod
    def send_message(self):
        pass
