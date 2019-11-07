import requests
import json

url = "https://ye5y9r600c-dsn.algolia.net/1/indexes/ordered_articles_production/query"

querystring = {"x-algolia-agent":"Algolia for vanilla JavaScript 3.20.3","x-algolia-application-id":"YE5Y9R600C","x-algolia-api-key":"YWVlZGM3YWI4NDg3Mjk1MzJmMjcwNDVjMjIwN2ZmZTQ4YTkxOGE0YTkwMzhiZTQzNmM0ZGFmYTE3ZTI1ZDFhNXJlc3RyaWN0SW5kaWNlcz1zZWFyY2hhYmxlc19wcm9kdWN0aW9uJTJDVGFnX3Byb2R1Y3Rpb24lMkNvcmRlcmVkX2FydGljbGVzX3Byb2R1Y3Rpb24lMkNDbGFzc2lmaWVkTGlzdGluZ19wcm9kdWN0aW9uJTJDb3JkZXJlZF9hcnRpY2xlc19ieV9wdWJsaXNoZWRfYXRfcHJvZHVjdGlvbiUyQ29yZGVyZWRfYXJ0aWNsZXNfYnlfcG9zaXRpdmVfcmVhY3Rpb25zX2NvdW50X3Byb2R1Y3Rpb24lMkNvcmRlcmVkX2NvbW1lbnRzX3Byb2R1Y3Rpb24="}

payload = "{\"params\":\"query=*&hitsPerPage=15&page=0&attributesToHighlight=%5B%5D&tagFilters=%5B%5D\"}"
headers = {
    'accept': "application/json",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    'content-type': "application/json",
    'sec-fetch-mode': "cors",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

json_obj = json.loads(response.text)
path = json_obj['hits'][0]['user']['username']
name = json_obj['hits'][0]['user']['name']

print("path:", path)
print("name:", name)