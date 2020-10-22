import psutil


print(f"::Virtual memory >> {psutil.virtual_memory()}")

print(f"::Swap memory >> {psutil.swap_memory()}")
