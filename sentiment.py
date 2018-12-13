import requests
import json

# defining the api-endpoint  
API_ENDPOINT = "https://eastus2.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
  
# your API key here 
API_KEY = "89d6afcc5e9b477182a4e1700b4f0f54"
  
# your source code here 
data = '''{
    "documents": 
    [{
	    "language": "en",
	    "id": "1",
	    "text": "This product sucks!"
    }]
}'''

headers = { 'Ocp-Apim-Subscription-Key': API_KEY, 'Content-Type':'application/json','Accept':'application/json'}
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data, headers = headers) 
# extracting response text  
pastebin_url = r.text 
print json.loads(pastebin_url)["documents"][0]["score"]