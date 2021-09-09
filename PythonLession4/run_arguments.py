#!/usr/bin/env python3
import os

#Is this the running file or a module? Retreive arguments if its the former.
if __name__ == '__main__':
	import sys
	arguments = sys.argv[1:]

#Print all arguments
def print_args(*args):
	for argument in args:
		print(argument)

path_to = arguments[0]
file_to_find = arguments[1]

#os.system('ls {}'.format(path))


def find(path, filename):
	for root, dirs, files in os.walk(path):
		if filename in files:
			return os.path.join(root, filename)

print(find(path_to, file_to_find))
