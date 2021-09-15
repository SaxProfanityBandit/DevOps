import random as rand

grades = [rand.randint(0, 100) for i in range(10)]

def print_grades(grade_list):
	for grade in grade_list:
		print("Grade: ", grade)

def grades_sum(grade_list):
	return sum(grade_list)

def grades_average(grade_list):
	return grades_sum(grade_list) / len(grade_list)

def grades_varience(grade_list):
	average = grades_average(grade_list)
	varience = 0
	for grade in grade_list:
		varience += (average - grade) ** 2
	return (varience / len(grade_list))

def standard_deviation(variance):
	return variance * 0.5


print_grades(grades)
print("Sum of all grades:", grades_sum(grades))
print("Average of all grades:", grades_average(grades))
print("Varience of all grades:", grades_varience(grades))
print("Standard Deviation:", standard_deviation(grades_varience(grades)))
