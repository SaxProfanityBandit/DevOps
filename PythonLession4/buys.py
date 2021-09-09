import sales
groceries = ['banana', 'orange', 'apple']

#print(sales.prices)

def compute_bill(food):
	total = 0
	for i in range(0, len(food)):
		for key, item in sales.prices.items():
			if food[i] == key and sales.stock[key] > 0:
				total += item
	return total

print(compute_bill(groceries))
