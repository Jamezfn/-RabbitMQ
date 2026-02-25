import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters=connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='acceptRejectExchange', exchange_type=ExchangeType.fanout)

message = "Hello World"

while True:
    channel.basic_publish(exchange='acceptRejectExchange', routing_key='Test', body=message)

    print(f"Sent message: {message}")
    input('Press any key to continue')