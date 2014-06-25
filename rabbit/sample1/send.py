#!/usr/bin/env python
import pika, sys

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials = credentials)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.exchange_declare(exchange="hello-exchange",
                         type="direct",
                         passive=False,
                         durable=True,
                         auto_delete=False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

channel.basic_publish(body = msg,
                      exchange = "hello-exchange",
                      properties = msg_props,
                      routing_key = "hello")

print msg + " is sent"
