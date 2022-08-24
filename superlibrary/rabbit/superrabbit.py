# AUTHOR: nmacatangay

import pika


# module specfic variable
hostname = "test"


def test():
    print hostname
    print "insidre superlibrary.rabbit.superrabbit"

def consume(queue_host, queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=queue_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback, queue=queue_name)
    channel.start_consuming()

def insert(queue_host, queue_name, queue_data):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=queue_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=queue_data,
        properties=pika.BasicProperties(
            delivery_mode = 2
        )
    )
    connection.close()


# class implementation for rabbit


class Queue(object):
    def __init__ (self, hostname) :
        self.hostname = hostname

    def callback(self, ch, method, properties, body):
        print "this must be implemented on the child class"
        ch.basic_ack(delivery_tag = method.delivery_tag)

    def start(self, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.hostname))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.callback, queue=self.queue_name)
        self.channel.start_consuming()

    def send(self, queue_name, data):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.hostname))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=data,
            properties=pika.BasicProperties(
                delivery_mode = 2
            )
        )
        return 1







