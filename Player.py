"""
The Character class is the base class for Player and Enemy

Types of Characters:
Player = 1
Enemy = 2

HP (Health Points are supposed to be common for both the types of Characters)


"""
class Character(object):
    # Set values during Object (Character) initialization
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

    def attack(self, enemy):
        if self.type == 1:
            print("Select your weapon to attack!\n")
            self.showInventory()
            print("\n\nWhat do you wanna use?")
            weapon = input().capitalize()
            print(weapon)


class Player(Character):
    """docstring for Player."""

    inventory = {'Sword': (10,20), 'Gun': (15,30)}
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



player = Player()
player.setInfo()
player.display()
player.isAlive()
player.attack(player)
