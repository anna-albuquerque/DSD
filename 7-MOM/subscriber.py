import pika

def callback(ch, method, properties, body):
    print(f'Mensagem recebida: {body}')

def consumir_mensagens():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='mensagem.*')

    print('Aguardando mensagens. Para sair, pressione CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    consumir_mensagens()