import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters=connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='FirstExchange', exchange_type=ExchangeType.direct)

channel.exchange_declare(exchange='SecondExchange', exchange_type=ExchangeType.fanout)

channel.exchange_bind("SecondExchange", "FirstExchange")

message = "Hello World: Passed through multiple exchange"
channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"Sent message: {message}")

connection.close()