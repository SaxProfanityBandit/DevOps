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


def quicksort(unsorted): #Defining the quicksort function
	
	#Defining the arrays that will "divide and conquer" the unsorted array.
	less = [] 
	equal = []
	greater = []
	if len(unsorted) > 1: #Has the array more than 1 number? if yes, sort, if no return the array.
		pointer = unsorted[0]
		for x in unsorted: 
		"""Decided from the index 0 value in the unsorted array, 		 x the current value of the array is placed 
		in the partion arrays for divide and conquer.""" 
			if x < pointer:
				less.append(x)
			elif x == pointer:
				equal.append(x)
			elif x > pointer:
				greater.append(x)
		return quicksort(less)+equal+quicksort(greater) #Recursively running the sorting until it is fully sorted.
	else: 
		return unsorted
#Printing it out in the console to see the finished sorting.
my_array_sorted = quicksort(my_array)
for i in my_array_sorted:
	print(i)
