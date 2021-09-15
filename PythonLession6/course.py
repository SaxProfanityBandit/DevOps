class Course(object):
	points = 40
	def __init__(self, name):
		self.name = name
	def course_name(self):
		return self.name
	
	def course_points(self):
		return self.points

agile = Course("Agile Methodology")
linux = Course("Linux and Scripts")

print(linux.course_name(), linux.course_points())
print(agile.course_name(), agile.course_points())
