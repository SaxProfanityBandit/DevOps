abba = {'A1': 'Agnetha', 'B1': 'Björn', 'A2': 'Anna-Lena'}
#print(abba)

del abba['A2']
#print(abba)

abba['A2'] = 'Anni-Frid'
abba['B2'] = 'Benny'

#print(abba)
#print(len(abba))

inventory = {
	'gold' : 500,
	'pouch' : ['flint', 'twine', 'gemstone'],
	'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pouch'].sort()
inventory['pocket'] = ['seashell', 'berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

for key in inventory:
	print (inventory[key])
