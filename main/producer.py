# amqps://bfcstckj:oLB6aJ4IP2iwtHaS_M2Yqeza1FdR94v_@cow.rmq2.cloudamqp.com/bfcstckj
import pika, json

params = pika.URLParameters('amqps://bfcstckj:oLB6aJ4IP2iwtHaS_M2Yqeza1FdR94v_@cow.rmq2.cloudamqp.com/bfcstckj')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)