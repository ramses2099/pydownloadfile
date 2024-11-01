import os
import sys
import six
import json
from datetime import datetime
from kafka import KafkaProducer
from dotenv import load_dotenv
from newsapi import NewsApiClient

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
Q='Big Data'

def main() -> None:
    
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    newsapi = NewsApiClient(api_key=API_KEY)
    
    # Define the list of media sources
    sources = 'bbc-news,cnn,fox-news,nbc-news,the-guardian-uk,the-new-york-times,the-washington-post,usa-today,independent,daily-mail'

    # /v2/everything
    response = newsapi.get_everything(q=Q,
                                        sources=sources,
                                        language='en')
    
    # Check if the request was successful
    if response['status'] == 'ok':
        data = response['articles']
        # Print the titles of the articles
        if data:
            for row in data:
                print(row['title'])
                source = row["source"]["name"]
                publishedAt = datetime.strptime(row["publishedAt"], '%Y-%m-%dT%H:%M:%SZ')
                article = {
                    'source': source,
                    'publishedAt': publishedAt.strftime('%Y-%m-%d'),
                    'author': row['author'],
                    'title': row['title'],
                    'description': row['description'].replace('\n', ' ').replace('\r', ''),
                    'content': row['content'].replace('\n', ' ').replace('\r', '')  
                }
                
                # Send the article to Kafka                    
                producer.send(TOPIC_NAME, json.dumps(article).encode('utf-8'))
                producer.flush()                
        
    else:
        print(f'Error: {response["message"]}')
        return

if __name__ == '__main__':
    main()