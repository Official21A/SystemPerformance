import psutil


print(f"::System users >> {psutil.users()}")

print(f"::Sys boot time >> {psutil.boot_time()}")

