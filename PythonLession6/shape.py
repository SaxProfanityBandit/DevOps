class Shape(object):
	def __init__(self, number_of_sides):
		self.number_of_sides = number_of_sides

class Triangle(Shape):
	def __init__(self, side1, side2, side3, angle1, angle2, angle3):
		self.number_of_sides = 3
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3

	def check_angles(self):
		angles_sum = self.angle1 + self.angle2 + self.angle3
		if angles_sum >= 180:
			return True
		else:
			return False

class Equilateral(Triangle):
	angle = 60
	def __init__(self, side):
		self.angle1 = self.angle
		self.angle2 = self.angle
		self.angle3 = self.angle
		self.side1 = side
		self.side2 = side
		self.side3 = side
		self.number_of_sides = 3

square = Shape(4)
triangle1 = Triangle(3, 3, 3, 60, 60, 60)
triangle2 = Triangle(5, 7, 9, 90, 60, 30)
equilatera = Equilateral(40)


print(square.number_of_sides)
print(triangle1.number_of_sides)
print(triangle2.number_of_sides)
print("T1:", triangle1.check_angles(), "T2:", triangle2.check_angles())
print("E1: ", equilatera.check_angles())
print(equilatera.number_of_sides)
