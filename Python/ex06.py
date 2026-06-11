import os
import json
from netmiko import ConnectHandler

with open("Python/inventory.json") as f:
    inventory = json.load(f)

router = inventory["R1"]

router["username"] = os.getenv("NET_USERNAME")
router["password"] = os.getenv("NET_PASSWORD")

conn = ConnectHandler(**router)

print(conn.send_command("show version"))

conn.disconnect()