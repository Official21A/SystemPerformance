import sys

from headers.system import *
from headers.altras import *
from headers.processing import *


def run(argv):

	if "high_check" in argv:
		hardware_full_check()
		alters_full_check()
		process_full_check()
		return

	if "low_check" in argv:
		cpu_check()
		network_check()
		process_check()
		return	

	if "hardware" in argv:
		hardware_full_check()
	else:
		if "CPU" in argv:
			cpu_check()
		if "memory" in argv:
			memory_check()
		if "disks" in argv:
			dicks_check()

	if "altras" in argv:
		alters_full_check()
	else:
		if "NET" in argv:
			network_check()
		if "other" in argv:
			other_check()
		if "SENS" in argv:
			sensors_check()		

	if "full_proc" in argv:
		process_full_check()
	else:
		if "proc" in argv:
			process_check()
		if "procAPI" in argv:
			API_check()		


if __name__ == "__main__":
	run(sys.argv)