#User Input
salary = int(input("Enter gross salary: "))
taxrate = int(input("Enter your taxrate in percentages: "))
rent = int(input("Enter your monthly rent: "))

#Converting the tax percentage into a float for multiplication
taxdec = taxrate / 100
#Calculating how much of the salary is actually tax.
tax = salary * taxdec

#Calculating Net Income
netsalary = salary - tax

#Calculating remaining after rent
remains = netsalary - rent

#Printing the result
print("Remaining: " + str(remains))
