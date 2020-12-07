from Classes.subclasses.full_caster import *
wizard_dict = {}


class Wizard(FullCaster):
	def __init__(self):
		self.signature_spells = 2
		self.wizard_options = {}
		super().__init__()

	def use_signature_spells(self):
		if self.signature_spells > 0:
			print("Used a signature spell")
			self.signature_spells -= 1
		else:
			print("Out of signature spells this long rest.")

	def reset_signature_spells(self):
		print("Reset Signature Spells")
		self.signature_spells = 2

	def create_wizard_options(self):
		self.wizard_options['0'] = "[5]: Use Signature Spells" + "[6]: Reset Signature Spells"
		self.wizard_options['5'] = self.use_signature_spells
		self.wizard_options['6'] = self.reset_signature_spells
		return self.wizard_options

	def list_options(self):
		selection = int_checker(self.wizard_options.get("0"))
		print(selection)
		self.wizard_options["{}".format(selection)]()


class Abjuration(Wizard):
	def __init__(self):
		self.arcane_ward = False
		self.abjuration_options = {}
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

	def create_abjuration_options(self):
		self.abjuration_options['0'] = "[7]: Use Arcane Ward\n" + "[8]: Reset Arcane Ward\n" + \
					"[9]: Change Level\n" + "[10]: Exit\n"
		self.abjuration_options['7'] = self.use_arcane_ward
		self.abjuration_options['8'] = self.reset_arcane_ward
		self.abjuration_options['9'] = self.change_fullcaster_level
		self.abjuration_options['10'] = leave
		return self.abjuration_options

	def list_options(self):
		selection = int_checker(self.abjuration_options.get("0"))
		print(selection)
		self.abjuration_options["{}".format(selection)]()


class Divination(Wizard):
	def __init__(self):
		self.max_portent = 0
		self.current_portent = 0
		self.third_eye = False
		self.divination_options = {}
		super().__init__()

	def use_expert_divination(self):
		if self.get_level() >= 6:
			spell_level = self.use_cur_spell_slot()
			restore_slot = int_checker("What spell slot would they like to restore?")
			if restore_slot < 6 and restore_slot < spell_level:
				self.add_spell_slot(restore_slot)
			else:
				print("Must restore a spell slot less than 6th level and lower than spell level cast")

	def set_max_portent(self):
		if 2 <= self.get_level() < 14:
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

	def change_divination_level(self):
		self.change_fullcaster_level()
		self.set_max_portent()
		self.reset_current_portents()

	def create_divination_options(self):
		self.divination_options['0'] = "[7]: Use Expert Divination\n" + "[8]: Use Portent\n" + \
					"[9]: Reset Current Portents\n" + "[10]: Change Level\n" + "[11]: Exit\n"
		self.divination_options['7'] = self.use_expert_divination
		self.divination_options['8'] = self.use_portent
		self.divination_options['9'] = self.reset_current_portents
		self.divination_options['10'] = self.change_divination_level
		self.divination_options['11'] = leave
		return self.divination_options

	def list_options(self):
		selection = int_checker(self.divination_options.get("0"))
		print(selection)
		self.divination_options["{}".format(selection)]()


class Enchantment(Wizard):
	def __init__(self):
		self.hypnotic_gaze = False
		self.instinctive_charm = False
		self.enchantment_options = {}
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

	def create_enchantment_options(self):
		self.enchantment_options['0'] = "[7]: Use Hypnotic Gaze\n" + "[8]: Reset Hypnotic Gaze\n" + \
					"[9]: Use Instinctive Charm\n" + "[10]: Reset Instinctive Charm\n" + \
					"[11]: Change Level\n" + "[12]: Exit\n"

		self.enchantment_options['7'] = self.use_hypnotic_gaze
		self.enchantment_options['8'] = self.reset_hypnotic_gaze
		self.enchantment_options['9'] = self.use_instinctive_charm
		self.enchantment_options['10'] = self.reset_instinctive_charm
		self.enchantment_options['11'] = self.change_fullcaster_level
		self.enchantment_options['12'] = leave
		return self.enchantment_options

	def list_options(self):
		selection = int_checker(self.enchantment_options.get("0"))
		print(selection)
		self.enchantment_options["{}".format(selection)]()


