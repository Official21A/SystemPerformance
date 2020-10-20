import psutil

print(f"::Disk partitions >> {psutil.disk_partitions()}")

print(f"::Disk usage >> {psutil.disk_usage('/')}")

print(f"::IO counters >> {psutil.disk_io_counters(perdisk=False)}")
