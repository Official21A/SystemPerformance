import psutil


print(f"::Net IO counters >> {psutil.net_io_counters(pernic=True)}")

print(f"::Net connections >> {psutil.net_connections()}")

print(f"::Net addrs >> {psutil.net_if_addrs()}")

print(f"::Net stats >> {psutil.net_if_stats()}")