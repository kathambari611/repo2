import json
import os

from netmiko import ConnectHandler

USERNAME = os.getenv("NET_USERNAME")
PASSWORD = os.getenv("NET_PASSWORD")

with open("Python/Assignment/inventory.json") as f:
    inventory = json.load(f)

loopback_count = 0

for hostname, router in inventory["routers"].items():

    print(f"\nConnecting to {hostname}")
    loopback_count += 1

    try:

        router["username"] = USERNAME
        router["password"] = PASSWORD

        print(router)

        conn = ConnectHandler(**router)

        config_commands = [

            "interface loopback10",
            "description Created_By_Python"]
        config_commands.append(f"ip address 10.10.10.{loopback_count} 255.255.255.255")

        output = conn.send_config_set(config_commands)

        print(output)

        conn.save_config()

    except Exception as e:

        print(f"Failed on {hostname}")
        print(e)