import json

with open("Python/device.json") as f:
    data = json.load(f)

print(data["hostname"])

