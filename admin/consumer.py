# amqps://bfcstckj:oLB6aJ4IP2iwtHaS_M2Yqeza1FdR94v_@cow.rmq2.cloudamqp.com/bfcstckj
import pika, json

params = pika.URLParameters('amqps://bfcstckj:oLB6aJ4IP2iwtHaS_M2Yqeza1FdR94v_@cow.rmq2.cloudamqp.com/bfcstckj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Recieved in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()