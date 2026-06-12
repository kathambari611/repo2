import json
import os
import datetime

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

        conn = ConnectHandler(**conn_router)

        running_config = conn.send_command(
            "show running-config"
        )

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = f"/home/student/Documents/repo2/Python/Assignment/backups/{hostname}_{timestamp}.cfg"

        with open(backup_file, "w") as file:
            file.write(running_config)

        print(f"Backup saved -> {backup_file}")

        conn.disconnect()

    except Exception as e:

        print(f"Failed on {hostname}")
        print(e)