from character import Character

class Warrior(Character):
    weapon = 'sword'

    def rage(self):
        self.attack_limit = 20

    def __str__(self):
        return 'Warrior, {}, {}'.format(self.weapon, self.attack_limit)
