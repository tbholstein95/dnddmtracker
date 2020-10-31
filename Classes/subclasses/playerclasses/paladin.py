from Classes.subclasses.half_caster import *
paladin_dict = {}

class Paladin(HalfCaster):
	def __init__(self):
		self.max_divine_sense = 0
		self.current_divine_sense = 0
		self.max_lay_on_hands = 0
		self.current_lay_on_hands = 0
		self.charisma = 0
		self.channel_divinity = False
		self.max_cleansing_touch = 0
		self.current_cleansing_touch = 0
		HalfCaster.__init__(self)

	def set_charisma(self):
		char = int(input("What is this Paladin's charisma modifier?"))
		self.charisma = char

	def get_charisma(self):
		return self.charisma

	def set_max_divine_sense(self):
		char = self.get_charisma()
		self.max_divine_sense = char + 1

	def set_current_divine_sense(self):
		self.current_divine_sense = self.max_divine_sense

	def get_current_divine_sense(self):
		return self.current_divine_sense

	def use_divine_sense(self):
		cur_divine_sense = self.get_current_divine_sense()
		if cur_divine_sense > 0:
			print("Paladin used Divine Sense")
			self.current_divine_sense -= 1
		else:
			print("Not enough points in Divine Sense left")

	def set_max_lay_on_hands_pool(self):
		cur_level = self.get_level()
		pool = 5 * cur_level
		self.max_lay_on_hands = pool

	def set_current_lay_on_hands_pool(self):
		self.current_lay_on_hands = self.max_lay_on_hands

	def get_current_lay_on_hands(self):
		return self.current_lay_on_hands

	def use_lay_on_hands_to_heal(self):
		amount = int(input("How many points would the Paladin like to use?"))
		if amount <= self.get_current_lay_on_hands():
			self.current_lay_on_hands -= amount
		else:
			print("Paladin only has {} points left".format(self.get_current_lay_on_hands()))

	def use_lay_on_hands_remove_poison(self):
		if self.get_current_lay_on_hands() >= 5:
			print("Spending 5 points to remove poison/disease")
			self.current_lay_on_hands = self.get_current_lay_on_hands() - 5
		else:
			print("Paladin only has {} points left".format(self.get_current_lay_on_hands()))

	def use_channel_divinity(self):
		if not self.channel_divinity:
			print("Used Channel Divinity")
			self.channel_divinity = True
		else:
			print("Already used Channel Divinity this long rest")

	def reset_channel_divinity(self):
		if self.channel_divinity:
			print("Reset Channel Divinity")
			self.channel_divinity = False
		else:
			print("Can still use Channel Divinity")

	def set_max_cleansing_touch(self):
		char = self.get_charisma()
		self.max_cleansing_touch = char

	def get_max_cleansing_touch(self):
		return self.max_cleansing_touch

	def set_current_cleansing_touch(self):
		max = self.get_max_cleansing_touch()
		self.current_cleansing_touch = max

	def get_current_cleansing_touch(self):
		return self.current_cleansing_touch

	def use_cleansing_touch(self):
		if self.get_current_cleansing_touch() > 0:
			print("Used Cleansing Touch")
			self.current_cleansing_touch -= 1
		else:
			print("Not enough Cleansing Touch points left")

	def list_paladin_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Divine Sense\n" +

			      "[3]: Reset Divine Sense\n" + "[4]: Use Lay on Hands to Heal\n" + "[5]: Use Lay on Hands to Cure Poison/Disease\n" +

			      "[6]: Reset Lay on Hands Pool\n" + "[7]: Use Channel Divinity\n" + "[8]: Reset Channel Divinity\n" + "[9] Use Cleansing Touch\n" +

			      "[10]: Reset Cleansing Touch\n" + "[11]: Use Hit Dice\n" + "[12]: Reset Hit Dice\n" + "[13]: Change Level\n" + "[14]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.use_divine_sense()
		elif selection == 3:
			self.set_current_divine_sense()
		elif selection == 4:
			self.use_lay_on_hands_to_heal()
		elif selection == 5:
			self.use_lay_on_hands_remove_poison()
		elif selection == 6:
			self.set_current_lay_on_hands_pool()
		elif selection == 7:
			self.use_channel_divinity()
		elif selection == 8:
			self.reset_channel_divinity()
		elif selection == 9:
			self.use_cleansing_touch()
		elif selection == 10:
			self.set_current_cleansing_touch()
		elif selection == 11:
			self.use_hit_dice()
		elif selection == 12:
			self.reset_current_hit_dice()
		elif selection == 13:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_current_spell_slots(self.get_level())
		elif selection == 14:
			print("Leaving")
			return

	def create_paladin(self, name):
		name = name
		level = int(input("What level is this Paladin?"))
		player = Devotion()
		player.set_charisma()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(level)
		player.set_current_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_current_spell_slot(level))

		return player

