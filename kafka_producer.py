# -*- coding: utf-8 -*-

"""

step 1 : pip3 install kafka-python or pip install kafka-python

    bootstrap_servers=[‘0.0.0.0:32820’]: sets the host and port the producer should contact to bootstrap initial
    cluster metadata. It is not necessary to set this here, since the default is localhost:9092.
     
    value_serializer=lambda x: dumps(x).encode(‘utf-8’): function of how the data should be serialized before 
    sending to the broker. Here, we convert the data to a json file and encode it to utf-8.

   """

from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'),
   bootstrap_servers=['0.0.0.0:32768'])

for i in range(1, 100):
    producer.send('t1', value={"hello": i})
    sleep(0.1)
    
