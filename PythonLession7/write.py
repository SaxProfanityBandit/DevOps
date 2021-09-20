#!/usr/bin/env python3

even = [x for x in range(100) if x % 2 == 0]
my_file = open("even.txt", "w")

for line in even:
	my_file.write(str(line) + "\n")

my_file.close()

my_file2 = open("even.txt","r")


"""
for line in my_file2:
	print(line, end="")
"""

i = 0
while i < 10:
	print(my_file2.readline(), end="")
	i += 1

my_file2.close()
