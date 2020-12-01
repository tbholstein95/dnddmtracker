from Classes.subclasses.full_caster import *
import math

druid_dict = {}


class Druid(FullCaster):
	def __init__(self):
		self.max_wild_shape = 2
		self.current_wild_shape = 0
		self.default_druid_options = {}
		super().__init__()

	def get_max_wild_shape(self):
		return self.max_wild_shape

	def get_current_wild_shape(self):
		return self.current_wild_shape

	def set_max_wild_shape(self):
		if self.get_level() < 20:
			self.max_wild_shape = 2
		else:
			self.max_wild_shape = float('inf')

	def set_current_wild_shape(self):
		self.current_wild_shape = self.get_max_wild_shape()

	def use_wild_shape(self):
		if self.get_current_wild_shape() == 0:
			print("Cannot Wild Shape anymore til Long Rest")
			return
		else:
			self.current_wild_shape -= 1

	def create_druid_options(self):
		self.default_druid_options['0'] = "[5]: Use Wildshape\n" + "[6]: Reset Wildshape\n"
		self.default_druid_options['5'] = self.use_wild_shape
		self.default_druid_options['6'] = self.set_current_wild_shape
		return self.default_druid_options

	def change_druid_level(self):
		self.set_level()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()
		self.set_max_hit_dice(self.get_level())
		self.set_hit_dice(self.get_level())

	def list_druid_options(self):
		selection = int(input(self.default_druid_options.get("0")))
		print(selection)
		self.default_druid_options["{}".format(selection)]()


