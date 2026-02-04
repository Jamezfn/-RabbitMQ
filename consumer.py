#!/usr/bin/env python

import pika

def message_recieved(ch, method, properties, body):
    print(f"recieved new message: {body}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, 
                      on_message_callback=message_recieved)

print("starting consuming")

channel.start_consuming()
