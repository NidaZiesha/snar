from random import randint
class Item(object):
    # Base class for 'Weapon' class and 'Potions' class
    # __init__ takes name, desc - description, item_type and value
    # name - for identifying the item in inventory of the player or just
    #      for naming
    # description - provides description of the item. Not necessary
    #      Provided default value to allow quick creation of normal items
    # value - value which will be converted to gold on selling at shop
    #      (Not added yet). Type:int
    def __init__(self, name, desc='No description.', value=1):
        self.name = name
        self.description = desc
        self.value = value

    # Displays information of the item when called
    def info(self):
        print('Name: ', self.name)
        print('Desc: ',self.description)
        print('Value: ',self.value)

    # The 'use' mehtod takes 'target' as argument where target is the name of
    # the object the item will affect.
    def use(self, target=None):
        pass

class Weapon(Item):
    #   takes name, desc, value, dmg_range, sta_cost
    #   use super to assign name, desc, item_type, value to prevent repetitive code
    # dmg_range - tuple containing 2 values - min and max damage of the weapon
    # sta_cost  - 'Stamina Cost'. Type:int
    def __init__(self, name, desc, dmg_range, sta_cost, value=1):
        super(Weapon, self).__init__(name, desc, value)
        self.dmg_range = dmg_range
        self.sta_cost = sta_cost

    def __repr__(self):
        return f'{self.name}'

    def info(self):

        super(Weapon, self).info()
        print('Damage: ', self.dmg_range[0], '-', self.dmg_range[1])
        print('Stamina Cost: ', self.sta_cost)

    def inflictDamage(self, player):
       dmg = random.randint(self.dmg_range[0], self.dmg_range[1])
       player.hp -= dmg

    # For providimg upgrades to weapos in game
    # upgradeWeapon - Take 2 args.
    # new_range is Tuple containing new value for dmg_range
    # new_sta_cost is type:int containing new value for sta_cost
    def upgradeWeapon(self, new_range, new_sta_cost):
        self.dmg_range = new_range
        self.sta_cost = new_sta_cost

# Class Food is sub-class of class Item.
# It will be used as items which will heal/regen the players
# hp and sp points
# The extra param taken as compared to Item is hp_sp_amt which
# will be tuples in the format (hp_heal_amt, sp_heal_amt)
class Food(Item):

    def __init__(self, name, desc, value=1, hp_sp_amt=(0,0)):
        super(Food, self).__init__(name, desc, value)
        self.hp_sp_amt = hp_sp_amt

    # The 'use' mehtod takes 'target' as argument where target is the name of
    # the object the item will affect.
    def use(self, target):
        target.hp += self.hp_sp_amt[0]
        target.sp += self.hp_sp_amt[1]
