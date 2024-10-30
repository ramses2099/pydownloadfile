import os
import requests
from datetime import datetime
from newsapi import NewsApiClient

API_KEY = '176dfe240742406d8873cf3c88e95d27'
PAGE_SIZE = 100

def main() -> None:
    os.system("cls")
    print("Starting")
        
    # Init
    newsapi = NewsApiClient(api_key=API_KEY)   

    sources = newsapi.get_everything(q="Big Data")
    
    # status code
    print(f"Status: {sources["status"]}")   
    print(f"Total rows: {sources["totalResults"]}")
    totalRows = sources["totalResults"]
    pages = round(totalRows / PAGE_SIZE)
    print(f"Total pages: {pages}") 
    
    if sources["status"] == "ok":
        for i in range(1, pages):
            sources = newsapi.get_everything(q="Big Data", page=i)
            if sources["status"] == "ok":
                data = sources["articles"]
                
                with open("news.csv",'w', encoding="utf-8") as f:
                    columns ="source,publishedAt,author,title,description,content\n"            
                    f.write(columns)
                    if data:
                        for row in data:
                            source = row["source"]["name"]
                            publishedAt = datetime.strptime(row["publishedAt"], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
                            line = f"{source},{publishedAt},{row['author']},{row['title']},{row['description']},{row['content']}\n"
                            f.write(line)
           
    
    print("Finished")
    
if __name__ == "__main__":
    main()