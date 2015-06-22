#!/usr/bin/env python

import pika
import sys

def callback(ch, method, properties, body):
        print " [x] Received %r" % (body,)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    print >> sys.stderr, "Usage: %s [info], [warning], [error]" % (sys.argv[0],)
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

print ' [*] Waiting for messages. To exit, press CTRL+C'

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()

