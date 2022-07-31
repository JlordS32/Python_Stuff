import json

with open("data.json", "r") as f:
    json_object = json.loads(f.read())

print(json_object['names'])