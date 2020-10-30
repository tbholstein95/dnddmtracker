from Classes.subclasses.full_caster import *
wizard_dict = {}
# TODO : Refresh spell slots
class Wizard(FullCaster):
	def __init__(self):
		self.signature_spells = 2
		FullCaster.__init__(self)

	def list_wizard_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Hit Dice\n" +

			      "[3]: Reset Hit Dice\n" + "[4]: Change Level\n" + "[5]: Exit\n"))

		if selection == 1:
			self.use_spell_slot()
		elif selection == 2:
			self.use_hit_dice()
		elif selection == 3:
			self.reset_current_hit_dice()
		elif selection == 4:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_spell_slots(self.get_level())
		elif selection == 5:
			print("Leaving")
			return

	def create_wizard(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Wizard()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_cur_spell_slot(level))

		return player

class Abjuration(Wizard):
	def __init__(self):
		self.arcane_ward = False
		Wizard.__init__(self)

	def use_arcane_ward(self):
		if not self.arcane_ward:
			self.arcane_ward = True
			print("Used Arcane Ward.  Can't create again until Long Rest")
		else:
			print("Already used Arcane Ward. Wizard needs a long rest first")

	def reset_arcane_ward(self):
		if self.arcane_ward:
			self.arcane_ward = False

	def list_abjuration_options(self):
		selection = int(input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Hit Dice\n" +

		"[3]: Change Level\n" + "[16]: Exit\n"))

		if selection == 1:
			self.use_spell_slot()
		elif selection == 2:
			self.use_hit_dice()
		elif selection == 3:
			self.set_level()
			self.set_hit_dice(self.get_level())
		elif selection == 4:
			print("Leaving")
			return
	def create_abjuration_wizard(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Abjuration()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Slots" + player.get_cur_spell_slot(level))

		return player

class Divination(Wizard):
	def __init__(self):
		self.max_portent = 0
		self.current_portent = 0
		self.third_eye = False
		Wizard.__init__(self)

	def use_expert_divination(self):
		if self.get_level() >= 6:
			spell_level = self.use_spell_slot()
			restore_slot = int(input("WHat spell slot would they like to restore?"))
			if restore_slot < 6 and restore_slot < spell_level:
				self.add_spell_slot(restore_slot)
			else:
				print("Must restore a spell slot less than 6th level and lower than spell level cast")

	def set_max_portent(self):
		if 2 <= self.get_level() <14:
			self.max_portent = 2
		elif 14 <= self.get_level():
			self.max_portent = 3

	def get_current_portent(self):
		return self.current_portent

	def use_portent(self):
		if 0 < self.get_current_portent():
			self.current_portent -= 1
		else:
			print("Not enough portents left")

	def reset_current_portents(self):
		self.current_portent = self.max_portent

	def use_third_eye(self):
		if not self.third_eye:
			self.third_eye = True
		else:
			print("Already used Third Eye. Must long rest")

	def refresh_third_eye(self):
		if self.third_eye:
			self.third_eye = False
		else:
			print("Third Eye is still good to go")

	def list_divination_options(self):
		selection = int(input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Expert Divination\n" +

		"[3]: Use Portent\n" + "[4]: Reset Current Portents\n" + "[5]: Use Hit Dice\n" + "[6]: Reset Hit Dice\n" +

		"[7]: Change Level\n" + "[8]: Exit\n"))

		if selection == 1:
			self.use_spell_slot()
		elif selection == 2:
			self.use_expert_divination()
		elif selection == 3:
			self.use_portent()
		elif selection == 4:
			self.reset_current_portents()
		elif selection == 5:
			self.use_hit_dice()
		elif selection == 6:
			self.reset_current_hit_dice()
		elif selection == 7:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_portent()
			self.set_spell_slots(self.get_level)
		elif selection == 8:
			print("Leaving")
			return

	def create_divination_wizard(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Divination()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_hit_dice(level)
		player.set_max_portent()
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Slots" + player.get_cur_spell_slot(level))

		return player

class Enchantment(Wizard):
	def __init__(self):
		self.hypnotic_gaze = False
		self.instinctive_charm = False
		Wizard.__init__(self)

	def use_hypnotic_gaze(self):
		if not self.hypnotic_gaze:
			self.hypnotic_gaze = True
			print("Used hypnotic gaze")
		else:
			print("Already used Hypnotic Gaze this Long Rest")

	def reset_hypnotic_gaze(self):
		if self.hypnotic_gaze:
			self.hypnotic_gaze = False
			print("Hypnotic Gaze refreshed")
		else:
			print("Hypnotic Gaze is still usable")

	def use_instinctive_charm(self):
		if not self.instinctive_charm:
			print("Used Instinctive Charm")
			self.instinctive_charm = True
		else:
			print("Already used Instinctive Charm this long rest")

	def reset_instinctive_charm(self):
		if self.instinctive_charm:
			print("Refreshed Instinctive Charm")
			self.instinctive_charm = False
		else:
			self.instinctive_charm = True
			print("Instinctive Charm still usable")

	def list_enchantment_options(self):
		selection = int(input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Hypnotic Gaze\n" +

		"[3]: Reset Hypnotic Gaze\n" + "[4]: Use Instinctive Charm\n" + "[5]: Reset Instinctive Charm\n" +

		"[6]: Use Hit Dice\n" + "[7]: Reset Hit Dice\n" + "[8]: Change Level\n" + "[9]: Exit\n"))

		if selection == 1:
			self.use_spell_slot()
		elif selection == 2:
			self.use_hypnotic_gaze()
		elif selection == 3:
			self.reset_hypnotic_gaze()
		elif selection == 4:
			self.use_instinctive_charm()
		elif selection == 5:
			self.reset_instinctive_charm()
		elif selection == 6:
			self.use_hit_dice()
		elif selection == 7:
			self.reset_current_hit_dice()
		elif selection == 8:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_spell_slots(self.get_level())
		elif selection == 8:
			print("Leaving")
			return

	def create_enchantment_wizard(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Enchantment()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Slots" + player.get_cur_spell_slot(level))

		return player

class Illusion(Wizard):
	def __init__(self):
		self.illusory_self = False
		Wizard.__init__(self)

	def use_illusory_self(self):
		if not self.illusory_self:
			print("Used illusory Self")
			self.illusory_self = True
		else:
			print("Wizard needs a short or long rest before casting Illusory Self again.")

	def reset_illusory_set(self):
		if self.illusory_self:
			print("Refreshed illusory self")
			self.illusory_self = False
		else:
			print("Illusory Self is still usable")

	def list_illusion_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Illusory Self\n" +

			      "[3]: Reset Illusory Self\n" + "[4]: Use Hit Dice\n" + "[5]: Reset Hit Dice\n" + "[6]: Change Level\n" + "[7]: Exit\n"))

		if selection == 1:
			self.use_spell_slot()
		elif selection == 2:
			self.use_illusory_self()
		elif selection == 3:
			self.reset_illusory_set()
		elif selection == 4:
			self.use_hit_dice()
		elif selection == 5:
			self.reset_current_hit_dice()
		elif selection == 6:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_spell_slots(self.get_level())
		elif selection == 7:
			print("Leaving")
			return

	def create_illusion_wizard(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Enchantment()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_cur_spell_slot(level))

		return player

