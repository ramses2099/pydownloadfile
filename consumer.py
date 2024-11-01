import os
import sys
import six

from kafka.consumer import KafkaConsumer

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves


################################################################
# producer data from newsapi
# by jose encarnacion
# 8982860
# Big Data integration and storage 
################################################################

# Kafka consumer configuration
topic = "topicnews"
brokers = "localhost:9092"

def main() -> None:
    # Create the Kafka consumer
    consumer = KafkaConsumer(topic, bootstrap_servers=brokers,group_id='console-consumer-group',
                             auto_offset_reset='latest', enable_auto_commit=False)

    # Continuously poll for new messages
    for message in consumer:
        print(message.value.decode())


if __name__ == '__main__':
    main()