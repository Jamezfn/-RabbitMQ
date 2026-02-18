import pika

def on_request_message_recieved(ch, method, properties, body):
    print(f"Request new message recieved: {properties.correlation_id}:{body}")
    ch.basic_publish(
        '', routing_key=properties.reply_to,
        body=f"Hey its your server reply to {properties.correlation_id}"
    )

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.queue_declare(queue='request-queue')

channel.basic_consume(queue='request-queue', auto_ack=True, on_message_callback=on_request_message_recieved)

print("Starting server...")

channel.start_consuming()