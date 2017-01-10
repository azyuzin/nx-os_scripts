import requests
import json

import getpass
"""
Modify these please
"""
url='http://172.23.28.x/ins'
switchuser='user_here'
#switchpassword='PASSWORD'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show clock",
      "version": 1
    },
    "id": 1
  }
]

switchpassword = getpass.getpass("enter password:") 
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print response['result']['body']['simple_time']
