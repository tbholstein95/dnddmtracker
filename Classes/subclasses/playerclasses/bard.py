from Classes.subclasses.full_caster import *
bard_dict = {}


class Bard(FullCaster):

	def __init__(self):
		self.charisma = 0
		self.counter_charm = False
		self.max_bardic_inspiration = 0
		self.current_bardic_inspiration = 0
		self.default_bard_options = {}
		self.new_options = {}
		super().__init__()

	def get_max_bardic_inspiration(self):
		return self.max_bardic_inspiration

	def get_current_bardic_inspiration(self):
		return self.current_bardic_inspiration

	def get_charisma(self):
		return self.charisma

	def set_charisma(self):
		self.charisma = int(input("What should this Bard's charisma be?"))

	def set_max_bardic_inspiration(self):
		cur_charisma = self.get_charisma()
		if cur_charisma < 1:
			cur_charisma = 1
		self.max_bardic_inspiration = cur_charisma

	def set_cur_bardic_inspiration(self, amount):
		self.current_bardic_inspiration = amount

	def reset_bardic_inspiration(self):
		self.current_bardic_inspiration = self.get_max_bardic_inspiration()
		print("Reset Bardic Inspiration")

	def use_bardic_inspiration(self):
		if self.check_bardic_inspiration():
			self.current_bardic_inspiration -= 1
			print("Used Bardic Inspiration!")
		else:
			print("Out of Bardic Inspiration")

	def check_bardic_inspiration(self):
		if self.get_current_bardic_inspiration() == 0:
			return False
		else:
			return True

	def charisma_option(self):
		self.set_charisma()
		self.set_max_bardic_inspiration()
		self.set_cur_bardic_inspiration(self.get_charisma)

	def change_level_option(self):
		self.base_change_level()
		self.charisma_option()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()

	def create_default_bard_options(self):
		# Default player and spell caster take up 0-4.
		self.default_bard_options['0'] = "[5]: Use Bardic Inspiration\n" + "[6]: Reset Bardic Inspiration\n" + \
							"[7]: Change Charisma\n"
		self.default_bard_options['5'] = self.use_bardic_inspiration
		self.default_bard_options['6'] = self.reset_bardic_inspiration
		self.default_bard_options['7'] = self.charisma_option
		return self.default_bard_options

	def list_options(self):
		selection = int(input(self.default_bard_options.get("0")))
		print(selection)
		self.default_bard_options["{}".format(selection)]()


class Glamour(Bard):

	def __init__(self):
		self.enthralling_performance = False
		self.mantle_of_majesty = False
		self.unbreakable_majesty = False
		self.glamour_options = {}
		super().__init__()

	def use_of_enthralling_performance(self):
		self.enthralling_performance = True
		self.use_bardic_inspiration()
		print("Used Enthralling Performance")

	def use_enthralling_performance(self):
		cur_bardic_inspo = self.get_current_bardic_inspiration()
		if cur_bardic_inspo < 1:
			print("Player does not have enough Bardic Inspiration to perform this action")
		else:
			self.use_of_enthralling_performance()

	def reset_enthralling_performance(self):
		self.enthralling_performance = False
		print("Reset Enthralling Performance")

	def use_mantle_of_majesty(self):
		if not self.mantle_of_majesty:
			self.mantle_of_majesty = True
			print("Used Mantle of Majesty")
		else:
			print("Mantle of Majesty already active")

	def reset_mantle_of_majesty(self):
		self.mantle_of_majesty = False
		print("Mantle of Majesty reset")

	def use_unbreakable_majesty(self):
		if not self.unbreakable_majesty:
			self.unbreakable_majesty = True
			print("Used Unbreakable Majesty")
		else:
			print("Unbreakable Majesty already active")

	def reset_unbreakable_majesty(self):
		self.unbreakable_majesty = False
		print("Reset Unbreakable Majesty")

	def create_glamour_options(self):
		self.glamour_options['0'] = "[8]: Use Enthralling Performance\n" + "[9]: Reset Enthralling Performance" + \
						"[10]: Use Mantle of Majesty\n" + "[11]: Reset Mantle of Majesty\n" + \
						"[12]: Use Unbreakable Majesty\n" + "[13]: Reset Unbreakable Majesty\n" + \
						"[14]: Change Level\n" + "[15]: Exit\n"

		self.glamour_options['8'] = self.use_enthralling_performance
		self.glamour_options['9'] = self.reset_enthralling_performance
		self.glamour_options['10'] = self.use_mantle_of_majesty
		self.glamour_options['11'] = self.reset_mantle_of_majesty
		self.glamour_options['12'] = self.use_unbreakable_majesty
		self.glamour_options['13'] = self.reset_unbreakable_majesty
		self.glamour_options['14'] = self.change_level_option
		self.glamour_options['15'] = leave
		return self.glamour_options

	def list_options(self):
		selection = int(input(self.glamour_options.get("0")))
		print(selection)
		self.glamour_options["{}".format(selection)]()


class Swords(Bard):
	def __init__(self):
		self.blade_flourish = False
		self.sword_options = {}
		super().__init__()

	def get_blade_flourish(self):
		return self.blade_flourish

	def use_blade_flourish(self):
		available = self.get_blade_flourish()
		if not available:
			self.blade_flourish = True
			print("Used Blade Flourish!")
		else:
			print("Blade Flourish already used this turn")

	def reset_blade_flourish(self):
		self.blade_flourish = False

	def create_swords_options(self):
		self.sword_options['0'] = "[8]: Use Blade Flourish\n" + "[9]: Reset Blade Flourish\n" + "[10]: Change Level\n" + \
						"[11]: Exit\n"
		self.sword_options['8'] = self.use_blade_flourish
		self.sword_options['9'] = self.reset_blade_flourish
		self.sword_options['10'] = self.change_level_option
		self.sword_options['11'] = leave
		return self.sword_options

	def list_options(self):
		selection = int(input(self.sword_options.get("0")))
		print(selection)
		self.sword_options["{}".format(selection)]()


