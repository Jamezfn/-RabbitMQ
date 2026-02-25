import pika
from pika.exchange_type import ExchangeType

def alt_message_received(ch, method, properties, body):
    print(f"ALT:Receive message: {body}")  

def main_message_received(ch, method, properties, body):
    print(f"main:Receive message: {body}") 

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='altExchange', exchange_type=ExchangeType.fanout)
channel.exchange_declare(
    exchange='mainExchange', 
    exchange_type=ExchangeType.direct,
    arguments={'alternate-exchange': 'altExchange'}
)


channel.queue_declare(queue='altExchangeQueue')
channel.queue_bind(queue='altExchangeQueue', exchange='altExchange')

channel.queue_declare(queue='mainExchangeQueue')
channel.queue_bind(queue='mainExchangeQueue', exchange='mainExchange', routing_key='Test')

channel.basic_consume(queue='altExchangeQueue', auto_ack=True, on_message_callback=alt_message_received)
channel.basic_consume(queue='mainExchangeQueue', auto_ack=True, on_message_callback=main_message_received)

print('Starting to consume')
channel.start_consuming()