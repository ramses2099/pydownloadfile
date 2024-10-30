import os
import requests
from datetime import datetime

URL_BASE = 'https://newsapi.org/v2/everything'
PAGE_SIZE = 100
Q='Big Data'
headers = {'Content-Type':'application/json', 'X-Api-Key':'176dfe240742406d8873cf3c88e95d27'}

def call_api(page):
    params = {
        "q": Q,
        "page": page,
    }
    
    url = f"{URL_BASE}" 
            
    response = requests.get(url,headers=headers,params=params)

    # Verify status code
    print(f"Status: {response.status_code}") 
    
    if response.status_code == 200:
        data = response.json()
        assert data["status"] == "ok"
        
        if data["status"] == "ok":
            assert data["articles"] is not None
            articles = data["articles"]
                
            with open("news.csv",'a', encoding="utf-8") as f:
                columns ="source,publishedAt,author,title,description\n"            
                f.write(columns)
                if articles:
                    for row in articles:
                        source = row["source"]["name"]
                        publishedAt = datetime.strptime(row["publishedAt"], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
                        line = f"{source},{publishedAt},{row['author']},{row['title']},{row['description']}\n"
                        f.write(line)


def main() -> None:
    os.system("cls")
    print("Starting")
    
    params = {
        "q": Q,
        "page": 1
    }
    
    url = f"{URL_BASE}" 
            
    response = requests.get(url,headers=headers,params=params)

    # Verify status code
    print(f"Status: {response.status_code}") 
    
    start_time= datetime.now()
    
    if response.status_code == 200:
        data = response.json()
        assert data["status"] == "ok"
        assert data["totalResults"] is not None        
        total_pages = 6 #data["totalResults"] // PAGE_SIZE
        print(f"Total pages {total_pages}")
        page = 1
        
        while (total_pages >= page):
            call_api(page)
            page += 1
            end_time = datetime.now()
            print(f"Duration: {end_time - start_time}")
            print(f"Downloaded page: {page}")
            start_time = end_time   
       
       
    print("Finished")
    
if __name__ == "__main__":
    main()