class Whispers(Bard):
	def __init__(self):
		self.psychic_blades = False
		self.words_of_terror = False
		self.mantle_of_whispers = False
		self.shadow_lore = False
		self.whispers_options = {}
		super().__init__()

	def get_psychic_blades(self):
		return self.psychic_blades

	def get_words_of_terror(self):
		return self.words_of_terror

	def get_mantle_of_whispers(self):
		return self.mantle_of_whispers

	def get_shadow_lore(self):
		return self.shadow_lore

	def set_psychic_blades(self, truefalse):
		self.psychic_blades = truefalse

	def use_psychic_blades(self):
		if self.get_current_bardic_inspiration() == 0:
			print("Not enough Bardic Inspiration")
			return
		elif self.get_psychic_blades:
			print("Already used Psychic Blades")
			return
		else:
			self.set_psychic_blades(True)
			self.use_bardic_inspiration()
			print("Used Psychic Blades. Cannot use again until next turn.")

	def reset_psychic_blades(self):
		self.set_psychic_blades(False)

	def set_words_of_terror(self, truefalse):
		self.words_of_terror = truefalse

	def use_words_of_terror(self):
		if self.get_words_of_terror():
			print("Already used Words of Terror this awake cycle")
			return
		else:
			self.words_of_terror = True

	def reset_words_of_terror(self):
		self.set_words_of_terror(False)

	def set_mantle_of_whispers(self, truefalse):
		self.mantle_of_whispers = truefalse

	def use_mantle_of_whispers(self):
		if self.get_mantle_of_whispers():
			print("Already used this Awake cycle")
			return
		elif self.get_current_bardic_inspiration() == 0:
			print("Not enough Bardic Inspriation left")
			return
		else:
			self.set_mantle_of_whispers(True)

	def reset_mantle_of_whispers(self):
		self.set_mantle_of_whispers(False)

	def set_shadow_lore(self, truefalse):
		self.shadow_lore = truefalse

	def use_shadow_lore(self):
		if self.get_shadow_lore():
			print("Already used Shadow Lore this Awake Cycle")
			return
		if not self.check_bardic_inspiration():
			print("Not enough Bardic Inspiration to use Shadow Lore")
		else:
			self.set_shadow_lore(True)

	def reset_shadow_lore(self):
		self.set_shadow_lore(False)

	def create_whispers_options(self):
		self.whispers_options['0'] = "[8]: Use Psychic Blades\n" + "[9]: Reset Psychic Blades\n" + \
					"[10]: Use Words of Terror\n" + "[11]: Reset Words of Terror\n" + \
					"[12]: Use Mantle of Whispers\n" + "[13]: Reset Mantle of Whispers\n" + \
					"[14]: Use Shadow Lore\n" + "[15]: Reset Shadow Lore\n" + "[16]: Change Level\n" + \
					"[17]: Exit\n"

		self.whispers_options['8'] = self.use_psychic_blades
		self.whispers_options['9'] = self.reset_psychic_blades
		self.whispers_options['10'] = self.use_words_of_terror
		self.whispers_options['11'] = self.reset_words_of_terror
		self.whispers_options['12'] = self.use_mantle_of_whispers
		self.whispers_options['13'] = self.reset_mantle_of_whispers
		self.whispers_options['14'] = self.use_shadow_lore
		self.whispers_options['15'] = self.reset_shadow_lore
		self.whispers_options['16'] = self.change_level_option
		self.whispers_options['17'] = leave
		return self.whispers_options

	def list_options(self):
		selection = int(input(self.whispers_options.get("0")))
		print(selection)
		self.whispers_options["{}".format(selection)]()


def merge_base_bard_dicts(player):
	bard_opts = player.create_default_bard_options()
	merge_dicts(player.merge_base_and_fullspell_options(), bard_opts)
	return bard_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_bard(name):
	player = create(name, Bard)
	player.change_level_option()
	merge_base_bard_dicts(player)
	return player


def create_glamour_bard(name):
	player = create(name, Glamour)
	player.change_level_option()
	merge_dicts(merge_base_bard_dicts(player), player.create_glamour_options())
	return player


def create_swords_bard(name):
	player = create(name, Swords)
	player.change_level_option()
	merge_dicts(merge_base_bard_dicts(player), player.create_swords_options())
	return player


def create_whispers_bard(name):
	player = create(name, Whispers)
	player.change_level_option()
	merge_dicts(merge_base_bard_dicts(player), player.create_swords_options())
	return player


def main_bard_making(name, dictionary):
	player_subclass = input("What is their subclass?").capitalize()
	if player_subclass == "Glamour":
		p1 = create_glamour_bard(name)
		new_options = Glamour.list_options
	elif player_subclass == "Swords":
		p1 = create_swords_bard(name)
		new_options = Swords.list_options
	elif player_subclass == "Whispers":
		p1 = create_whispers_bard(name)
		new_options = Whispers.list_options
	else:
		p1 = create_bard(name)
		new_options = Bard.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}

	print("Name:" + p1.get_name(), "Level:", + p1.get_level(), "Bardic Inspiration:", (
		p1.get_current_bardic_inspiration(), "Charisma:", + p1.get_charisma()))
