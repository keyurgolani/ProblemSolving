import random

class Combat(object):
    dodge_limit = 6
    attack_limit = 6

    weapons = {
    'Sword' : [0, 0],
    'Axe' : [0, 0],
    'Bow' : [0, 0]
    }

    def dodge(self):
        return random.randint(1, self.dodge_limit) > 4


    def attack(self):
        return random.randint(1, self.attack_limit) > 4
