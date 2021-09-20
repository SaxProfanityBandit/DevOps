class Converter(object):
	count = 0
	def __init__(self, table):
		self.table = table
	def convert(self, roman_letters):
		result = 0
		for letter in roman_letters:
			for key, item in self.table.items():
				if letter == key:
					result += item
		return result

class SimpleCounter(Converter):
	def __init__(self):
		pass
	def increment(self, amount):
		self.count += amount
	def decrement(self, amount):
		self.count -= amount

class BankAccount(object):
	#Member variables
	def __init__(self, pin, amount):
		self.pin = pin
		self.amount = amount


	def deposit(self, pin, amount):
		if pin == self.pin:
			self.amount += amount
			print("You've added {} to your account. Current balance: {}".format(amount, self.amount))
		else:
			print("Wrong pin! Try again.")

	def withdraw(self, pin, amount):
		if pin == self.pin:
			if amount <= self.amount:
				self.amount -= amount
				print("You have withdrawed {} from your account. Current balance: {}".format(amount, self.amount))
			else:
				print("You don't have enough funds to withdraw:", amount)
		else:
			print("Wrong pin! Try again.")

	def get_balance(self, pin):
		if pin == self.pin:
			print("Your current balance is", self.amount)
		else:
			print("Wrong pin! Try again.")

	def change_pin(self, old_pin, new_pin):
		if old_pin == self.pin:
			self.pin = new_pin
			print("You have changed your pin successfully!")
		else:
			print("Wrong pin! Try again.")

class SavingsAccount(BankAccount):
	def __init__(self, pin, amount, rate):
		self.pin = pin
		self.amount = amount
		self.rate = rate
	
	def rate_bonus(self):
		rate = self.rate * self.amount
		self.amount += rate
		print("Your saving account's rate has increased your balance with:", rate)

class FeeSavingsAccount(SavingsAccount):
	def __init__(self, pin, amount, rate, fee):
		self.pin = pin
		self.amount = amount
		self.rate = rate
		self.fee = fee

	def withdraw(self, pin, amount):
		if pin == self.pin:
			if amount+self.fee <= self.amount:
				self.amount -= amount+self.fee
				print("You have withdrawed {} from your account, Fee: {}. Current balance: {}".format(amount, self.fee, self.amount))
			else:
				print("You don't have enough funds to withdraw:", amount)
		else:
			print("Wrong pin! Try again.")

class Adress(object):
	def __init__(self, street, postal_number, city, country):
		self.street = street
		self.postal_number = postal_number
		self.city = city
		self.country = country

class Person(object):
	def __init__(self, full_name, email, age, gender_identity, phone_number, hobby):
		self.full_name = full_name
		self.email = email
		self.age = age
		self.gender_identity = gender_identity
		self.phone_number = phone_number
		self.hobby = hobby

class Contact(Adress, Person):
	def __init__(self, full_name, email, age, gender_identity, phone_number, hobby, street, postal_number, city, country):
		Person.__init__(self, full_name, email, age, gender_identity, phone_number, hobby)
		Adress.__init__(self, street, postal_number, city, country)

	def print_info(self):
		print("""
My name is {} and my email is {}
I'm {} years old and I identify as {}.
My main hobby is {}.
To reach me, my phone number is {}

I live at:
Adress: {}
City: {} {}
Country: {}

Nice to meet you!
""".format(self.full_name, self.email, self.age, self.gender_identity, self.hobby, self.phone_number, self.street, self.postal_number, self.city, self.country))



converter = Converter({'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':
1000})

c = converter.convert('MMMCMLXXXVI')
print(c)

cc = SimpleCounter()
cc.increment(11)
cc.decrement(2)
print(cc.count)

account = BankAccount(3333, 10000)
account.deposit(3333, 500)
account.get_balance(3333)
account.withdraw(3333, 5000)
account.change_pin(3333, 5555)
account.withdraw(3333, 5000)

savings_account = SavingsAccount(1111, 100000, 0.02)
savings_account.rate_bonus()
savings_account.get_balance(1111)
fee_savings_account = FeeSavingsAccount(2222, 10000, 0.05, 15)
fee_savings_account.withdraw(2222, 3000)

rickard = Contact("Rickard Sahlgren", "rsahlgren@gmail.com", 28, "He/Him", "0721-******", "Tabletop games", "****************", 46166, "Trollhättan", "Sweden")

rickard.print_info()
