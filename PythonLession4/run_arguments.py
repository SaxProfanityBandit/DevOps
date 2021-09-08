#Is this the running file or a module? Retreive arguments if its the former.
if __name__ == '__main__':
	import sys
	arguments = sys.argv[1:]

#Print all arguments
def print_args(*args):
	for argument in args:
		print(argument)


print_args(arguments)
