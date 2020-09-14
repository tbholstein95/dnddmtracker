class Barbarian:

	def __init__(self, name):
		self.name = name
		self.level = 0
		self. rage = 0
		self.hit_dice = 0

	def get_name(self):
		return self.name

	def get_level(self):
		return self.level

	def get_rage(self):
		return self.rage

	def get_hit_dice(self):
		return self.hit_dice

	def set_name(self, name):
		self.name = name

	def set_level(self, level):
		self.level = level

	def set_rage(self, level):
		if level < 3:
			self.rage = 2
		elif 3 <= level < 6:
			self.rage = 3
		elif 6 <= level < 12:
			self.rage = 4
		elif 12 <= level < 20:
			self.rage = 5
		elif level >= 20:
			self.rage = 100

	def set_hit_dice(self, level):
		self.hit_dice = level

	def use_hit_dice(self, amount):
		self.hit_dice -= amount

	def create_barbarian(self):
		name = input("What is the barbarian's name?\n")
		level = int(input("What level is this barbarian?\n"))
		subclass = input("What subclass is " + name + "?\n")
		player = Barbarian(str(name))
		player.set_level(level)
		player.set_rage(level)
		player.set_hit_dice(level)
		print(player.get_name(), player.get_level(), player.get_rage(), player.get_hit_dice())






