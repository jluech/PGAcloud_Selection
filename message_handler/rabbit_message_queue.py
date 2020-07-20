import logging

import pika

from message_handler.message_handler import MessageHandler
from selection.__main__ import apply_selection

QUEUE_NAME = "selection"


def __selection_request_callback(ch, method, properties, body):
    logging.debug("{queue_}: Received selection request for population: {pop_}".format(
        queue_=QUEUE_NAME,
        pop_=body,
    ))
    apply_selection(body)


class RabbitMessageQueue(MessageHandler):
    def __init__(self):
        # Establish connection to rabbitMQ.
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="rabbitMQ",
            credentials=pika.PlainCredentials("rabbit", "MQ")
        ))
        self.channel = self.connection.channel()

    def receive_message(self, action_on_receive):
        # Create queue for selection.
        self.channel.queue_declare(queue=QUEUE_NAME, durable=True)

        # Listen to selection queue.
        self.__listen_to_queue(action_on_receive)

        # Close connection when finished. TODO: check if prematurely closing connection
        self.connection.close()

    def send_message(self):
        pass

    def __listen_to_queue(self, callback):
        # Actively listen for messages in queue and perform callback on receive.
        self.channel.basic_consume(
            queue=QUEUE_NAME,
            on_message_callback=callback,
            auto_ack=True
        )
        logging.debug("Waiting for selection requests.")
        self.channel.start_consuming()
