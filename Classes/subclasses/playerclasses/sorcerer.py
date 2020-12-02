from Classes.subclasses.full_caster import *
sorcerer_dict = {}


class Sorcerer(FullCaster):

	def __init__(self):
		self.max_sorcery_points = 0
		self.current_sorcery_points = 0
		self.sorcerer_options = {}
		super().__init__()

	def set_max_sorcery_points(self, level):
		if level > 1:
			self.max_sorcery_points = level

	def get_max_sorcery_points(self):
		return self.max_sorcery_points

	def set_current_sorcery_points(self, amount):
		self.current_sorcery_points = amount

	def get_current_sorcery_points(self):
		return self.current_sorcery_points

	def reset_current_sorcery_points(self):
		amount = self.get_max_hit_dice()
		self.set_current_sorcery_points(amount)

	def add_sorcery_points(self, amount):
		current = self.get_current_sorcery_points()
		self.set_current_sorcery_points(current + amount)

	def use_sorcery_point(self, amount):
		current_sp = self.get_current_sorcery_points()
		if current_sp >= amount:
			self.set_current_sorcery_points(current_sp-amount)
		else:
			print("Sorcerer does not have that many sorcery points right now")

	def create_spell_slot(self):
		slot = int(input("What spell slot does the sorcerer want?"))
		point_cost = 0
		if slot == 1:
			point_cost = 2
		elif slot == 2:
			point_cost = 3
		elif slot == 3:
			point_cost = 5
		elif slot == 4:
			point_cost = 6
		elif slot == 5:
			point_cost = 7
		current_sp = self.get_current_sorcery_points()
		if point_cost > current_sp:
			print("Sorcerer only has {} sorcery points.".format(current_sp))
		if current_sp >= point_cost:
			self.use_sorcery_point(point_cost)
			self.add_spell_slot(slot)
			print("Added one slot to level {} spells.".format(slot))

	def create_sorcery_points(self):
		points = int(input("What level spell is the Sorcerer spending for this?"))
		slots = self.get_current_spell_slot(points)
		if slots >= 0:
			self.add_sorcery_points(points)
		else:
			print("Sorcerer doesn't have any remaining {} slots to spend".format(points))

	def use_careful_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")

	def use_distant_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")

	def use_empowered_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")

	def use_extended_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")

	def use_heightened_spell(self):
		self.use_sorcery_point(3)
		print("Spent 3 sorcery points")

	def use_quickened_spell(self):
		self.use_sorcery_point(2)
		print("Spent two sorcery point")

	def use_subtle_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")

	def use_twinned_spell(self):
		spell_level = int(input("What is the spell level?"))
		if self.get_current_spell_slot(spell_level) > 0:
			self.use_sorcery_point(spell_level)
			print("Spend {} sorcery point(s)".format(spell_level))
		else:
			print("No spell slots left for that level")

	def use_sorcerous_restoration(self):
		self.add_sorcery_points(4)

	def create_sorcerer_options(self):
		self.sorcerer_options['0'] = "[5]: Create Spell Slot\n" + "[6]: Create Sorcery Point\n" + \
					"[7]: Use Careful Spell\n" + "[8]: Use Distant Spell\n" + "[9]: Use Empowered Spell \n" + \
					"[10]: Use Extended Spell\n" + "[11]: Use Heightened Spell\n" + "[12]: Use Quickened Spell\n" + \
					"[13]Use Subtle Spell\n" + "[14]: Use Twinned Spell\n" + "[15]: Use Sorcerous Restoration\n"

		self.sorcerer_options['5'] = self.create_spell_slot
		self.sorcerer_options['6'] = self.create_sorcery_points
		self.sorcerer_options['7'] = self.use_careful_spell
		self.sorcerer_options['8'] = self.use_distant_spell
		self.sorcerer_options['9'] = self.use_empowered_spell
		self.sorcerer_options['10'] = self.use_extended_spell
		self.sorcerer_options['11'] = self.use_heightened_spell
		self.sorcerer_options['12'] = self.use_quickened_spell
		self.sorcerer_options['13'] = self.use_subtle_spell
		self.sorcerer_options['14'] = self.use_twinned_spell
		self.sorcerer_options['15'] = self.use_sorcerous_restoration
		return self.sorcerer_options

	def change_sorcerer_level(self):
		self.change_fullcaster_level()
		self.set_max_sorcery_points(self.get_level())
		self.reset_current_sorcery_points()

	def list_options(self):
		selection = int(input(self.sorcerer_options.get("0")))
		print(selection)
		self.sorcerer_options["{}".format(selection)]()


