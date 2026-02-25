import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters=connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mainExchange', exchange_type=ExchangeType.direct)

message = "Hello World: Expired"

channel.basic_publish(exchange='mainExchange', routing_key='Test', body=message)

print(f"Sent message: {message}")

connection.close()