class Devotion(Paladin):
	def __init__(self):
		self.holy_nimbus = False
		Paladin.__init__(self)

	def use_holy_nimbus(self):
		if not self.holy_nimbus:
			print("Use Holy Nimbus")
			self.holy_nimbus = True
		else:
			print("Already used Holy Nimbus this Long Rest")

	def reset_holy_nimbus(self):
		if self.holy_nimbus:
			print("Refreshed Holy Nimbus")
			self.holy_nimbus = False
		else:
			print("Holy Nimbus is still good to be used")

	def list_devotion_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Divine Sense\n" +

			      "[3]: Reset Divine Sense\n" + "[4]: Use Lay on Hands to Heal\n" + "[5]: Use Lay on Hands to Cure Poison/Disease\n" +

			      "[6]: Reset Lay on Hands Pool\n" + "[7]: Use Channel Divinity\n" + "[8]: Reset Channel Divinity\n" + "[9] Use Cleansing Touch\n" +

			      "[10]: Reset Cleansing Touch\n" + "[11]: Use Holy Nimbus\n" + "[12]: Reset Holy Nimbus\n" +

			      "[13]: Use Hit Dice\n" + "[14]: Reset Hit Dice\n" + "[15]: Change Level\n" + "[16]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.use_divine_sense()
		elif selection == 3:
			self.set_current_divine_sense()
		elif selection == 4:
			self.use_lay_on_hands_to_heal()
		elif selection == 5:
			self.use_lay_on_hands_remove_poison()
		elif selection == 6:
			self.set_current_lay_on_hands_pool()
		elif selection == 7:
			self.use_channel_divinity()
		elif selection == 8:
			self.reset_channel_divinity()
		elif selection == 9:
			self.use_cleansing_touch()
		elif selection == 10:
			self.set_current_cleansing_touch()
		elif selection == 11:
			self.use_holy_nimbus()
		elif selection == 12:
			self.reset_holy_nimbus()
		elif selection == 13:
			self.use_hit_dice()
		elif selection == 14:
			self.reset_current_hit_dice()
		elif selection == 15:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_current_spell_slots(self.get_level())
		elif selection == 16:
			print("Leaving")
			return

	def create_devotion_paladin(self, name):
		name = name
		level = int(input("What level is this Paladin?"))
		player = Devotion()
		player.set_charisma()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(level)
		player.set_current_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_current_spell_slot(level))

		return player

class Ancient(Paladin):
	def __init__(self):
		self.elder_champion = False
		Paladin.__init__(self)

	def use_elder_champion(self):
		if not self.elder_champion:
			print("Used Elder Champion")
			self.elder_champion = True
		else:
			print("Already Used Elder Champion this long rest")

	def reset_elder_champion(self):
		if self.elder_champion:
			print("Reset Elder Champion")
			self.elder_champion = False
		else:
			print("Paladin can still use Elder Champion")

	def list_ancients_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Divine Sense\n" +

			      "[3]: Reset Divine Sense\n" + "[4]: Use Lay on Hands to Heal\n" + "[5]: Use Lay on Hands to Cure Poison/Disease\n" +

			      "[6]: Reset Lay on Hands Pool\n" + "[7]: Use Channel Divinity\n" + "[8]: Reset Channel Divinity\n" + "[9] Use Cleansing Touch\n" +

			      "[10]: Reset Cleansing Touch\n" + "[11]: Use Elder Champion\n" + "[12]: Reset Elder Champion\n" +

			      "[13]: Use Hit Dice\n" + "[14]: Reset Hit Dice\n" + "[15]: Change Level\n" + "[16]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.use_divine_sense()
		elif selection == 3:
			self.set_current_divine_sense()
		elif selection == 4:
			self.use_lay_on_hands_to_heal()
		elif selection == 5:
			self.use_lay_on_hands_remove_poison()
		elif selection == 6:
			self.set_current_lay_on_hands_pool()
		elif selection == 7:
			self.use_channel_divinity()
		elif selection == 8:
			self.reset_channel_divinity()
		elif selection == 9:
			self.use_cleansing_touch()
		elif selection == 10:
			self.set_current_cleansing_touch()
		elif selection == 11:
			self.use_elder_champion()
		elif selection == 12:
			self.reset_elder_champion()
		elif selection == 13:
			self.use_hit_dice()
		elif selection == 14:
			self.reset_current_hit_dice()
		elif selection == 15:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_current_spell_slots(self.get_level())
		elif selection == 16:
			print("Leaving")
			return

	def create_ancients_paladin(self, name):
		name = name
		level = int(input("What level is this Paladin?"))
		player = Devotion()
		player.set_charisma()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(level)
		player.set_current_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_current_spell_slot(level))

		return player

