from Classes.subclasses.half_caster import *
paladin_dict = {}


class Paladin(HalfCaster):
	def __init__(self):
		self.max_divine_sense = 0
		self.current_divine_sense = 0
		self.max_lay_on_hands = 0
		self.current_lay_on_hands = 0
		self.charisma = 0
		self.channel_divinity = False
		self.max_cleansing_touch = 0
		self.current_cleansing_touch = 0
		self.paladin_options = {}
		super().__init__()

	def set_charisma(self):
		char = int(input("What is this Paladin's charisma modifier?"))
		self.charisma = char

	def get_charisma(self):
		return self.charisma

	def set_max_divine_sense(self):
		char = self.get_charisma()
		self.max_divine_sense = char + 1

	def set_current_divine_sense(self):
		self.current_divine_sense = self.max_divine_sense

	def get_current_divine_sense(self):
		return self.current_divine_sense

	def use_divine_sense(self):
		cur_divine_sense = self.get_current_divine_sense()
		if cur_divine_sense > 0:
			print("Paladin used Divine Sense")
			self.current_divine_sense -= 1
		else:
			print("Not enough points in Divine Sense left")

	def set_max_lay_on_hands_pool(self):
		cur_level = self.get_level()
		pool = 5 * cur_level
		self.max_lay_on_hands = pool

	def set_current_lay_on_hands_pool(self):
		self.current_lay_on_hands = self.max_lay_on_hands

	def get_current_lay_on_hands(self):
		return self.current_lay_on_hands

	def use_lay_on_hands_to_heal(self):
		amount = int(input("How many points would the Paladin like to use?"))
		if amount <= self.get_current_lay_on_hands():
			self.current_lay_on_hands -= amount
		else:
			print("Paladin only has {} points left".format(self.get_current_lay_on_hands()))

	def use_lay_on_hands_remove_poison(self):
		if self.get_current_lay_on_hands() >= 5:
			print("Spending 5 points to remove poison/disease")
			self.current_lay_on_hands = self.get_current_lay_on_hands() - 5
		else:
			print("Paladin only has {} points left".format(self.get_current_lay_on_hands()))

	def use_channel_divinity(self):
		if not self.channel_divinity:
			print("Used Channel Divinity")
			self.channel_divinity = True
		else:
			print("Already used Channel Divinity this long rest")

	def reset_channel_divinity(self):
		if self.channel_divinity:
			print("Reset Channel Divinity")
			self.channel_divinity = False
		else:
			print("Can still use Channel Divinity")

	def set_max_cleansing_touch(self):
		char = self.get_charisma()
		self.max_cleansing_touch = char

	def get_max_cleansing_touch(self):
		return self.max_cleansing_touch

	def set_current_cleansing_touch(self):
		totes_max = self.get_max_cleansing_touch()
		self.current_cleansing_touch = totes_max

	def get_current_cleansing_touch(self):
		return self.current_cleansing_touch

	def use_cleansing_touch(self):
		if self.get_current_cleansing_touch() > 0:
			print("Used Cleansing Touch")
			self.current_cleansing_touch -= 1
		else:
			print("Not enough Cleansing Touch points left")

	def create_paladin_options(self):
		self.paladin_options['0'] = "[5] = Use Divine Sense" + "[6]: Reset Divine Sense\n" + \
					"[7]: Use Lay on Hands to Heal\n" + "[8]: Use Lay on Hands to Cure Poison/Disease\n" + \
					"[9]: Reset Lay on Hands Pool\n" + "[10]: Use Channel Divinity\n" + \
					"[11]: Reset Channel Divinity\n" + "[12] Use Cleansing Touch\n" + "[13]: Reset Cleansing Touch\n"

		self.paladin_options['5'] = self.use_divine_sense
		self.paladin_options['6'] = self.set_current_divine_sense
		self.paladin_options['7'] = self.use_lay_on_hands_to_heal
		self.paladin_options['8'] = self.use_lay_on_hands_remove_poison
		self.paladin_options['9'] = self.set_current_lay_on_hands_pool
		self.paladin_options['10'] = self.use_channel_divinity
		self.paladin_options['11'] = self.reset_channel_divinity
		self.paladin_options['12'] = self.use_cleansing_touch
		self.paladin_options['13'] = self.set_current_cleansing_touch
		return self.paladin_options

	def change_paladin_level(self):
		self.set_charisma()
		self.change_half_caster_level()
		self.set_max_cleansing_touch()
		self.set_current_cleansing_touch()
		self.set_max_lay_on_hands_pool()
		self.set_current_lay_on_hands_pool()
		self.set_max_divine_sense()
		self.set_current_divine_sense()

	def list_options(self):
		selection = int(input(self.paladin_options.get("0")))
		print(selection)
		self.paladin_options["{}".format(selection)]()


