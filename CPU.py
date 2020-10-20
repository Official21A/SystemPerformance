import psutil

print(f"::CPU times >> {psutil.cpu_times()}")

for x in range(3):
    print(f"::CPU percent >> {psutil.cpu_percent(interval=1)}")

for x in range(3):
    print(f"::CPU percpu >> {psutil.cpu_percent(interval=1, percpu=True)}")

for x in range(3):
    print(f"::CPU nper >> {psutil.cpu_times_percent(interval=1, percpu=False)}")


print(f"::CPU count >> {psutil.cpu_count()}")

print(f"::CPU logical >> {psutil.cpu_count(logical=False)}")

print(f"::CPU stats >> {psutil.cpu_stats()}")

print(f"::CPU freq >> {psutil.cpu_freq()}")
