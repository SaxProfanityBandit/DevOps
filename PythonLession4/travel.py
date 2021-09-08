suitcase = []
suitcase.append("Clothes")
suitcase.append("Phone Charger")
suitcase.append("Passport")
suitcase.append("Suspicious Bag")

i = suitcase.index("Phone Charger")
suitcase.insert(i, "Bath Towel")
suitcase.pop(len(suitcase)-2)

print(suitcase)

first = suitcase[:2]
middle = suitcase[1:3]
last = suitcase[2]

for thing in suitcase:
	print(thing)
