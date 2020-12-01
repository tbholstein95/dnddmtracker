from abc import ABC, abstractmethod
options_dict = {}


def merge_dicts(higher, deeper):
	concat_string = higher['0'] + deeper['0']
	deeper.update(higher)
	deeper['0'] = concat_string
	return deeper


def leave():
	print("Leaving")
	return 0


class PlayerCharacter:
	def __init__(self):
		self.name = None
		self.level = 0
		self.hit_dice = 0
		self.max_hit_dice = 0

	def get_name(self):
		return self.name

	def get_level(self):
		return self.level

	def get_hit_dice(self):
		return self.hit_dice

	def get_max_hit_dice(self):
		return self.max_hit_dice

	def set_name(self, name):
		self.name = name

	def set_level(self):
		number = int(input("What level should this character be?"))
		self.level = int(number)

	def set_hit_dice(self, level):
		self.hit_dice = level

	def set_max_hit_dice(self, level):
		self.max_hit_dice = level

	def reset_current_hit_dice(self):
		self.hit_dice = self.get_max_hit_dice()

	def use_hit_dice(self):
		amount_to_use = int(input("How many hit dice were used?"))
		current_hit_dice = self.get_hit_dice()
		if current_hit_dice == 0:
			print("No hit dice left")
		else:
			self.hit_dice -= amount_to_use
			print("Used Hit Dice")

	def base_change_level(self):
		self.set_level()
		self.set_max_hit_dice(self.get_level())
		self.reset_current_hit_dice()

	def create_player_character_options(self):
		# First 3 options, do not use 0-2 in other classes.
		options_dict['0'] = "What action are you counting?\n[1]: Use Hit Dice\n[2]: Reset Hit Dice\n"
		options_dict['1'] = self.use_hit_dice
		options_dict['2'] = self.reset_current_hit_dice
		return options_dict



