import json
import os

from netmiko import ConnectHandler

USERNAME = os.getenv("NET_USERNAME")
PASSWORD = os.getenv("NET_PASSWORD")

with open("Python/Assignment/inventory02.json") as f:
    inventory = json.load(f)

loopback_count = 0

for hostname, router in inventory["routers"].items():

    print(f"\nConnecting to {hostname}")
    loopback_count += 1

    try:

        conn_router = {}
        conn_router["device_type"] = router["device_type"]
        conn_router["host"] = router["host"]
        conn_router["username"] = USERNAME
        conn_router["password"] = PASSWORD
        

        print(conn_router)
        print(router["site"])

        conn = ConnectHandler(**conn_router)

        config_commands = []
        config_commands.append(f"banner motd # Welcome to {router['site']} #")

        output = conn.send_config_set(config_commands)

        print(output)

        conn.save_config()

    except Exception as e:

        print(f"Failed on {hostname}")
        print(e)