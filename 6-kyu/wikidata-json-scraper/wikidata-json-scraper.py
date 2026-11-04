import requests 
​
# It is stronglly recommended to use these header along with your request:
headers = {
    "Accept-Encoding": "gzip,deflat",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
​
def wikidata_scraper(url):
    id = url.split('/')[-1]
    
    data = requests.get(url, headers=headers)
    data.raise_for_status()
    response = data.json()
    print(response)
    item = next(iter(response['entities'].values()))
    return {
        "ID": item.get('id',{}),
        "LABEL": item.get('labels', {}).get('en', {}).get('value', 'No Label'), 
        "DESCRIPTION": item.get('descriptions', {}).get('en', {}).get('value', 'No Description'),
    }
    
    