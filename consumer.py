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


load_dotenv()

API_KEY = os.getenv('API_KEY')
TOPIC_NAME = os.getenv('TOPIC_NAME')

def main() -> None:
    consumer = KafkaConsumer(consumer)
    for message in consumer:
        values = message.value
        print(f'{values}')

if __name__ == '__main__':
    main()