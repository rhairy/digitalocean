import json
import requests

_api_url_base = 'https://api.digitalocean.com/v2/'

def create(api_token, droplet_json):
    
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}

    api_url = '{0}droplets'.format(_api_url_base)

    response = requests.post(api_url, data=droplet_json, headers=headers)

    return json.loads(response.content.decode('utf-8'))

def retrieve(api_token, droplet_id):
    
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}

    api_url = '{0}droplets/{1}'.format(_api_url_base, droplet_id)

    response = requests.get(api_url, headers=headers)
    return json.loads(response.content.decode('utf-8'))

def retrieve_all(api_token):
    
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}

    api_url = '{0}droplets'.format(_api_url_base)

    response = requests.get(api_url, headers=headers)

    return json.loads(response.content.decode('utf-8'))
