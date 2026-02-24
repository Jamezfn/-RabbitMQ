import pika
from pika.exchange_type import ExchangeType

def message_recieved(ch, method, properties, body):
    print(f"Receive message: {body}")  

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters=connection_params)

channel = connection.channel()
channel.exchange_declare(exchange='SecondExchange', exchange_type=ExchangeType.fanout)
channel.queue_declare(queue='letterbox')

channel.queue_bind(queue='letterbox', exchange='SecondExchange')

channel.basic_consume(queue="letterbox", on_message_callback=message_recieved, auto_ack=True) 

print("starting consuming")

channel.start_consuming()