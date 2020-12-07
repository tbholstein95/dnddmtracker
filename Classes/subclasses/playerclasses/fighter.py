
from Classes.subclasses.half_caster import *
fighter_dict = {}


class Fighter(PlayerCharacter):
	def __init__(self):
		self.second_wind = False
		self.action_surge = False
		self.max_indomitable = 0
		self.current_indomitable = 0
		self.fighter_options = {}
		super().__init__()

	def set_second_wind(self, truefalse):
		self.second_wind = truefalse

	def set_action_surge(self, truefalse):
		self.action_surge = truefalse

	def reset_action_surge(self):
		self.set_action_surge(False)

	def set_max_indomitable(self):
		level = self.get_level()
		if level >= 9:
			self.max_indomitable = 1
		elif level >= 13:
			self.max_indomitable = 2
		elif level >= 17:
			self.max_indomitable = 3

	def set_current_indomitable(self):
		amount = self.get_max_indomitable()
		self.current_indomitable = amount

	def use_current_indomitable(self):
		self.current_indomitable -= 1

	def get_second_wind(self):
		return self.second_wind

	def get_action_surge(self):
		return self.action_surge

	def get_max_indomitable(self):
		return self.max_indomitable

	def get_current_indomitable(self):
		return self.current_indomitable

	def use_indomitable(self):
		current = self.get_current_indomitable()
		if current == 0:
			print("Out of uses until the next Long Rest")
			return
		else:
			self.use_current_indomitable()

	def use_second_wind(self):
		if self.get_second_wind():
			print("Cannot use Second Wind until short or long rest")
			return
		else:
			print("Used Second Wind")
			self.set_second_wind(True)

	def reset_second_wind(self):
		self.set_second_wind(False)

	def use_action_surge(self):
		if self.get_action_surge():
			print("Cannot use Action Surge until short or long rest")
			return
		else:
			print("Used Action Surge")
			self.set_action_surge(True)

	def create_fighter_options(self):
		self.fighter_options['0'] = "[3]: Use Second Wind\n" + "[4]: Reset Second Wind\n " + "[5]: Use Action Surge\n " + \
					"[6]: Reset Action Surge\n" + "[7]: Use Indomitable\n" + "[8]: Reset Indomitable\n"
		self.fighter_options['3'] = self.use_second_wind
		self.fighter_options['4'] = self.reset_second_wind
		self.fighter_options['5'] = self.use_action_surge
		self.fighter_options['6'] = self.reset_action_surge
		self.fighter_options['7'] = self.use_indomitable
		self.fighter_options['8'] = self.set_current_indomitable
		return self.fighter_options

	def change_fighter_level(self):
		self.base_change_level()
		self.set_max_indomitable()
		self.set_current_indomitable()

	def list_options(self):
		selection = int_checker(self.fighter_options.get("0"))
		print(selection)
		self.fighter_options["{}".format(selection)]()


class BattleMaster(Fighter):
	def __init__(self):
		self.max_superiority_dice = 0
		self.current_superiority_dice = 0
		self.battlemaster_options = {}
		super().__init__()

	def set_max_superiority_dice(self):
		level = self.get_level()
		if level < 7:
			self.max_superiority_dice = 4
		elif level >= 7:
			self.max_superiority_dice = 5
		elif level >= 15:
			self.max_superiority_dice = 6

	def set_current_superiority_dice(self):
		amount = self.get_max_superiority_dice()
		self.current_superiority_dice = amount

	def get_max_superiority_dice(self):
		return self.get_max_superiority_dice()

	def get_current_superiority_dice(self):
		return self.current_superiority_dice

	def use_current_superiority_dice(self):
		self.current_superiority_dice -= 1

	def use_superiority_dice(self):
		current_dice = self.get_current_superiority_dice()
		if current_dice == 0:
			print("Not enough Superiority Dice remaining")
			return
		else:
			self.use_current_superiority_dice()

	def change_battlemaster_level(self):
		self.change_fighter_level()
		self.set_max_superiority_dice()
		self.set_current_superiority_dice()

	def create_battlemaster_options(self):
		self.battlemaster_options['0'] = "[9]: Use Superiority Dice \n " + "[10]: Reset Superiority Dice\n" + \
						"[11]: Change Level\n" + "[10]: Exit\n"
		self.battlemaster_options['9'] = self.use_superiority_dice
		self.battlemaster_options['10'] = self.set_current_superiority_dice
		self.battlemaster_options['11'] = self.change_battlemaster_level
		self.battlemaster_options['12'] = leave
		return self.battlemaster_options

	def list_options(self):
		selection = int_checker(self.battlemaster_options.get("0"))
		print(selection)
		self.battlemaster_options["{}".format(selection)]()


class Eldritch(Fighter, HalfCaster):
	def __init__(self):
		HalfCaster.__init__(self)
		Fighter.__init__(self)
		self.eldritch_options = {}

	def change_eldritch_level(self):
		self.change_fighter_level()
		self.set_max_spell_slots(self.get_level())
		self.set_current_spell_slots(self.get_level())

	def create_eldritch_options(self):
		self.eldritch_options['0'] = "[5]: Use Second Wind\n" + "[6]: Reset Second Wind \n " + "[7]: Use Action Surge\n " + \
					"[8]: Reset Action Surge\n" + "[9]: Use Indomitable\n" + "[10]: Reset Indomitable\n" + \
					"[11]: Change Level\n" + "[12]: Exit\n"
		self.eldritch_options['5'] = self.use_second_wind
		self.eldritch_options['6'] = self.reset_second_wind
		self.eldritch_options['7'] = self.use_action_surge
		self.eldritch_options['8'] = self.reset_action_surge
		self.eldritch_options['9'] = self.use_indomitable
		self.eldritch_options['10'] = self.set_current_indomitable
		self.eldritch_options['11'] = self.change_eldritch_level
		self.eldritch_options['12'] = leave

	def list_options(self):
		selection = int_checker(self.eldritch_options.get("0"))
		print(selection)
		self.eldritch_options["{}".format(selection)]()


def merge_base_fighter_dicts(player):
	player_class = player.create_player_character_options()
	fighter_opts = player.create_fighter_options()
	merge_dicts(player_class, fighter_opts)
	return fighter_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_fighter(name):
	player = create(name, Fighter)
	player.change_fighter_level()
	merge_base_fighter_dicts(player)
	return player


def create_battlemaster_fighter(name):
	player = create(name, BattleMaster)
	player.change_battlemaster_level()
	merge_dicts(merge_base_fighter_dicts(player), player.create_battlemaster_options())
	return player


def create_eldritch_fighter(name):
	player = create(name, Eldritch)
	player.change_eldritch_level()
	merge_dicts(player.merge_dicts(player.create_player_character_options(), player.create_halfcaster_character_options()),
		player.create_eldritch_options())
	return player


def main_fighter_making(name, dictionary):
	player_subclass = input("What is their subclass?").capitalize()
	if player_subclass == "BattleMaster":
		p1 = create_battlemaster_fighter(name)
		new_options = BattleMaster.list_options
	elif player_subclass == "Eldritch":
		p1 = create_eldritch_fighter(name)
		new_options = Eldritch.list_options
	else:
		p1 = create_fighter(name)
		new_options = Fighter.list_options

	print('Name:' + p1.get_name(), ' Level:', p1.get_level(), ' Hit Dice:', p1.get_hit_dice())

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}
