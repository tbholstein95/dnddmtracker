class PlayerCharacter:
	def __init__(self):
		self.name = None
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

	def set_level(self):
		level = int(input("What level should this character be?"))
		self.level = level

	def set_hit_dice(self, level):
		self.hit_dice = level

	def use_hit_dice(self):
		amount_to_use = int(input("How many hit dice were used?"))
		current_hit_dice = self.get_hit_dice()
		if current_hit_dice == 0:
			print("No hit dice left")
		else:
			self.hit_dice -= amount_to_use