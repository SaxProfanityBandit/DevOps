def grade_converter(grade):
	if grade >= 90:
		return "A"
	elif grade >= 80: #and grade < 90:
		return "B"
	elif grade >= 70: #and grade < 80:
		return "C"
	elif grade >= 65: #and grade < 70:
		return "D"
	else:
		return "F"
#Should print A
#print(grade_converter(92))
#Should print C
#print(grade_converter(70))
#Should print F
#print(grade_converter(61))"

print(grade_converter(int(input("Write the test score in points (0-100): "))))
