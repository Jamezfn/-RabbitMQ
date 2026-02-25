import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    if method.delivery_tag % 5 == 0:
        # ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True, multiple=True)
    print(f"Receive message: {body}")  

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='acceptRejectExchange', exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='acceptRejectQueue')
channel.queue_bind(queue='acceptRejectQueue', exchange='acceptRejectExchange', routing_key='Test')

channel.basic_consume(queue='acceptRejectQueue', on_message_callback=on_message_received)

print('Starting to consume')
channel.start_consuming()