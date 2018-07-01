from Character import *
from _weapons import *
from _enemies import *
from Actions import *


player = Player()
player.setInfo()
player.addToInventory(wood_sword)

combat(player, spider)
