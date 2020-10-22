DIR_PATH = "../inners/"


def network_check():
	exec(open(f'{DIR_PATH}network.py').read())


def other_check():
	exec(open(f'{DIR_PATH}others.py').read())


def sensors_check():
	exec(open(f'{DIR_PATH}sensors.py').read())


def alters_full_check():
	network_check()
	other_check()
	sensors_check()	