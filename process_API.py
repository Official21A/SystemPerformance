import psutil

for proc in psutil.process_iter(['pid', 'name']):
    print(proc.info)

print(f" >> {psutil.pid_exists(3)}")


def on_terminate(proc):
    print("process {} terminated".format(proc))