import os
import requests
from datetime import datetime

URL_BASE = 'https://data.cityofnewyork.us'
headers = {'Content-Type':'application/json', 'X-Api-Key':'ca0q7ekoz5f80vnh18wab5wfwn4lexpsynv7ydtybnhq88vl4'}
#total rows 37, 814, 029

def main() -> None:
    os.system("cls")
    print("Starting")
    
    start_time= datetime.now()
    rows = 10000000
    row = 0
    
    # $limit 	The number of results to return 	1000 	2.0 endpoints: maximum of 50,000; 2.1: unlimited 
    # $offset 	The index of the result array where to start the returned list of results. 	0 	N/A
    while (rows >=  row):
        
        data = {"limit":50000, "offset": row}
        
        url = f"{URL_BASE}/resource/erm2-nwe9.csv" 
            
        response = requests.get(url,headers=headers,data=data)

        # Verify status code
        print(f"status: {response.status_code}") 

        with open("data.csv",'ab') as f:
            for chunk in response.iter_content(chunk_size=1048576):
                if chunk:
                    f.write(chunk)
                    
        row += 50000
        if row > 0:
            end_time = datetime.now()
            print(f"Duration: {end_time - start_time}")
            print(f"Downloaded: {row}/{rows} rows")
            start_time = end_time
            
        
    print("Finished")
    
if __name__ == "__main__":
    main()