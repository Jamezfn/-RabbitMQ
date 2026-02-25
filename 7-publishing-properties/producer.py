import pika

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()
channel.confirm_delivery()
channel.tx_select()

channel.queue_declare(queue='Test', durable=True)

message = "Hello World"

channel.basic_publish(
    exchange='pubsub', 
    routing_key='', 
    body=message,
    properties=pika.BasicProperties(
        headers={'name': 'James'},
        delivery_mode=1,
        expiration=123456,
        content_type="application/json"
    ),
    mandatory=True
)

channel.tx_commit()

channel.tx_rollback()

print(f"Sent message: {message}")

connection.close()