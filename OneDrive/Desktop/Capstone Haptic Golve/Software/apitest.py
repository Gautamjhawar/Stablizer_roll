import requests
import json
import time
url = "http://192.168.0.104:5000/api/getuserobject"

payload = json.dumps({
  "finger1": "450",
  "finger2": "832",
  "finger3": "680",
  "finger4": "1024",
  "finger5": "200",
  "tempMax": "45",
  "tempMin": "30",
  "tempAvg": "32",
  "EventTrigger": "0"
})
headers = {
  'Content-Type': 'application/json'
}
while 1:
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(0.005)
