#!/usr/bin/env python3

even = [x for x in range(2,20) if x % 2 == 0]
with open("even.txt", "w") as my_file:
	for line in even:
		my_file.write(str(line) + "\n")


with open("even.txt","r") as my_file2:
	for _ in range(10):
		print(my_file2.readline().strip())




"""
i = 0
while i < 10:
	print(my_file2.readline(), end="")
	i += 1

my_file2.close()
"""
