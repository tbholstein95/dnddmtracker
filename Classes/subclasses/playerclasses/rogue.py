from Classes.playercharacter import *
from Classes.subclasses.half_caster import *
rogue_dict = {}

class Rogue(PlayerCharacter):

	def __init__(self):
		self.stroke_of_luck = False
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

	def list_rogue_options(self):
		selection = int(input("What action are you counting?\n" + "[1]: Use Stroke of Luck" +
				      "[2]: Reset Stroke of Luck" + "[3]: Use Hit Dice" + "[4]: Reset Hit Dice" + "[5]: Change Level" + "[6]: Exit"))

		if selection == 1:
			self.use_stroke_of_luck()
		if selection == 2:
			self.reset_stroke_of_luck()
		if selection == 3:
			self.use_hit_dice()
		if selection == 4:
			self.reset_current_hit_dice()
		if selection == 5:
			self.set_level()
			self.set_hit_dice(self.get_level())
		if selection == 6:
			print("Leaving")
			return

	def create_rogue(self, name):
		name = name
		level = int(input("What level is this Rogue?\n"))
		player = Arcane()
		player.set_level()
		player.set_hit_dice(level)
		player.set_name(name)
		player.set_max_spell_slots(level)
		player.set_current_spell_slots(level)

		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Hit Dice:', player.get_hit_dice())

		return player


#TODO Make sure this multiple inheritance is correct
class Arcane(Rogue, HalfCaster):
	def __init__(self):
		self.spell_thief = False
		Rogue.__init__(self)
		HalfCaster.__init__(self)

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

	def list_arcane_options(self):
		selection = int(input("What action are you counting?\n" + "[1]: Use Spell Slot" + "[2]: Use Stroke of Luck" +
				      "[3]: Reset Stroke of Luck" + "[4]: Use Spell Thief + [5]: Reset Spell Thief" +
				      "[6]: Use Hit Dice" + "[7]: Reset Hit Dice" + "[8]: Change Level" + "[9]: Exit"))

		if selection == 1:
			self.use_cur_spell_slot()
		if selection == 2:
			self.use_stroke_of_luck()
		if selection == 3:
			self.reset_stroke_of_luck()
		if selection == 4:
			self.use_spell_thief()
		if selection == 5:
			self.reset_spell_thief()
		if selection == 6:
			self.use_hit_dice()
		if selection == 7:
			self.reset_current_hit_dice()
		if selection == 8:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_spell_slots(self.get_level())
			self.set_current_spell_slots(self.get_level())

		if selection == 9:
			print("Leaving")
			return

	def create_arcane_rogue(self, name):
		name = name
		level = int(input("What level is this Rogue?\n"))
		player = Arcane()
		player.set_level()
		player.set_hit_dice(level)
		player.set_name(name)
		player.set_max_spell_slots(level)
		player.set_current_spell_slots(level)

		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Hit Dice:', player.get_hit_dice())

		return player

def main_rogue_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Arcane":
		p1 = Arcane()
		p1 = p1.create_arcane_rogue(name)
		class_options = Arcane.list_arcane_options
	else:
		p1 = Rogue()
		p1 = p1.create_rogue(name)
		class_options = Rogue.list_rogue_options

	rogue_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}