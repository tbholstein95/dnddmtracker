class Barbarian:

	hit_dice = None
	level = None
	hit_dice = level
	rage = None

	def __init__(self, name):
		self.name = name

	def set_rage(self, level):
		if level < 3:
			rage = 2
			return rage
		elif 3 <= level < 6:
			rage = 3
			return rage
		elif 6 <= level < 12:
			rage = 4
			return rage
		elif 12 <= level < 20:
			rage = 5
			return rage
		elif level >= 20:
			rage = 100
			return rage


	def use_hit_dice(self, amount):
		Barbarian.hit_dice += amount


def create_barbarian():
	name = input("What is the barbarian's name?\n")
	level = input("What level is this barbarian?\n")
	


