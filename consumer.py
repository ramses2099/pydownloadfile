import os
import sys
import six

from kafka import KafkaConsumer
from dotenv import load_dotenv

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves


################################################################
# producer data from newsapi
# by jose encarnacion
# 8982860
# Big Data integration and storage 
################################################################


topic="topicnews"
brokers = "localhost:9092"

def main() -> None:
    consumer = KafkaConsumer(topic)
    print("Starting consumer...")
    if consumer:
        print("Consumer is running...")
        for message in consumer:            
            print(f'{message}')

if __name__ == '__main__':
    main()