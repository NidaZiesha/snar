
# This is combat function. It accepts player objectt and current enemy.

def combat(player, enemy, room=None): # Future scope: add room for floor.
	
	playerTurn = True
	# The player attacks first. 
	while(player.isAlive() and enemy.isAlive()): # If either is alive, loop continues.

		print('\n\n')

		if playerTurn:
			enemy.hp -= player.attack()
			playerTurn = False # Change turn.
		else:
			enemy.attack(player)
			playerTurn = True
		
		player.info()
		enemy.info()