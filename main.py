import pika

rabbitmq_host = { host }
rabbitmq_port = 5672
rabbitmq_user = { username }
rabbitmq_pass = { password }
rabbitmq_vhost = { vhots_name }

creds = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
connection_params = pika.ConnectionParameters(
    host=rabbitmq_host,
    port=rabbitmq_port,
    credentials=creds,
    virtual_host=rabbitmq_vhost
)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

exchange_name = 'test_exchange'
queue_name = 'test_queue'
channel.exchange_declare(
    exchange=exchange_name,
    exchange_type='direct',
    durable=True
)
channel.queue_declare(
    queue=queue_name,
    arguments={"x-message-ttl": 3600000},
    durable=True
)

channel.queue_bind(
    queue=queue_name,
    exchange=exchange_name,
    routing_key=''
)

sample_message = ["Hello World!", "This is second sample message", "This is third one", "Forth one"]

for message in sample_message:
    channel.basic_publish(
        exchange=exchange_name,
        routing_key='',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)
    )
    
    print("sample message ", message, "sent")


connection.close()