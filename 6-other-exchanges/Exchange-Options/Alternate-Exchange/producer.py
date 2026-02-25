import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters=connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='altExchange', exchange_type=ExchangeType.fanout)
channel.exchange_declare(
    exchange='mainExchange', 
    exchange_type=ExchangeType.direct,
    arguments={'alternate-exchange': 'altExchange'}
)

message = "Hello World"

channel.basic_publish(exchange='mainExchange', routing_key='Test', body=message)

print(f"Sent message: {message}")

connection.close()