class Transmutation(Wizard):
	def __init__(self):
		self.shapechange = False
		self.create_transmuter_stone = False
		Wizard.__init__(self)

	def use_shapechange(self):
		if not self.shapechange:
			print("Used Shapechange Polymorph")
			self.shapechange = True
		else:
			print("Already used Shapechange this short/long rest")

	def reset_shapechange(self):
		if self.shapechange:
			print("Refreshed Shapechange")
			self.shapechange = False
		else:
			print("Shapechange is still usable")

	def use_master_transmuter(self):
		if not self.create_transmuter_stone:
			print("Transmuter Stone destroyed. Long rest before making a new one")
			self.create_transmuter_stone = True
		else:
			print("Need to make a new stone")

	def reset_use_master_transmuter(self):
		if self.create_transmuter_stone:
			print("Created a new stone")
			self.create_transmuter_stone = False
		else:
			print("No need to remake the stone because of Master Transmuter")



	def list_transmutation_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Shapechange\n" +

			      "[3]: Reset Shapechange\n" + "[4]: Use Master Transmuter\n" + "[5]: Reset Use Master Transmuter\n" +

			      "[6]: Use Hit Dice\n" + "[7]: Reset Hit Dice\n" + "[8]: Change Level\n" + "[9]: Exit\n"))

		if selection == 1:
			self.use_spell_slot()
		elif selection == 2:
			self.use_shapechange()
		elif selection == 3:
			self.reset_shapechange()
		elif selection == 4:
			self.use_master_transmuter()
		elif selection == 5:
			self.reset_use_master_transmuter()
		elif selection == 6:
			self.use_hit_dice()
		elif selection == 7:
			self.reset_current_hit_dice()
		elif selection == 8:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_spell_slots(self.get_level())
		elif selection == 9:
			print("Leaving")
			return

	def create_transmutation_wizard(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Enchantment()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_cur_spell_slot(level))

		return player

def main_wizard_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Abjuration":
		p1 = Abjuration()
		p1 = p1.create_abjuration_wizard(name)
		class_options = Abjuration.list_abjuration_options
	elif player_subclass == "Divination":
		p1 = Divination()
		p1 = p1.create_divination_wizard(name)
		class_options = Divination.list_divination_options
	elif player_subclass == "Enchantment":
		p1 = Enchantment()
		p1 = p1.create_enchantment_wizard(name)
		class_options = Enchantment.list_enchantment_options
	elif player_subclass == "Illusion":
		p1 = Illusion()
		p1 = p1.create_illusion_wizard(name)
		class_options = Illusion.list_illusion_options
	elif player_subclass == "Transmutation":
		p1 = Transmutation()
		p1 = p1.create_transmutation_wizard(name)
		class_options = Transmutation.list_transmutation_options
	else:
		p1 = Wizard()
		p1 = p1.create_wizard(name)
		class_options = Wizard.list_wizard_options

	wizard_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}





