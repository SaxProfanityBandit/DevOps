class Employee(object):
	def __init__(self, employee_name):
		self.employee_name = employee_name
	def calculate_wage(self, hours):
		return hours * 20.00

class PartTimeEmployee(Employee):
	def calculate_wage(self, hours):
		return hours * 12.00
	def full_time_wage(self, hours):
		return super(PartTimeEmployee, self).calculate_wage(hours)

class Monkey(object):
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "Hi I'm {}".format(self.name)


empl = Employee("Rickard")
empl2 = PartTimeEmployee("David")

		
print(empl.calculate_wage(10))
print(empl2.calculate_wage(10))
print(empl2.full_time_wage(10))

monk = Monkey("Albert")
print(monk)
