def hello(name):
	print("Hello {}!".format(name))

#hello("Rickard")

def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False

#print(is_even(3))

def is_int(x):
	if type(x) is int:
		return True
	else:
		return False

#print(is_int(10.3))

def hotel_cost(nights):
	return 1200 * nights

def plane_ride_cost(city):
	if city.lower() == "barcelona":
		return 1830
	elif city.lower() == "rom":
		return 2500
	elif city.lower() == "paris":
		return 2220
	elif city.lower() == "london":
		return 1200
	else:
		return "The city you typed is spelled wrong or we do not fly there!"

def rental_bike_cost(days):
	if days >= 7:
		return ((days * 40) - 80)
	elif days >= 3 and days < 7:
		return ((days * 40) - 20)
	else:
		return days * 40

def trip_cost(city, days, spending_money):
	return rental_bike_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print("1. Trip: Barcelona: {} kr".format(trip_cost("Barcelona", 5, 600)))
print("2. Trip: Paris: {} kr".format(trip_cost("Paris", 14, 2000)))
print("3. Trip: London: {} kr".format(trip_cost("London", 10, 3000)))
