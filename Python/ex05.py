import json
from netmiko import ConnectHandler

with open("Python/inventory.json") as f:
    inventory = json.load(f)

router = inventory["R3"]

router["username"] = "admin"
router["password"] = "Password123"

conn = ConnectHandler(**router)

output = conn.send_command("show interface desc")

print(output)

conn.disconnect()