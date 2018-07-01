from random import randint
# Stamina changed to sp (Stamina Points)
class Character(object):

    def setInfo(self, name, hp):
        self.name = name
        self.hp = hp
        self.invent = {}

    def isAlive(self):
        if self.hp >0:
            print(f"{self.name} is Alive.")
            return 1
        else:
            print(f"{self.name} is Dead.")
            return 0


class Player(Character):
    """docstring for Player."""

    def setInfo(self):
        inp = input("You-Know-Who needs your name. \n\n>>")
        super(Player, self).setInfo(inp, 100)
        self.gold = 0
        self.sp = 100
        self.invent = {}


    def info(self):
        print(f"{self.name} hp: {self.hp} gold: {self.gold} sta: {self.sp}")

    # Creates a key, value pair for objects added to inventory
    def addToInventory(self, obj):
        self.invent[f'{obj.name}'] = obj


    def displayInventory(self):
        print(self.invent)

    # On using weapon, the sp of player is reduced and the damage value is
    # returned which will be used as damage done to enemy
    # If the player does not have enough stamina then 0 damage will be
    # done to enemy

    def attack(self, target):
        inp = input('')
        if inp in self.invent.keys():
            weapon = self.invent[inp]
            self.sp -= weapon.sta_cost
            target.hp -= randint(*weapon.dmg_range)
        else:
            print('Missed')

class Enemy(Character):

    #inventory = {'Sword': (5,15), 'Gun': (10,25)}
    def __init__(self, name, hp, gold, dmg_range):
    	self.name = name
    	self.hp = hp
        self.gold = randint(10,100)
    	self.dmg_range = dmg_range
    	self.invent = {}

    def info(self):
        print(f"{self.name} hp: {self.hp} gold: {self.gold}")

    def attack(self, target):
        target.hp -= randint(*self.dmg_range)
