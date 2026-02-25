import pika
from pika.exchange_type import ExchangeType

def dlx_message_received(ch, method, properties, body):
    print(f"DLX:Receive message: {body}")  

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mainExchange', exchange_type=ExchangeType.direct)
channel.exchange_declare(
    exchange='deadExchange', 
    exchange_type=ExchangeType.fanout
)


channel.queue_declare(
    queue='mainExchangeQueue',
    arguments={'x-dead-letter-exchange': 'deadExchange', 'x-message-ttl': 5000}
)
channel.queue_bind(queue='mainExchangeQueue', exchange='mainExchange', routing_key='Test')


channel.queue_declare(queue='dlxExchangeQueue')
channel.queue_bind(queue='dlxExchangeQueue', exchange='deadExchange')


channel.basic_consume(queue='dlxExchangeQueue', auto_ack=True, on_message_callback=dlx_message_received)

print('Starting to consume')
channel.start_consuming()