class Land(Druid):
	def __init__(self):
		self.natural_recovery = False
		self.land_options = {}
		super().__init__()

	def get_natural_recovery(self):
		return self.natural_recovery

	def set_natural_recovery(self, truefalse):
		self.natural_recovery = truefalse

	def use_natural_recovery(self):
		if self.get_natural_recovery():
			print("Already used Natural Recovery this long rest")
			return
		else:
			cur_level = self.get_level()
			restore_up_to = math.ceil(cur_level // 2)
			temp_restore_up_to = restore_up_to
			print(f"Player can restore up to {restore_up_to} combined spell slot levels")
			while temp_restore_up_to > 0:
				restoring = int(input("What level spell is player recovering? Type '0' to stop early"))
				if restoring > restore_up_to or restoring >= 6:
					print("Spell slot too great")
				if restoring == 0:
					return
				else:
					quant_restoring = int(input("How many of these spell slots?"))
					if quant_restoring * restoring > restore_up_to or quant_restoring * restoring > \
						self.max_slots[restoring]:
						print("This is too many")
					else:
						self.current_slots[restoring] += quant_restoring
			self.set_natural_recovery(True)

	def reset_natural_recovery(self):
		self.natural_recovery = False

	def change_land_level(self):
		self.set_level()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()
		self.set_max_hit_dice(self.get_level())
		self.reset_current_hit_dice()

	def create_land_options(self):
		self.land_options['0'] = "[5]: Use Natural Recovery\n" + "[6]: Reset Natural Recovery\n" + \
					"[7]: Change Level\n" + "[8]: Exit\n"
		self.land_options['5'] = self.use_natural_recovery
		self.land_options['6'] = self.reset_natural_recovery
		self.land_options['7'] = self.change_land_level
		self.land_options['8'] = leave
		return self.land_options

	def list_options(self):
		selection = int(input(self.land_options.get("0")))
		print(selection)
		self.land_options["{}".format(selection)]()


class Moon(Druid):
	def __init__(self):
		self.moon_options = {}
		super().__init__()

	def use_combat_wildshape_heal(self):
		to_use = int(input("What level spell slot is the player using?"))
		current_slot = self.get_current_spell_slot(to_use)
		if current_slot == 0:
			print("No remaining slots of this level")
		else:
			self.use_cur_spell_slot()
			print("Used a spell slot to heal")

	def create_moon_options(self):
		self.moon_options['0'] = "[5]: Use Combat WildShape Heal\n" + "[6]: Change Level\n" + "[7]: Exit\n"
		self.moon_options['5'] = self.use_combat_wildshape_heal
		self.moon_options['6'] = self.change_druid_level
		self.moon_options['7'] = leave
		return self.moon_options

	def list_options(self):
		selection = int(input(self.moon_options.get("0")))
		print(selection)
		self.moon_options["{}".format(selection)]()


class Dream(Druid):
	def __init__(self):
		self.max_summer_court_dice = 0
		self.cur_summer_court_dice = 0
		self.wisdom = 0
		self.max_hidden_paths = 0
		self.current_hidden_paths = 0
		self.walker_in_dreams = False
		self.dream_options = {}
		super().__init__()

	def set_wisdom(self):
		amount = int(input("What is this Druid's wisdom modifier?"))
		self.wisdom = amount

	def set_max_summer_court_dice(self):
		amount = self.get_level
		self.max_summer_court_dice = amount

	def set_max_hidden_paths(self):
		amount = self.get_wisdom
		self.max_hidden_paths = amount

	def set_current_summer_court_dice(self):
		amount = self.get_max_summer_court_dice()
		self.current_hidden_paths = amount

	def use_current_summer_court_dice(self, amount):
		self.cur_summer_court_dice -= amount

	def set_current_hidden_paths(self):
		amount = self.get_max_hidden_paths
		self.current_hidden_paths = amount

	def get_wisdom(self):
		return self.wisdom

	def get_max_summer_court_dice(self):
		return self.max_summer_court_dice

	def get_max_hidden_paths(self):
		return self.max_hidden_paths

	def get_current_summer_court_dice(self):
		return self.cur_summer_court_dice

	def get_current_hidden_paths(self):
		return self.current_hidden_paths

	def use_summer_court(self):
		cur_amount = self.get_current_summer_court_dice()
		if cur_amount == 0:
			print("No more dice to spend")
			return
		else:
			amount_to_use = int(input(f"Player can use {self.get_current_summer_court_dice()}" + (

				"Summer Court Dice. How many dice did they use?")))
			self.use_current_summer_court_dice(amount_to_use)

	def use_hidden_paths(self):
		cur_amount = self.get_current_hidden_paths()
		if cur_amount == 0:
			print("Not available to use until after Long Rest")
			return
		else:
			self.current_hidden_paths -= 1

	def change_dream_level(self):
		self.set_level()
		self.set_wisdom()
		self.set_max_hidden_paths()
		self.set_max_summer_court_dice()
		self.set_current_hidden_paths()
		self.set_current_summer_court_dice()
		self.set_max_hidden_paths()
		self.set_current_hidden_paths()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()
		self.set_max_hit_dice(self.get_level())
		self.set_hit_dice(self.get_level())

	def create_dream_options(self):
		self.dream_options['0'] = "[5]: Use Balm of the Summer Court\n" + "[6]: Reset Balm of the Summer court\n" + \
					"[7]: Use Hidden Paths\n" + "[8]: Reset Hidden Paths" + "[9]: Change Level\n" + \
					"[10]: Exit\n"

		self.dream_options['5'] = self.use_summer_court
		self.dream_options['6'] = self.set_current_summer_court_dice
		self.dream_options['7'] = self.use_hidden_paths
		self.dream_options['8'] = self.set_current_hidden_paths
		self.dream_options['9'] = self.change_dream_level
		self.dream_options['10'] = leave
		return self.dream_options

	def list_options(self):
		selection = int(input(self.dream_options.get("0")))
		print(selection)
		self.dream_options["{}".format(selection)]()


class Shepherd(Druid):
	def __init__(self):
		self.spirit_totem = False
		self.faithful_summons = False
		self.shepherd_options = {}
		super().__init__()

	def get_spirit_totem(self):
		return self.spirit_totem

	def get_faithful_summons(self):
		return self.faithful_summons

	def set_spirit_totem(self, truefalse):
		self.spirit_totem = truefalse

	def reset_spirit_totem(self):
		self.set_spirit_totem(False)

	def set_faithful_summons(self, truefalse):
		self.faithful_summons = truefalse

	def use_spirit_totem(self):
		if self.get_spirit_totem:
			print("Already used this Short/Long Rest")
			return
		else:
			print("Used Spirit Totem")
			self.set_spirit_totem(True)

	def use_faithful_summons(self):
		current_faithful = self.get_faithful_summons()
		if current_faithful:
			print("Already used Faithful Summons this Long Rest")
			return
		else:
			print("Used Faithful Summons")
			self.set_faithful_summons(True)

	def reset_faithful_summons(self):
		self.set_faithful_summons(False)

	def create_shepherd_options(self):
		self.shepherd_options['0'] = "[5]: Use Spirit Totem\n" + "[6]: Reset Spirit Totem\n" + "[7]: Use Faithful Summons\n" \
					+ "[8]: Reset Faithful Summons\n" + "[9]: Change Level\n" + "[10]: Exit\n"

		self.shepherd_options['5'] = self.use_spirit_totem
		self.shepherd_options['6'] = self.reset_spirit_totem
		self.shepherd_options['7'] = self.use_faithful_summons
		self.shepherd_options['8'] = self.reset_faithful_summons
		self.shepherd_options['9'] = self.change_druid_level
		self.shepherd_options['10'] = leave
		return self.shepherd_options

	def list_options(self):
		selection = int(input(self.shepherd_options.get("0")))
		print(selection)
		self.shepherd_options["{}".format(selection)]()


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_druid(name):
	player = create(name, Druid)
	player.change_druid_level()
	default_player_opts = player.create_player_character_options()
	default_spell_opts = player.create_fullcaster_character_options()
	druid_opts = player.create_druid_options()
	merge_dicts(default_player_opts, default_spell_opts)
	merge_dicts(default_spell_opts, druid_opts)
	return player


def create_dream_druid(name):
	player = create(name, Dream)
	player.change_dream_level()
	player.create_dream_options()
	default_player_opts = player.create_player_character_options()
	default_spell_opts = player.create_fullcaster_character_options()
	druid_opts = player.create_druid_options()
	merge_dicts(default_player_opts, default_spell_opts)
	merge_dicts(default_spell_opts, druid_opts)
	merge_dicts(druid_opts, player.dream_options)
	return player


def create_shepherd_druid(name):

	player = create(name, Shepherd)
	player.change_druid_level()
	player.create_shepherd_options()
	default_player_opts = player.create_player_character_options()
	default_spell_opts = player.create_fullcaster_character_options()
	druid_opts = player.create_druid_options()
	merge_dicts(default_player_opts, default_spell_opts)
	merge_dicts(default_spell_opts, druid_opts)
	merge_dicts(druid_opts, player.shepherd_options)
	return player


def create_land_druid(name):
	player = create(name, Land)
	player.change_land_level()
	player.create_land_options()
	default_player_opts = player.create_player_character_options()
	default_spell_opts = player.create_fullcaster_character_options()
	druid_opts = player.create_druid_options()
	merge_dicts(default_player_opts, default_spell_opts)
	merge_dicts(default_spell_opts, druid_opts)
	merge_dicts(druid_opts, player.land_options)
	return player


def create_moon_druid(name):
	player = create(name, Moon)
	player.change_druid_level()
	player.create_moon_options()
	default_player_opts = player.create_player_character_options()
	default_spell_opts = player.create_fullcaster_character_options()
	druid_opts = player.create_druid_options()
	merge_dicts(default_player_opts, default_spell_opts)
	merge_dicts(default_spell_opts, druid_opts)
	merge_dicts(druid_opts, player.moon_options)
	return player


def main_druid_making(name, dictionary):
	player_subclass = input("What is their subclass?").capitalize()
	if player_subclass == "Land":
		p1 = create_land_druid(name)
		new_options = Land.list_options
	elif player_subclass == "Moon":
		p1 = create_moon_druid(name)
		new_options = Moon.list_options
	elif player_subclass == "Dream":
		p1 = create_dream_druid(name)
		new_options = Dream.list_options
	elif player_subclass == "Shepherd":
		p1 = create_shepherd_druid(name)
		new_options = Shepherd.list_options
	else:
		p1 = create_druid(name)
		new_options = Druid.list_druid_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}
