"""
The Character class is the base class for Player and Enemy

Types of Characters:
Player = 1
Enemy = 2

HP (Health Points are supposed to be common for both the types of Characters)


"""
from item import Weapon
from random import randint
class Character(object):
    # Set values during Object (Character) initialization
	def __init__(self):
		self.invent = {}
		
    def setInfo(self, name, type, hp):
        self.name = name
        self.type = type
        self.hp = hp

    def isAlive(self):
        # Checks whether the Character is Alive
        if self.type == 1: # if Player
            if self.hp > 0:
                print("You're still Alive")
            else:
                print("You is dead. You didn't play well, huh")
        elif self.type == 2: # if other than Player (Enemy, or subclasses of Enemy)
            if self.hp > 0:
                pass
            else:
                print(f"You defeated {self.name}")
                del(self) # Deletes the Enemy object, frees memory

 
			
            


class Player(Character):
    """docstring for Player."""

    inventory = {'sword': (10,20), 'gun': (15,30)}
    def setInfo(self):
        inp = input("You-Know-Who needs your name. \n\n>>")
        super(Player, self).setInfo(inp, 1, 100)
        self.stamina = 100


    def display(self):
        print("You are",self.name)
        print("Health: ", self.hp)
        print("Stamina: ", self.stamina)

    def showInventory(self):
        print("\nHere's the stuff in your Backpack\n\n")
        for items in self.inventory:
            print(items)
			
	 # Creates a key, value pair for objects added to inventory
    def addToInventory(self, obj):
        self.inventory[f'{obj.name}'] = obj
			
	def attack(self):
		weapon = input()
		if weapon in invent.keys():
			return randint(*invent[weapon].dmg_range)
		else:
			print('MISSED')
			




	
#player = Player()
#claws = Weapon('claws', 'Made with Goblin Iron', (10,20), 2, 1, 2)
#player.addToInventory(claws)