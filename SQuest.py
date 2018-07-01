from Character import *
from Actions import *
from random import randint
from Main import *

def SQuest(self):

    print("Enter a friends name")
    fname = input('>' )
    print(f""" You instantly got addicted to the new game you recently
    discovered at the Fun Fair.
    You have a childhood friend who is your grandparents neighbour. His parents
    own a farm.
    You and {faname} go to the farm where you two made some cool cardboard
    cutouts to practise on.
        """)
    combat(player,enemy)

if player.hp > 0:
    print('You won! Congratulations on the gold.')
    player.gold += randint(*enemy.gold)
else:
    pass

player.info()
