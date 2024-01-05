import pika

def publicar_mensagem(mensagem):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    channel.basic_publish(exchange='topic_logs', routing_key='mensagem.importante', body=mensagem)

    print(f'Mensagem publicada: {mensagem}')

    connection.close()

if __name__ == '__main__':
    mensagem = 'Esta é uma mensagem importante!'
    publicar_mensagem(mensagem)