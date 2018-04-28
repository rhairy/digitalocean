import droplets
import getpass
import json
import requests

token = getpass.getpass("Please paste your API token here: ")

new_json_data = {
    "name": "test.rhairy.com", 
    "region": "sfo2", 
    "size": "s-1vcpu-1gb", 
    "image": "ubuntu-16-04-x64", 
    "backups": False, 
    "ipv6": True, 
    "ssh": [],
    "user_data": "null", 
    "private_networking": False, 
    "monitoring": False, 
    "volumes": [], 
    "tags": [] 
}

serial = json.dumps(new_json_data)
print(droplets.create(token, serial))
