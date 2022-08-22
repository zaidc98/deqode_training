import base64
import json
import requests
 
def test_pubsub(event,context):
   print("========= ",event)
  
   mess = base64.b64decode(event['data']).decode('utf-8')
   api_req = requests.get("https://raw.githubusercontent.com/amylio/Movies-ETL/main/MOD8_Challenge_Submission/Resources/wikipedia-movies.json")
   resp_text = api_req.text
   parse_json = json.loads(resp_text)
 
   print(f" ============ printing the publish message : {mess} =====")
   print(f"======== {len(parse_json)} records have been fetched from the API ==========")
   print("========First two records are as follow==========")
   print(parse_json[:2])

