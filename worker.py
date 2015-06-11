#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
        print " [x] Received %r" % (body,)
        time.sleep( body.count('.') )
        print " [x] Done"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_consume(callback, queue='hello', no_ack=True)

print ' [*] Waiting for messages. To exit, press CTRL+C'
channel.start_consuming()

