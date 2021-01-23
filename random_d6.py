import random


class DiceRoll:
	def __init__(self,dice):
		self.dice = dice

	def d6(self):
		self.min_roll = 1
		self.max_roll = 6

		dice = random.randint(self.min_roll,self.max_roll)

		print(dice)


my_dice = DiceRoll(1)
my_dice.d6()




