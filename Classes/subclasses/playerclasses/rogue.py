from Classes.playercharacter import *
from Classes.subclasses.half_caster import *
rogue_dict = {}


class Rogue(PlayerCharacter):

	def __init__(self):
		self.stroke_of_luck = False
		self.rogue_options = {}
		super().__init__()

	def get_stroke_of_luck(self):
		return self.stroke_of_luck

	def use_stroke_of_luck(self):
		if not self.get_stroke_of_luck():
			print("Used Stroke of Luck")
			self.stroke_of_luck = True
		else:
			print("Can't use Stroke of Luck until end of short of long rest")

	def reset_stroke_of_luck(self):
		if self.stroke_of_luck:
			print("Refreshed Stroke of Luck")
			self.stroke_of_luck = False
		else:
			print("Stroke of Luck is still goo to use.")

	def create_rogue_options(self):
		self.rogue_options['0'] = "[3]: Use Stroke of Luck" + "[4]: Reset Stroke of Luck"
		self.rogue_options['3'] = self.use_stroke_of_luck
		self.rogue_options['4'] = self.reset_stroke_of_luck
		return self.rogue_options

	def list_options(self):
		selection = int(input(self.rogue_options.get("0")))
		print(selection)
		self.rogue_options["{}".format(selection)]()


class Arcane(Rogue, HalfCaster):
	def __init__(self):
		self.spell_thief = False
		Rogue.__init__(self)
		HalfCaster.__init__(self)
		self.arcane_options = {}

	def use_spell_thief(self):
		if not self.spell_thief:
			print("Used Spell Thief")
			self.spell_thief = True
		else:
			print("Already used Spell Thief this Long Rest")

	def reset_spell_thief(self):
		if self.spell_thief:
			print("Reset Spell Thief")
			self.spell_thief = False
		else:
			print("Spell Thief is still good to use.")

	def create_arcane_options(self):
		self.arcane_options['0'] = "[5]: Use Spell Thief + [6]: Reset Spell Thief" + "[7]: Change Level" + "[8]: Exit"
		self.arcane_options['5'] = self.use_spell_thief
		self.arcane_options['6'] = self.reset_spell_thief
		self.arcane_options['7'] = self.change_half_caster_level
		self.arcane_options['8'] = leave
		return self.arcane_options


def merge_base_fighter_dicts(player):
	player_class = player.create_player_character_options()
	rogue_opts = player.create_fighter_options()
	merge_dicts(player_class, rogue_opts)
	return rogue_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_rogue(name):
	player = create(name, Rogue)
	player.base_change_level()
	merge_dicts(player.create_player_character_options(), player.create_rogue_options())
	return player


def create_arcane_rogue(name):
	player = create(name, Arcane)
	player.change_half_caster_level()
	merge_dicts(merge_base_fighter_dicts(player), player.create_arcane_options())
	return player


def main_rogue_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Arcane":
		p1 = create(name, Arcane)
		class_options = Arcane.list_options
	else:
		p1 = create(name, Rogue)
		class_options = Rogue.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "options": class_options}