class Devotion(Paladin):
	def __init__(self):
		self.holy_nimbus = False
		self.devotion_options = {}
		super().__init__()

	def use_holy_nimbus(self):
		if not self.holy_nimbus:
			print("Use Holy Nimbus")
			self.holy_nimbus = True
		else:
			print("Already used Holy Nimbus this Long Rest")

	def reset_holy_nimbus(self):
		if self.holy_nimbus:
			print("Refreshed Holy Nimbus")
			self.holy_nimbus = False
		else:
			print("Holy Nimbus is still good to be used")

	def create_devotion_options(self):
		self.devotion_options['0'] = "What action are you counting?\n" + "[14]: Use Holy Nimbus\n" + \
					"[15]: Reset Holy Nimbus\n" + "[16]: Change Level\n" + "[17]: Exit\n"
		self.devotion_options['14'] = self.use_holy_nimbus
		self.devotion_options['15'] = self.reset_holy_nimbus
		self.devotion_options['16'] = self.change_paladin_level
		self.devotion_options['17'] = leave
		return self.devotion_options

	def list_options(self):
		selection = int(input(self.devotion_options.get("0")))
		print(selection)
		self.devotion_options["{}".format(selection)]()


class Ancient(Paladin):
	def __init__(self):
		self.elder_champion = False
		self.ancient_options = {}
		super().__init__()

	def use_elder_champion(self):
		if not self.elder_champion:
			print("Used Elder Champion")
			self.elder_champion = True
		else:
			print("Already Used Elder Champion this long rest")

	def reset_elder_champion(self):
		if self.elder_champion:
			print("Reset Elder Champion")
			self.elder_champion = False
		else:
			print("Paladin can still use Elder Champion")

	def create_ancients_options(self):
		self.ancient_options['0'] = "[14]: Use Elder Champion\n" + "[15]: Reset Elder Champion\n" + \
					"[16]: Change Level\n" + "[17]: Exit\n"
		self.ancient_options['14'] = self.use_elder_champion
		self.ancient_options['15'] = self.reset_elder_champion
		self.ancient_options['16'] = self.change_paladin_level
		self.ancient_options['17'] = leave
		return self.ancient_options

	def list_options(self):
		selection = int(input(self.ancient_options.get("0")))
		print(selection)
		self.ancient_options["{}".format(selection)]()


class Vengeance(Paladin):
	def __init__(self):
		self.avenging_angel = False
		self.vengeance_options = {}
		super().__init__()

	def use_avenging_angel(self):
		if not self.avenging_angel:
			print("Used Avenging Angel")
			self.avenging_angel = True
		else:
			print("Already used Avenging Angel")

	def reset_avenging_angel(self):
		if self.avenging_angel:
			print("Reset Avenging Angel")
			self.avenging_angel = False
		else:
			print("Avenging Angel is still usable")

	def create_vengeance_options(self):
		self.vengeance_options['0'] = "[14]: Use Avenging Angel\n" + "[15]: Reset Avenging Angel\n" + \
					"[16]: Change Level\n" + "[17]: Exit\n"
		self.vengeance_options['14'] = self.use_avenging_angel
		self.vengeance_options['15'] = self.reset_avenging_angel
		self.vengeance_options['16'] = self.change_paladin_level
		self.vengeance_options['17'] = leave
		return self.vengeance_options

	def list_options(self):
		selection = int(input(self.vengeance_options.get("0")))
		print(selection)
		self.vengeance_options["{}".format(selection)]()


def merge_base_paladin_dicts(player):
	merge_dicts(player.merge_player_and_half(), player.create_paladin_options())
	return player.paladin_options


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_paladin(name):
	player = create(name, Devotion)
	player.change_paladin_level()
	merge_base_paladin_dicts(player)
	return player


def create_ancients_paladin(name):
	player = create(name, Ancient)
	player.change_paladin_level()
	merge_dicts(merge_base_paladin_dicts(player), player.create_ancients_options())
	return player


def create_devotion_paladin(name):
	player = create(name, Devotion)
	player.change_paladin_level()
	merge_dicts(merge_base_paladin_dicts(player), player.create_devotion_options())
	return player


def create_vengeance_paladin(name):
	player = create(name, Vengeance)
	player.change_paladin_level()
	merge_dicts(merge_base_paladin_dicts(player), player.create_vengeance_options())
	return player


def main_paladin_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Devotion":
		p1 = create_devotion_paladin(name)
		class_options = Devotion.list_options
	elif player_subclass == "Ancient":
		p1 = create_ancients_paladin(name)
		class_options = Ancient.list_options
	elif player_subclass == "Vengeance":
		p1 = create_vengeance_paladin(name)
		class_options = Vengeance.list_options
	else:
		p1 = create_paladin(name)
		class_options = Paladin.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "options": class_options}
