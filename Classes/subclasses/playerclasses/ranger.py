from Classes.subclasses.half_caster import *
ranger_dict = {}

class Ranger(HalfCaster):
	def __init__(self):
		HalfCaster.__init__(self)

	def list_ranger_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Hit Dice\n" +

			      "[3]: Reset Hit Dice\n" + "[4]: Change Level\n" + "[5]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.use_hit_dice()
		elif selection == 3:
			self.reset_current_hit_dice()
		elif selection == 4:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_current_spell_slots(self.get_level())
		elif selection == 14:
			print("Leaving")
			return

	def create_ranger(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Ranger()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(level)
		player.set_current_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_current_spell_slot(level))

		return player

def main_ranger_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	p1 = Ranger()
	p1 = p1.create_ranger(name)
	class_options = Ranger.list_ranger_options

	ranger_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}