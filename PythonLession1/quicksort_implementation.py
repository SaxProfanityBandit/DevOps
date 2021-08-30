#importing of libraries
import random
#The maximum size of the random data/list.
list_size = 100

#Maximum size of random number
max_random = 100
x = 0
my_array = []
while x < list_size: #creating a while loop to fill the array.
	my_array.append(random.randint(0, max_random))
	#print(my_array[x]) Printed the values for testing
	x += 1


def quicksort(unsorted):
	
	less = []
	equal = []
	greater = []
	if len(unsorted) > 1:
		pointer = unsorted[0]
		for x in unsorted:
			if x < pointer:
				less.append(x)
			elif x == pointer:
				equal.append(x)
			elif x > pointer:
				greater.append(x)
		return quicksort(less)+equal+quicksort(greater)
	else: 
		return unsorted

my_array_sorted = quicksort(my_array)
for i in my_array_sorted:
	print(i)
