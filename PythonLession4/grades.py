alice = {
	'name'     : 'Alice',
	'homework' : [100.0, 92.0, 98.0, 100.0],
	'quizzes'  : [82.0, 83.0, 91.0],
	'tests'    : [89.0, 97.0]
}

lars = {
	'name'     : 'Lars',
	'homework' : [90.0, 97.0, 75.0, 92.0],
	'quizzes'  : [88.0, 40.0, 94.0],
	'tests'    : [75.0, 90.0]
}

tomas = {
	'name'     : 'Tomas',
	'homework' : [0.0, 87.0, 75.0, 22.0],
	'quizzes'  : [0.0, 75.0, 78.0],
	'tests'    : [100.0, 100.0]
}

students = [alice, lars, tomas]

for student in students:
	for key, item in student.items():
		print(key, item)
	print()

def average(grades):
	return sum(grades) / len(grades)

def get_average(student):
	dict_average = {}
	total_average = 0
	for key, item in student.items():
		if type(item) is list:
			dict_average[key] = average(item)
	for key, item in dict_average.items():
		if key == "homework":
			total_average += dict_average[key] * 0.10
		elif key == 'quizzes':
			total_average += dict_average[key] * 0.3
		elif key == 'tests':
			total_average += dict_average[key] * 0.6
	return total_average

print(get_average(alice))

def get_letter_grade(score):
	if score >= 90:
		return 'A'
	elif score >= 80:
		return 'B'
	elif score >= 70:
		return 'C'
	elif score >= 60:
		return 'D'
	else:
		return F


print("Alice: ", get_letter_grade(get_average(alice)))	
print("Lars: ", get_letter_grade(get_average(lars)))	
print("Tomas: ", get_letter_grade(get_average(tomas)))	

def get_class_average(student_list):
	results = []
	for student in student_list:
		results.append(get_average(student))
	return sum(results) / len(student_list)
class_average = get_class_average(students)
print("Class average:", class_average, "/", get_letter_grade(class_average))
