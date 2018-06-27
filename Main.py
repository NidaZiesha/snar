from Character import *
from item import *
from time import sleep
from threading import Thread

player = Player()
player.setInfo()

#name, desc, item_type=0, value=1, dmg_range, sta_cost
claws = Weapon('claws', 'Made with Goblin Iron', (10,20), 2, 1, 2)
spidy = Enemy()
spidy.setInfo('Spidy', 70, claws)
player.addToInventory(claws)
player.info()
spidy.info()

while(player.isAlive() and spidy.isAlive()):

    # inp = None
    print('\n\n')
    # Thread(target = check).start()
    # global inp
    #inp = input()
    try:
        for i in range(0,3):
            sleep(1)
        spidy.attack(player)
    except KeyboardInterrupt:
        # inp = input()
        spidy.hp -= player.useWeapon('claws')

    # spidy.attack(player)


    player.info()
    spidy.info()


# Info class is showing too much info
# Can't use in combat
# Check the combat options
