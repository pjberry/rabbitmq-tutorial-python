#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
        print " [x] Received %r" % (body,)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

print ' [*] Waiting for messages. To exit, press CTRL+C'

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()

