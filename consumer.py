import os
import sys
import six
import json

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
    consumer = KafkaConsumer(topic, 
                                auto_offset_reset='earliest',
                                enable_auto_commit=False,
                                value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    try:
        print("Start Consuming for messages...")
        
        with open("news.csv",'w', encoding="utf-8") as f:
            columns ="source,publishedAt,author,title,description,content\n"            
            f.write(columns)
            # Continuously poll for new messages
            for message in consumer:
                data = message.value            
                line = f"{data['source']},{data['publishedAt']},{data['author']},{data['title']},{data['description']},{data['content']}\n"
                f.write(line)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close(autocommit=False)
        print("Finished Consuming for messages...")


if __name__ == '__main__':
    main()