import random


class DiceRoll:
	def __init__(self,dice):
		self.dice = dice

	def d6(self):
		self.min_roll = 1
		self.max_roll = 6

		dice = random.rantint(min_roll,max_roll)

		print(dice)


my_dice = DiceRoll()
my_dice.d6()




