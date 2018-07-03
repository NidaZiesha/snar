from random import randint
from lexicon import *
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
        print(f"\n{self.name} hp: {self.hp} gold: {self.gold} sta: {self.sp}")

    # Creates a key, value pair for objects added to inventory
    def addToInventory(self, obj):
        self.invent[f'{obj.name}'] = obj


    def displayInventory(self):
        print([key for key in self.invent.keys()])

    # On using weapon, the sp of player is reduced and the damage value is
    # returned which will be used as damage done to enemy
    # If the player does not have enough stamina then 0 damage will be
    # done to enemy

    def attack(self, target):
        inp = input('>>')
        weapon_val = parse_input(inp, target)
        if weapon_val in self.invent.keys():
            weapon = self.invent[weapon_val]
            self.sp -= weapon.sta_cost
            target.hp -= randint(*weapon.dmg_range)
        else:
            print('Missed') # If weapon not in inventory

    # The use method takes item name as argument.
    # If the item exists in the inventory then call the 'use' method of the
    # item. After using the item, delete it from the inventory.
    def use(self, item):
        if item.name in self.invent.keys():
            item.use(self)
            del self.invent[item.name]
        else:
            print('No such item in inventory.')


class Enemy(Character):

    #inventory = {'Sword': (5,15), 'Gun': (10,25)}
    def __init__(self, name, hp, gold, dmg_range):
        self.name = name
        self.hp = hp
        self.gold = gold
        self.dmg_range = dmg_range
        self.invent = {}

    def info(self):
        print(f"{self.name} hp: {self.hp} gold: {self.gold}")

    def attack(self, target):
        target.hp -= randint(*self.dmg_range)
