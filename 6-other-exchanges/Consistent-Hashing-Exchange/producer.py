import pika

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters=connection_params)

channel = connection.channel()

channel.exchange_declare('simpleHashing', 'x-consistent-hash')

route_key = "Hash me!"
message = "Hello World: Hash me!"
channel.basic_publish(exchange='simpleHashing', routing_key=route_key, body=message)

print(f"Sent message: {message}")

connection.close()