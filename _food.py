from item import Food
from random import randint
# Food format Food(name, desc, value, hp_sp_amt(0,0))

cheese = Food('cheese', "It's cheese. That's all I know", 10, (20,20))
chicken = Food('chicken', "Chicken dinner. Only for winners.", 20, (30,30))
mead = Food('meda', 'No pain but temporary gain.', 50, (50, -30))
dahi_shakkar = Food('dahi_shakkar', "Luck from cuznosun's mum ", randint(1,1000), (randint(1,1000), randint(1,1000)))
poison = Food('poison', 'To kill your enemies or rats silently.\n What if your enemies are rats?', 50, (-50 ,-50))
