#!/usr/bin/env python

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs', type='direct')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)

print " [x] Sent %r " % (message,)

connection.close()

