from Character import *
from item import *
import timeit
from time import sleep
from threading import Thread
from _weapon import *
from Actions import *

def playerAttackTime():

    inp = input(">>")
    demo = player.useWeapon('claws')
    return timeit.timeit(playerAttackTime)

player = Player()
player.setInfo()

#name, desc, item_type=0, value=1, dmg_range, sta_cost
claws = Weapon('claws', 'Made with Goblin Iron', (10,20), 2, 2)
spidy = Enemy()
spidy.setInfo('Spidy', 70, claws)
player.addToInventory(claws)
player.info()	
spidy.info()
player.addToInventory(wood_sword)

combat(player, spidy)

	