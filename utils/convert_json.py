import json

with open('doc/data.json', 'r') as f:
    data = json.load(f)

objects = data['items']
locations = data['house_locations']
menu = data['menu']