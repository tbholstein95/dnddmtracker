class PlayerCharacter:
	def __init__(self, name):
		self.name = name
		self.level = 0
		self.hit_dice = 0

	def get_name(self):
		return self.name

	def get_level(self):
		return self.level

	def get_hit_dice(self):
		return self.hit_dice

	def set_name(self, name):
		self.name = name

	def set_level(self, level):
		self.level = level

	def set_hit_dice(self, level):
		self.hit_dice = level

	def use_hit_dice(self, amount):
		self.hit_dice -= amount