import sys
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll

class Game:
	def setup(self):
		self.player = Character()
		self.monsters = [
		Goblin(),
		Troll(),
		Dragon()
		]
		self.monster = self.getNextMonster()

	def getNextMonster(self):
		try:
			return self.monsters.pop(0)
		except IndexError:
			return None

	def monsterTurn(self):
		if self.monster.attack():
			print '{} is attacking'.format(self.monster)
			if raw_input('Dodge? Y/n: ').lower() != 'n':
				if self.player.dodge():
					print 'You dodged the attack'
				else:
					self.player.hit_points -= 1
					print 'You got hit anyway!'
			else:
				print '{} hit you for 1 Hit Point'.format(self.monster)
				self.player.hit_points -= 1
		else:
			print "{} isn't attacking this turn.".format(self.monster)

	def playerTurn(self):
		playerChoice = raw_input('[A]ttack, [R]est, [Q]uit : ').lower()
		if playerChoice == 'a':
			print "You're attacking {}!".format(self.monster)
			if self.player.attack():
				if self.monster.dodge():
					print '{} dodged your attack!'.format(self.monster)
				else:
					if self.player.leveled_up():
						self.monster.hit_points -= 2
					else:
						self.monster.hit_points -= 1
					print 'You hit {} with {}'.format(self.monster, self.player.weapon)
			else:
				print 'You missed!'
		elif playerChoice == 'r':
			self.player.rest()
		elif playerChoice == 'q':
			sys.exit()
		else:
			self.playerTurn()


	def cleanup(self):
		if self.monster.hit_points <= 0:
			self.player.experience += self.monster.experience
			print 'You killed {}'.format(self.monster)
			self.monster = self.getNextMonster()

	def __init__(self):
		self.setup()
		while self.player.hit_points and (self.monster or self.monsters):
			print '\n' + '='*20
			print self.player
			self.monsterTurn()
			print '-'*20
			self.playerTurn()
			self.cleanup()
			print '\n' + '='*20

		if self.player.hit_points:
			print 'You Win!'
		elif self.monsters or self.monster:
			print 'You lose!'
		sys.exit()


Game()