class Draconic(Sorcerer):
	def __init__(self):
		self.draconic_options = {}
		super().__init__()

	def elemental_affinity_resistance(self):
		if self.level >= 6:
			self.use_sorcery_point(1)
			print("Sorcerer has resistance to whatever spell damage type was for an hour")
		else:
			print("Sorcerer needs to be at least level 6")

	def use_draconic_presence(self):
		if self.level >= 18:
			self.use_sorcery_point(5)
			print("Aura of fear created in 60 feet for 1 minute")
		else:
			print("Sorcerer needs to be level 18 first")

	def create_draconic_options(self):
		self.draconic_options['0'] = "[16]: Use Elemental Affinity\n" + "[17]: Use Dragonic Presence\n" + \
					"[18]: Change Level\n" + "[19]: Exit\n"
		self.draconic_options['16'] = self.elemental_affinity_resistance
		self.draconic_options['17'] = self.use_draconic_presence
		self.draconic_options['18'] = self.change_sorcerer_level
		self.draconic_options['19'] = leave
		return self.draconic_options

	def list_options(self):
		selection = int(input(self.draconic_options.get("0")))
		print(selection)
		self.draconic_options["{}".format(selection)]()


class WildMagic(Sorcerer):
	def __init__(self):
		self.tides_of_chaos = False
		self.wildmagic_options = {}
		super().__init__()

	def use_tides_of_chaos(self):
		self.use_sorcery_point(1)
		if not self.tides_of_chaos:
			self.tides_of_chaos = True
		else:
			print("Tides of Chaos on cooldown")

	def reset_tides_of_chaos_rest(self):
		self.tides_of_chaos = False

	def reset_tides_of_chaos_roll(self):
		self.tides_of_chaos = False

	def use_bend_luck(self):
		self.use_sorcery_point(2)
		print("Used bend luck")

	def create_wild_magic_options(self):
		self.wildmagic_options['0'] = "[14]: Use Bend Luck\n" + "[15]: Use Tides of Chaos\n" + \
					"[16]: Reset Tides of Chaos (Rest)\n" + "[17]: Reset Tides of Chaos (Roll)\n" + \
					"[19]: Change Level\n" + "[20]: Exit\n"
		self.wildmagic_options['14'] = self.use_bend_luck
		self.wildmagic_options['15'] = self.use_tides_of_chaos
		self.wildmagic_options['16'] = self.reset_tides_of_chaos_rest
		self.wildmagic_options['17'] = self.reset_tides_of_chaos_roll
		self.wildmagic_options['18'] = self.change_sorcerer_level
		self.wildmagic_options['19'] = leave
		return self.wildmagic_options

	def list_options(self):
		selection = int(input(self.wildmagic_options.get("0")))
		print(selection)
		self.wildmagic_options["{}".format(selection)]()


def merge_base_sorcerer_dicts(player):
	sorcerer_opts = player.create_default_sorcerer_options()
	merge_dicts(player.merge_base_and_fullspell_options(), sorcerer_opts)
	return sorcerer_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_basic_sorcerer(name):
	player = create(name, Sorcerer)
	player.change_sorcerer_level()
	merge_dicts(merge_base_sorcerer_dicts(player), player.create_sorcerer_options())
	return player


def create_draconic_sorcerer(name):
	player = create(name, Draconic)
	player.change_sorcerer_level()
	merge_dicts(merge_base_sorcerer_dicts(player), player.create_draconic_options())
	return player


def create_wild_magic_sorcerer(name):
	player = create(name, WildMagic)
	player.change_sorcerer_level()
	merge_dicts(merge_base_sorcerer_dicts(player), player.create_wild_magic_options())
	return player


def main_sorcerer_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Draconic":
		p1 = create_draconic_sorcerer(name)
		class_options = Draconic.list_options
	elif player_subclass == "Wild Magic":
		p1 = create_wild_magic_sorcerer(name)
		class_options = WildMagic.list_options
	else:
		p1 = create_basic_sorcerer(name)
		class_options = Sorcerer.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "options": class_options}


