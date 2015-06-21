#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
        print " [x] Received %r" % (body,)
        time.sleep( body.count('.') )
        print " [x] Done"
        ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='task_queue', durable=True)
channel.exchange_declare('logs', type='fanout')

channel.basic_consume(callback, queue='task_queue')

print ' [*] Waiting for messages. To exit, press CTRL+C'
channel.start_consuming()

