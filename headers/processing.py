DIR_PATH = "../process/"


def process_check():
	exec(open(f'{DIR_PATH}process.py').read())


def API_check():
	exec(open(f'{DIR_PATH}process_API.py').read())


def process_full_check():
	process_check()
	API_check()