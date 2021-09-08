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

path = arguments[0]
file_to_find = arguments[1]

#os.system('ls {}'.format(path))

if os.path.isfile("{}/{}".format(path, file_to_find)) == True:
	print("File found!")
	print(os.path.isfile("{}/{}".format(path, file_to_find)))
	print("{}/{}".format(path, file_to_find))
else:
	print("Couldn't find file.")

