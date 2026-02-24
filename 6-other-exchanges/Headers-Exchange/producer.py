import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters=connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='HeadersExchange', exchange_type=ExchangeType.headers)

message = "Hello World: Sent with headers"
channel.basic_publish(
    exchange='HeadersExchange', 
    routing_key='letterbox', 
    body=message,
    properties=pika.BasicProperties(headers={"name": "James"})
)

print(f"Sent message: {message}")

connection.close()