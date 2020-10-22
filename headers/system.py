DIR_PATH = "/hardware/"


def cpu_check():
	exec(open(f'{DIR_PATH}CPU.py').read())


def disks_check():
	exec(open(f'{DIR_PATH}disks.py').read())


def memory_check():
	exec(open(f'{DIR_PATH}memory.py').read())


def hardware_full_check():
	cpu_check()
	disks_check()
	memory_check()	