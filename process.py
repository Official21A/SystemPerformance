import psutil


p = psutil.Process()


print("::Process info >> ")


print(f" [self]    {p}")
print(f" [name]    {p.name()}")

print(f" [exe]   {p.exe()}") # '/usr/bin/python'
print(f" [cwd]   {p.cwd()}") # '/home/giampaolo'
print(f" [cwd_line]    {p.cmdline()}") # ['/usr/bin/python', 'main.py']


print(f" [pid]   {p.pid}") # 7055
print(f" [ppid]   {p.ppid()}") # 7054


print(f" [children]   {p.children(recursive=True)}")
print(f" [parent]    {p.parent()}")


print(f" [status]    {p.status()}") # 'running'
print(f" [username]    {p.username()}") # 'giampaolo'

print(f" [create_time]    {p.create_time()}") # 1267551141.5019531
print(f" [terminal]    {p.terminal()}") # '/dev/pts/0'

print(f" [uids]    {p.uids()}")
print(f" [gids]    {p.gids()}")


print(":: Cpu >> ")
print(f" [times]    {p.cpu_times()}")
print(f" [percent]    {p.cpu_percent(interval=1.0)}") # 12.1
print(f" [affinity]    {p.cpu_affinity()}") # [0, 1, 2, 3]
print(f" [number]   {p.cpu_num()}") # 1


print(":: Memory >> ")
print(f" [info]    {p.memory_info()}")
print(f" [full]    {p.memory_full_info()}") # "real" USS memory 
									 		# usage (Linux, macOS, Win only)
print(f" [percent]   {p.memory_percent()}") # 0.7823
print(f" [maps]   {p.memory_maps()}")

print()
print(f" [io_counters]    {p.io_counters()}")
print(f" [open_files]   {p.open_files()}")

print(f" [connections]   {p.connections()}")


print(f" [thread number]    {p.num_threads()}") # 4
print(f" [num_fds]   {p.num_fds()}") # 8
print(f" [threads]   {p.threads()}")


print(f" [ctx swithches]   {p.num_ctx_switches()}")

print(f" [nice]    {p.nice(10)}")
print(f" [ionice]   {p.ionice(psutil.IOPRIO_CLASS_IDLE)}") # IO priority 
												   		   #(Win and Linux only)

print(f" [rlimit]   {p.rlimit(psutil.RLIMIT_NOFILE, (5, 5))}") # set resource 
															   # limits (Linux only)


print(f" [environment]    {p.environ()}")

print(f" [as_dict]    {p.as_dict()}")

"""
	p.is_running()

	p.suspend()
	p.resume()

	p.terminate()
	p.kill()
	p.wait(timeout=3)
	<Exitcode.EX_OK: 0>
"""

print("\n::>>")
print(psutil.test())