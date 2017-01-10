#source: http://inbound.kelsercorp.com/blog/cisco-nexus-9000-automation-part-2
#Print Switch Details
import json
import requests
import getpass


my_headers = {'content-type': 'application/json-rpc'}
url='https://172.23.28.x/ins'
username = "user-here"

requests.packages.urllib3.disable_warnings()

password = getpass.getpass("enter password:")

#basics
payload=[{"jsonrpc": "2.0",
          "method": "cli",
          "params": {"cmd": "sh ver",
                     "version": 1},
          "id": 1}
         ]

response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password), verify=False).json()

print "\nHostname: " + response['result']['body']['host_name']
print "System Type: " + response['result']['body']['chassis_id']
print "Version: " + response['result']['body']['rr_sys_ver']




#ip stuff


payload=[{"jsonrpc": "2.0",
          "method": "cli",
          "params": {"cmd": "sh ip int br",
                     "version": 1},
          "id": 1}
         ]



response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password), verify=False).json()
TABLE_intf=response['result']['body']['TABLE_intf']
for interface in TABLE_intf:
  print "\nInterface Name: " + interface['ROW_intf']['intf-name'] + " : " + interface['ROW_intf']['prefix']





#environmentals



payload=[{"jsonrpc": "2.0",
          "method": "cli",
          "params": {"cmd": "sh environment",
                     "version": 1},
          "id": 1}
         ]

response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password), verify=False).json()


powersupply = response['result']['body']['powersup']['TABLE_psinfo']['ROW_psinfo']
print "\nNumber of Power Supplies:" + str(len(powersupply))
for i in powersupply:
    print "PS: " + str(i['psnum']) + " " + i['ps_status']
    
temperature = response['result']['body']['TABLE_tempinfo']['ROW_tempinfo']
print  "Current Intake Temperature: " + temperature[0]['curtemp']


#ospf stuff

#payload=[{"jsonrpc": "2.0",
#          "method": "cli",
#          "params": {"cmd": "sh ip BGP sum",
#                     "version": 1},
#          "id": 1}
#         ]

#response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password), verify=False).json()

#neighbors = response['result']['body']['TABLE_ctx']['ROW_ctx']['nbrcount']

#print "\nNumber of OSPF neighbors: " + str(neighbors)
#print "Neighbors:"
#print "RID             IP             Interface"
#for i in range(0,neighbors):
#    row = response['result']['body']['TABLE_ctx']['ROW_ctx']['TABLE_nbr']['ROW_nbr'][i]
 #   print row['rid'] + "           " + row['addr'] + "            " + row['intf']




#route stuff

payload=[{"jsonrpc": "2.0",
          "method": "cli",
          "params": {"cmd": "sh ip route vrf all",
                     "version": 1},
          "id": 1}
         ]

response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password), verify=False).json()

print "\nNumber of VRFs: " + str(len(response['result']['body']['TABLE_vrf']['ROW_vrf']))
for vrf in response['result']['body']['TABLE_vrf']['ROW_vrf']:
    print "VRF name: " + vrf['vrf-name-out']
    print "Number of Routes: " + str(len(vrf['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix']))


