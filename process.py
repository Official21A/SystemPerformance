import psutil


print(f"::System pids >> {psutil.pids()}")

p = psutil.Process(7055)


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
print(f" [parents]   {p.parents()}")


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

>>>
>>> p.environ()
{'LC_PAPER': 'it_IT.UTF-8', 'SHELL': '/bin/bash', 'GREP_OPTIONS': '--color=auto',
'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg',
 ...}
>>>
>>> p.as_dict()
{'status': 'running', 'num_ctx_switches': pctxsw(voluntary=63, involuntary=1), 'pid': 5457, ...}
>>> p.is_running()
True
>>> p.suspend()
>>> p.resume()
>>>
>>> p.terminate()
>>> p.kill()
>>> p.wait(timeout=3)
<Exitcode.EX_OK: 0>
>>>
>>> psutil.test()
USER         PID %CPU %MEM     VSZ     RSS TTY        START    TIME  COMMAND
root           1  0.0  0.0   24584    2240            Jun17   00:00  init
root           2  0.0  0.0       0       0            Jun17   00:00  kthreadd
...
giampaolo  31475  0.0  0.0   20760    3024 /dev/pts/0 Jun19   00:00  python2.4
giampaolo  31721  0.0  2.2  773060  181896            00:04   10:30  chrome
root       31763  0.0  0.0       0       0            00:05   00:00  kworker/0:1
>>>