class Illusion(Wizard):
	def __init__(self):
		self.illusory_self = False
		self.illusion_options = {}
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

	def create_illusion_options(self):
		self.illusion_options['0'] = "[7]: Use Illusory Self\n" + "[8]: Reset Illusory Self\n" \
					+ "[9]: Change Level\n" + "[10]: Exit\n"
		self.illusion_options['7'] = self.use_illusory_self
		self.illusion_options['8'] = self.reset_illusory_set
		self.illusion_options['9'] = self.change_fullcaster_level
		self.illusion_options['10'] = leave
		return self.illusion_options

	def list_options(self):
		selection = int_checker(self.illusion_options.get("0"))
		print(selection)
		self.illusion_options["{}".format(selection)]()


class Transmutation(Wizard):
	def __init__(self):
		self.shapechange = False
		self.create_transmuter_stone = False
		self.transmutation_options = {}
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

	def create_transmutation_options(self):
		self.transmutation_options['0'] = "[7]: Use Shapechange\n" + "[8]: Reset Shapechange\n" + \
						"[9]: Use Master Transmuter\n" + "[10]: Reset Use Master Transmuter\n" + \
						"[11]: Change Level\n" + "[12]: Exit\n"
		self.transmutation_options['7'] = self.use_shapechange
		self.transmutation_options['8'] = self.reset_shapechange
		self.transmutation_options['9'] = self.use_master_transmuter
		self.transmutation_options['10'] = self.reset_use_master_transmuter
		self.transmutation_options['11'] = self.change_fullcaster_level()
		self.transmutation_options['12'] = leave
		return self.transmutation_options

	def list_options(self):
		selection = int_checker(self.transmutation_options.get("0"))
		print(selection)
		self.transmutation_options["{}".format(selection)]()


def merge_base_wizard_dicts(player):
	wizard_opts = player.create_wizard_options()
	merge_dicts(player.merge_base_and_fullspell_options(), wizard_opts)
	return wizard_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_wizard(name):
	player = create(name, Wizard)
	player.change_fullcaster_level()
	merge_base_wizard_dicts(player)
	return player


def create_abjuration_wizard(name):
	player = create(name, Abjuration)
	player.change_fullcaster_level()
	merge_dicts(merge_base_wizard_dicts(player), player.create_abjuration_options())
	return player


def create_divination_wizard(name):
	player = create(name, Divination)
	player.change_divination_level()
	merge_dicts(merge_base_wizard_dicts(player), player.create_divination_options())
	return player


def create_enchantment_wizard(name):
	player = create(name, Enchantment)
	player.change_fullcaster_level()
	merge_dicts(merge_base_wizard_dicts(player), player.create_enchantment_options())
	return player


def create_illusion_wizard(name):
	player = create(name, Illusion)
	player.change_fullcaster_level()
	merge_dicts(merge_base_wizard_dicts(player), player.create_illusion_options())
	return player


def create_transmutation_wizard(name):
	player = create(name, Transmutation)
	player.change_fullcaster_level()
	merge_dicts(merge_base_wizard_dicts(player), player.create_transmutation_options())
	return player


def main_wizard_making(name, dictionary):
	player_subclass = input("What is their subclass?").capitalize()
	if player_subclass == "Abjuration":
		p1 = create_abjuration_wizard(name)
		class_options = Abjuration.list_options
	elif player_subclass == "Divination":
		p1 = create_divination_wizard(name)
		class_options = Divination.list_options
	elif player_subclass == "Enchantment":
		p1 = create_enchantment_wizard(name)
		class_options = Enchantment.list_options
	elif player_subclass == "Illusion":
		p1 = create_illusion_wizard(name)
		class_options = Illusion.list_options
	elif player_subclass == "Transmutation":
		p1 = create_transmutation_wizard(name)
		class_options = Transmutation.list_options
	else:
		p1 = create_wizard(name)
		class_options = Wizard.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}





