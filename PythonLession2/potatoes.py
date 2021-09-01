#!/usr/bin/env python3


#User Input
potatoes = int(input("How many potatoes do you have? "))
nr_of_persons = int(input("How many people are arriving? "))

#Calculating each people's portion.
potatoes_each = potatoes / nr_of_persons
print("Each person gets {} potatoes each.".format(potatoes_each))
