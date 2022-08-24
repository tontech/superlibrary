# AUTHOR: nmacatangay

import json
import boto.sqs
from boto.sqs.message import RawMessage

def connect_to_amazon(region, key, secret):

    # CONNECT TO AMAZON
    amazon = boto.sqs.connect_to_region(
            region,
            aws_access_key_id=key,
            aws_secret_access_key=secret)

    return amazon

def disconnect_from_amazon(amazon):

    # DISCONNECT FROM AMAZON
    amazon.close

    return None

def connect_to_sqs_queue(name, amazon):

    # CONNECT TO AMAZON SQS QUEUE
    queue = amazon.get_queue(name)

    return queue

def fetch_from_queue(queue, message_attributes, message_count):

    is_a_list = 1

    # VALIDATION
    if type(message_attributes).__name__ == "list":
        if len(message_attributes) < 1:
            is_a_list = 0
    else:
        is_a_list = 0

    # FETCH DATA
    if is_a_list == 1:
        queue_data = queue.get_messages(message_count, message_attributes=message_attributes)
    else:
        queue_data = queue.get_messages(message_count)

    return queue_data

def delete_from_queue(queue, queue_data):

    queue.delete_message_batch(queue_data)

    return None

def insert_to_queue(queue, message_body, message_attributes):

    message = RawMessage()
    message.set_body(message_body)
    message.message_attributes = message_attributes

    queue.write(message)

    return None
