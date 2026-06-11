import os
import json
from netmiko import ConnectHandler

with open("Python/inventory07.json") as f:
    inventory = json.load(f)

for router in inventory["routers"]:

    router["username"] = os.getenv("NET_USERNAME")
    router["password"] = os.getenv("NET_PASSWORD")

    print(f"\nConnecting to {router['host']}")

    conn = ConnectHandler(**router)

    output = conn.send_command("show ip interface brief")

    print(output)

    conn.disconnect()