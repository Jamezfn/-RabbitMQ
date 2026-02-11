#!/usr/bin/env python

import pika
import time
import random

def message_recieved(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"recieved new message: {body}, will take {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing the message")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='letterbox')

# channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letterbox', on_message_callback=message_recieved)

print("starting consuming")

channel.start_consuming()
