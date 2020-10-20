import psutil


print(f"::Sen temperatures >> {psutil.sensors_temperatures()}")

print(f":: Sen fans >> {psutil.sensors_fans()}")

print(f":: Sen battery >> {psutil.sensors_battery()}")
