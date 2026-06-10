import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    "192.168.10.2",
    username="admin",
    password="Password123",
    look_for_keys=False,
    allow_agent=False
)

print("connected")