class Vengeance(Paladin):
	def __init__(self):
		self.avenging_angel = False
		Paladin.__init__(self)

	def use_avenging_angel(self):
		if not self.avenging_angel:
			print("Used Avenging Angel")
			self.avenging_angel = True
		else:
			print("Already used Avenging Angel")

	def reset_avenging_angel(self):
		if self.avenging_angel:
			print("Reset Avenging Angel")
			self.avenging_angel = False
		else:
			print("Avenging Angel is still usable")

	def list_vengeance_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Use Divine Sense\n" +

			      "[3]: Reset Divine Sense\n" + "[4]: Use Lay on Hands to Heal\n" + "[5]: Use Lay on Hands to Cure Poison/Disease\n" +

			      "[6]: Reset Lay on Hands Pool\n" + "[7]: Use Channel Divinity\n" + "[8]: Reset Channel Divinity\n" + "[9] Use Cleansing Touch\n" +

			      "[10]: Reset Cleansing Touch\n" + "[11]: Use Avenging Angel\n" + "[12]: Reset Avenging Angel\n" +

			      "[13]: Use Hit Dice\n" + "[14]: Reset Hit Dice\n" + "[15]: Change Level\n" + "[16]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.use_divine_sense()
		elif selection == 3:
			self.set_current_divine_sense()
		elif selection == 4:
			self.use_lay_on_hands_to_heal()
		elif selection == 5:
			self.use_lay_on_hands_remove_poison()
		elif selection == 6:
			self.set_current_lay_on_hands_pool()
		elif selection == 7:
			self.use_channel_divinity()
		elif selection == 8:
			self.reset_channel_divinity()
		elif selection == 9:
			self.use_cleansing_touch()
		elif selection == 10:
			self.set_current_cleansing_touch()
		elif selection == 11:
			self.use_avenging_angel()
		elif selection == 12:
			self.reset_avenging_angel()
		elif selection == 13:
			self.use_hit_dice()
		elif selection == 14:
			self.reset_current_hit_dice()
		elif selection == 15:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_spell_slots(self.get_level())
			self.set_current_spell_slots(self.get_level())
		elif selection == 16:
			print("Leaving")
			return

	def create_vengeance_paladin(self, name):
		name = name
		level = int(input("What level is this Paladin?"))
		player = Devotion()
		player.set_charisma()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(level)
		player.set_current_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(),
		      "Slots" + player.get_current_spell_slot(level))

		return player

def main_paladin_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Devotion":
		p1 = Devotion()
		p1 = p1.create_devotion_paladin(name)
		class_options = Devotion.list_devotion_options
	elif player_subclass == "Ancient":
		p1 = Ancient()
		p1 = p1.create_ancients_paladin(name)
		class_options = Ancient.list_ancients_options
	elif player_subclass == "Vengeance":
		p1 = Vengeance()
		p1 = p1.create_vengeance_paladin(name)
		class_options = Vengeance.list_vengeance_options
	else:
		p1 = Paladin()
		p1 = p1.create_paladin(name)
		class_options = Paladin.list_paladin_options

	paladin_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}
