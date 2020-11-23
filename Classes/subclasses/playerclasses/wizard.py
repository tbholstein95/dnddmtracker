from Classes.subclasses.full_caster import *
wizard_dict = {}
# TODO : Refresh spell slots
class Wizard(FullCaster):
	def __init__(self):
		self.signature_spells = 2
		super().__init__()

	def list_wizard_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Reset Spell Slots\n" + "[3]: Use Hit Dice\n" +

			      "[4]: Reset Hit Dice\n" + "[5]: Change Level\n" + "[6]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		if selection == 2:
			self.set_current_list_spell_slots()
		elif selection == 3:
			self.use_hit_dice()
		elif selection == 4:
			self.reset_current_hit_dice()
		elif selection == 5:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_list_spell_slots(self.get_level())
			self.set_current_list_spell_slots()
		elif selection == 6:
			print("Leaving")
			return

	def create_wizard(self, name):
		name = name
		player = Wizard()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_cur_spell_slot(player.get_level()))

		return player

class Abjuration(Wizard):
	def __init__(self):
		self.arcane_ward = False
		super().__init__()

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
		selection = int(input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Reset Spell Slots\n" + "[3]: Use Hit Dice\n" +

		"[4]: Reset Hit Dice\n" + "[5]: Change Level\n" + "[6]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		if selection == 2:
			self.set_current_list_spell_slots()
		elif selection == 3:
			self.use_hit_dice()
		elif selection == 4:
			self.reset_current_hit_dice()
		elif selection == 5:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_list_spell_slots(self.get_level())
			self.set_current_list_spell_slots()
		elif selection == 6:
			print("Leaving")
			return
	def create_abjuration_wizard(self, name):
		name = name
		level = int(input("What level is this Wizard?"))
		player = Abjuration()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(self.get_level())
		player.set_current_list_spell_slots()
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Slots" + player.get_cur_spell_slot(level))

		return player

class Divination(Wizard):
	def __init__(self):
		self.max_portent = 0
		self.current_portent = 0
		self.third_eye = False
		super().__init__()
	#TODO: Fix spell slot
	def use_expert_divination(self):
		if self.get_level() >= 6:
			spell_level = self.use_cur_spell_slot()
			restore_slot = int(input("What spell slot would they like to restore?"))
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
		selection = int(input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Reset Spell Slot\n" +

		"[3]: Use Expert Divination\n" + "[4]: Use Portent\n" + "[5]: Reset Current Portents\n" + "[6]: Use Hit Dice\n" +

		"[7]: Reset Hit Dice\n" + "[8]: Change Level\n" + "[9]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.set_current_list_spell_slots()
		elif selection == 3:
			self.use_expert_divination()
		elif selection == 4:
			self.use_portent()
		elif selection == 5:
			self.reset_current_portents()
		elif selection == 6:
			self.use_hit_dice()
		elif selection == 7:
			self.reset_current_hit_dice()
		elif selection == 8:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_portent()
			self.set_max_list_spell_slots(self.get_level())
			self.set_current_list_spell_slots()
		elif selection == 8:
			print("Leaving")
			return

	def create_divination_wizard(self, name):
		name = name
		player = Divination()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_hit_dice(player.get_level())
		player.set_max_portent()
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Slots" + player.get_cur_spell_slot(player.get_level()))

		return player

class Enchantment(Wizard):
	def __init__(self):
		self.hypnotic_gaze = False
		self.instinctive_charm = False
		super().__init__()

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
		selection = int(input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Reset Spell Slot\n" + "[3]: Use Hypnotic Gaze\n" +

		"[4]: Reset Hypnotic Gaze\n" + "[5]: Use Instinctive Charm\n" + "[6]: Reset Instinctive Charm\n" +

		"[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice\n" + "[9]: Change Level\n" + "[10]: Exit\n"))
		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.set_current_list_spell_slots()
		elif selection == 3:
			self.use_hypnotic_gaze()
		elif selection == 4:
			self.reset_hypnotic_gaze()
		elif selection == 5:
			self.use_instinctive_charm()
		elif selection == 6:
			self.reset_instinctive_charm()
		elif selection == 7:
			self.use_hit_dice()
		elif selection == 8:
			self.reset_current_hit_dice()
		elif selection == 9:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_list_spell_slots(self.get_level())
			self.set_current_list_spell_slots()
		elif selection == 10:
			print("Leaving")
			return

	def create_enchantment_wizard(self, name):
		name = name
		player = Enchantment()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Slots" + player.get_cur_spell_slot(player.get_level()))

		return player

class Illusion(Wizard):
	def __init__(self):
		self.illusory_self = False
		super().__init__()

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
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Reset Spell Slot\n" + "[3]: Use Illusory Self\n" +

			      "[4]: Reset Illusory Self\n" + "[5]: Use Hit Dice\n" + "[6]: Reset Hit Dice\n" + "[7]: Change Level\n" + "[8]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.set_current_list_spell_slots()
		elif selection == 3:
			self.use_illusory_self()
		elif selection == 4:
			self.reset_illusory_set()
		elif selection == 5:
			self.use_hit_dice()
		elif selection == 6:
			self.reset_current_hit_dice()
		elif selection == 7:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_list_spell_slots(self.get_level())
			self.set_current_list_spell_slots()
		elif selection == 8:
			print("Leaving")
			return

	def create_illusion_wizard(self, name):
		name = name
		player = Enchantment()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_cur_spell_slot(player.get_level()))

		return player

class Transmutation(Wizard):
	def __init__(self):
		self.shapechange = False
		self.create_transmuter_stone = False
		super().__init__()

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
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Reset Spell Slot\n" + "[3]: Use Shapechange\n" +

			      "[4]: Reset Shapechange\n" + "[5]: Use Master Transmuter\n" + "[6]: Reset Use Master Transmuter\n" +

			      "[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice\n" + "[9]: Change Level\n" + "[10]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.set_current_list_spell_slots()
		elif selection == 3:
			self.use_shapechange()
		elif selection == 4:
			self.reset_shapechange()
		elif selection == 5:
			self.use_master_transmuter()
		elif selection == 6:
			self.reset_use_master_transmuter()
		elif selection == 7:
			self.use_hit_dice()
		elif selection == 8:
			self.reset_current_hit_dice()
		elif selection == 9:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_list_spell_slots(self.get_level())
			self.set_current_list_spell_slots()
		elif selection == 10:
			print("Leaving")
			return

	def create_transmutation_wizard(self, name):
		name = name
		player = Enchantment()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_cur_spell_slot(player.get_level()))

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





