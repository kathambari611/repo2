routers = ["R1","R2","R3"]
app = ["router","switch"]
model = ["3660","3750","7200"]

def loop_fun(device, apps, models):
    for router, md1 in zip( device, models):
        print(f"{router} = {md1}")

    print(apps)

loop_fun(routers, app, model)