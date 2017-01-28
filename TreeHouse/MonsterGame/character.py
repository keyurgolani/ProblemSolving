from combat import Combat
import random

class Character(Combat):
    attack_limit = 10
    experience = 0
    base_hit_points = 10

    def attack(self):
        return random.randint(1, self.attack_limit) + self.weapons[self.weapon][0] > 0

    def get_weapon(self):
        weapon_choice = raw_input("Weapon ([S]word, [A]xe, [B]ow): ").lower()
        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'Sword'
            elif weapon_choice == 'a':
                return 'Axe'
            elif weapon_choice == 'b':
                return 'Bow'
        else:
            print "Bad choice.\nChoose the correct weapon from given choices."
            return self.get_weapon()


    def __init__(self, **kwargs):
        self.name = raw_input("Name: ")
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
		return 'Name: {}\nWeapon: {}\nHP: {}\nXP: {}'.format(self.name,
											  self.weapon,
											  self.hit_points,
											  self.experience)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def leveled_up(self):
        return self.experience >= 5
