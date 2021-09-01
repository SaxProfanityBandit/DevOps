#!/usr/bin/env python3

#Constants
pension_age = 65

#User Input
age = int(input("Write your age: "))
#Calculating the actual difference.
difference = pension_age - age

#Console print.
print("You have {} years remaining until your pension.".format(difference))

