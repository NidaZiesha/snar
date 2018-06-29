import threading
import time


class playerThread(threading.Thread):

    def __init__(self, delay):
        threading.Thread.__init__(self)
        self.delay = delay

    def run(self, spidy, player):
        inp = input(">>")
        time.sleep(self.delay)
        if inp:
            if inp == 'attack':
                spidy.hp -= player.useWeapon('claws')
            else:
                spidy.attack(player)
        else:
            spidy.attack(player)
        time.sleep(self.delay)

class enemyThread(threading.Thread):

    def __init__(self, delay):
        threading.Thread.__init__(self)
        self.delay = delay

    def run(self, spidy, player):
        spidy.attack(player)
        time.sleep(self.delay)
