class Character(object):
    experience = 0
    hit_points = 10

    def get_weapon(self):
        weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()
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
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
		return 'Name: {} Weapon: {}, HP: {}, XP: {}'.format(self.name,
											  self.weapon,
											  self.hit_points,
											  self.experience)
