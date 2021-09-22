import os
import sys

if __name__ == "__main__":
	arguments = sys.argv[1]

process_raw = os.popen('ps aux').read().splitlines()

for p in process_raw:
	if arguments in p:
		elements = p.split()
		print(elements)

