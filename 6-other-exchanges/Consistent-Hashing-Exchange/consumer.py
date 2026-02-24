import pika
from pika.exchange_type import ExchangeType

def message_received(ch, method, properties, body):
    print(f"Q1:Receive message: {body}")  

def message_1_received(ch, method, properties, body):
    print(f"Q2:Receive message: {body}") 

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters=connection_params)

channel = connection.channel()
channel.exchange_declare('simpleHashing', 'x-consistent-hash')

channel.queue_declare(queue='letterbox1')
channel.queue_bind(queue='letterbox1', exchange='simpleHashing', routing_key="1")
channel.basic_consume(queue="letterbox1", on_message_callback=message_received, auto_ack=True) 

channel.queue_declare(queue='letterbox2')
channel.queue_bind(queue='letterbox2', exchange='simpleHashing', routing_key='4')
channel.basic_consume(queue="letterbox2", on_message_callback=message_1_received, auto_ack=True) 

print("starting consuming")

channel.start_consuming()