import battleship2

print("Hej!" + __name__)
print("Haj!" + battleship2.__name__)

if __name__ == "__main__":
	battleship = battleship2.Game(battleship2.battleship_run())
	battleship.main()
