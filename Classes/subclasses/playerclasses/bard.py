from Classes.subclasses.full_caster import *
bard_dict = {}


class Bard(FullCaster):

	def __init__(self):
		self.charisma = 0
		self.counter_charm = False
		self.max_bardic_inspiration = 0
		self.current_bardic_inspiration = 0
		super().__init__()

	def get_max_bardic_inspiration(self):
		return self.max_bardic_inspiration

	def get_current_bardic_inspiration(self):
		return self.current_bardic_inspiration

	def get_charisma(self):
		return self.charisma

	def set_charisma(self):
		self.charisma = int(input("What should this Bard's charisma be?"))

	def set_max_bardic_inspiration(self):
		cur_charisma = self.get_charisma()
		if cur_charisma < 1:
			cur_charisma = 1
		self.max_bardic_inspiration = cur_charisma

	def set_cur_bardic_inspiration(self, amount):
		self.current_bardic_inspiration = amount

	def reset_bardic_inspiration(self):
		self.current_bardic_inspiration = self.get_max_bardic_inspiration()
		print("Reset Bardic Inspiration")

	def use_bardic_inspiration(self):
		if self.check_bardic_inspiration():
			self.current_bardic_inspiration -= 1
			print("Used Bardic Inspiration!")
		else:
			print("Out of Bardic Inspiration")

	def check_bardic_inspiration(self):
		if self.get_current_bardic_inspiration() == 0:
			return False
		else:
			return True

	def charisma_option(self):
		self.set_charisma()
		self.set_max_bardic_inspiration()
		self.set_cur_bardic_inspiration(self.get_charisma)

	def change_level_option(self):
		self.set_level()
		self.set_charisma()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()
		self.set_max_bardic_inspiration()
		self.set_cur_bardic_inspiration(self.get_charisma)


	def list_bard_options(self):
		selection = int(
			input("What actions are you counting?\n" + "[1]: Cast Spell\n" + "[2]: Reset Spells\n" +

			"[3]: Use Bardic Inspiration\n" + "[4]: Use Hit Dice\n" + "[5]: Reset Hit Dice\n" +

			"[6]: Change Level\n" + "[7]: Change Charisma\n" + "[8]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		if selection == 2:
			self.set_current_list_spell_slots()
		if selection == 3:
			self.use_bardic_inspiration()
			print("Used Bardic Inspiration")
		if selection == 4:
			self.use_hit_dice()
		if selection == 5:
			self.reset_current_hit_dice()
		if selection == 6:
			self.change_level_option()
		if selection == 7:
			self.charisma_option()
		if selection == 8:
			print("Leaving")
			return

	def create_bard(self, name):
		name = name
		player = Bard()
		player.set_name(name)
		player.set_level()
		player.set_charisma()
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Bardic Inspiration:", (
			player.get_current_bardic_inspiration(), "Charisma:", + player.get_charisma()))

		return player



class Glamour(Bard):

	def __init__(self):
		self.enthralling_performance = False
		self.mantle_of_majesty = False
		self.unbreakable_majesty = False
		super().__init__()

	def use_of_enthralling_performance(self):
		self.enthralling_performance = True
		self.use_bardic_inspiration()
		print("Used Enthralling Performance")

	def use_enthralling_performance(self):
		cur_bardic_inspo = self.get_current_bardic_inspiration()
		if cur_bardic_inspo < 1:
			print("Player does not have enough Bardic Inspiration to perform this action")
		else:
			self.use_of_enthralling_performance()

	def reset_enthralling_performance(self):
		self.enthralling_performance = False
		print("Reset Enthralling Performance")

	def use_mantle_of_majesty(self):
		if not self.mantle_of_majesty:
			self.mantle_of_majesty = True
			print("Used Mantle of Majesty")
		else:
			print("Mantle of Majesty already active")

	def reset_mantle_of_majesty(self):
		self.mantle_of_majesty = False
		print("Mantle of Majesty reset")

	def use_unbreakable_majesty(self):
		if not self.unbreakable_majesty:
			self.unbreakable_majesty = True
			print("Used Unbreakable Majesty")
		else:
			print("Unbreakable Majesty already active")

	def reset_unbreakable_majesty(self):
		self.unbreakable_majesty = False
		print("Reset Unbreakable Majesty")

	def create_glamour_bard(self, name):
		name = name
		player = Glamour()
		player.set_level()
		player.set_charisma()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_max_bardic_inspiration()
		player.set_cur_bardic_inspiration(player.get_charisma())
		player.set_hit_dice(player.get_level())

		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Bardic Inspiration:", (
			player.get_current_bardic_inspiration(), "Charisma:", + player.get_charisma()))

		return player

	def list_glamour_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Cast Spell\n" + "[2]: Reset Spell Slots\n" + "[3]: Use Bardic Inspiration\n" +

			"[4: Use Enthralling Performance\n" + "[5]: Reset Enthralling Performance" + "[5]: Use Mantle of Majesty\n" +

			"[6]: Use Unbreakable Majesty\n" + "[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice\n" +

			"[9]: Change Level\n" + "[10]: Change Charisma\n" + "[11]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		if selection == 2:
			self.set_current_list_spell_slots()
		if selection == 3:
			self.use_bardic_inspiration()
			print(self.get_current_bardic_inspiration(), "Current Bardic Inspiration")
		if selection == 4:
			self.reset_bardic_inspiration()
		elif selection == 4:
			self.use_enthralling_performance()
			print(self.get_current_bardic_inspiration(), "Current Bardic Inspiration")
		elif selection == 5:
			print("Reset Enthralling Performance")
			self.reset_enthralling_performance()
		elif selection == 6:
			self.use_mantle_of_majesty()
		elif selection == 7:
			self.reset_mantle_of_majesty()
		elif selection == 8:
			self.use_unbreakable_majesty()
		elif selection == 9:
			self.reset_unbreakable_majesty()
		elif selection == 10:
			dice_to_use = int(input("How many dice did Bard use?"))
			self.set_hit_dice(dice_to_use)
		elif selection == 11:
			self.reset_current_hit_dice()
		elif selection == 12:
			self.change_level_option()
		elif selection == 13:
			self.charisma_option()
		elif selection == 14:
			return 0

class Swords(Bard):
	def __init__(self):
		self.blade_flourish = False
		super().__init__()

	def get_blade_flourish(self):
		return self.blade_flourish

	def use_blade_flourish(self):
		available = self.get_blade_flourish()
		if not available:
			self.blade_flourish = True
			print("Used Blade Flourish!")
		else:
			print("Blade Flourish already used this turn")

	def reset_blade_flourish(self):
		self.blade_flourish = False

	def create_swords_bard(self, name):
		name = name
		player = Swords()
		player.set_level()
		player.set_charisma()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_max_bardic_inspiration()
		player.set_cur_bardic_inspiration(player.get_charisma())
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Bardic Inspiration:", (
			player.get_current_bardic_inspiration(), "Charisma:", + player.get_charisma()))

		return player

	def list_swords_options(self):
		selection = int(
			input("What actions are you counting?\n" + "[1]: Use Spell Slot\n" + "[2]: Reset Spell Slot\n" +

			"[3]: Use Bardic Inspiration\n" + "[4]: Reset Bardic Inspiration\n" + "[5]: Use Blade Flourish\n" +

			"[6]: Reset Blade Flourish\n" +  "[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice"

			+ "[8]: Change Level\n" + "[9]: Change Charisma\n" + "[10]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		if selection == 2:
			self.set_current_list_spell_slots()
		if selection == 3:
			self.use_bardic_inspiration()
		if selection == 4:
			self.reset_bardic_inspiration()
		if selection == 5:
			self.use_blade_flourish()
		if selection == 6:
			self.reset_blade_flourish()
		if selection == 7:
			self.use_hit_dice()
		if selection == 8:
			self.reset_current_hit_dice()
		if selection == 9:
			self.change_level_option()
		if selection == 10:
			self.charisma_option()
		if selection == 11:
			print("Leaving")
			return


class Whispers(Bard):
	def __init__(self):
		self.psychic_blades = False
		self.words_of_terror = False
		self.mantle_of_whispers = False
		self.shadow_lore = False
		super().__init__()

	def get_psychic_blades(self):
		return self.psychic_blades

	def get_words_of_terror(self):
		return self.words_of_terror

	def get_mantle_of_whispers(self):
		return self.mantle_of_whispers

	def get_shadow_lore(self):
		return self.shadow_lore

	def set_psychic_blades(self, truefalse):
		self.psychic_blades = truefalse

	def use_psychic_blades(self):
		if self.get_current_bardic_inspiration() == 0:
			print("Not enough Bardic Inspiration")
			return
		elif self.get_psychic_blades:
			print("Already used Psychic Blades")
			return
		else:
			self.set_psychic_blades(True)
			self.use_bardic_inspiration()
			print("Used Psychic Blades. Cannot use again until next turn.")

	def reset_psychic_blades(self):
		self.set_psychic_blades(False)

	def set_words_of_terror(self, truefalse):
		self.words_of_terror = truefalse

	def use_words_of_terror(self):
		if self.get_words_of_terror():
			print("Already used Words of Terror this awake cycle")
			return
		else:
			self.words_of_terror = True

	def reset_words_of_terror(self):
		self.set_words_of_terror(False)

	def set_mantle_of_whispers(self, truefalse):
		self.mantle_of_whispers = truefalse

	def use_mantle_of_whispers(self):
		if self.get_mantle_of_whispers():
			print("Already used this Awake cycle")
			return
		elif self.get_current_bardic_inspiration() == 0:
			print("Not enough Bardic Inspriation left")
			return
		else:
			self.set_mantle_of_whispers(True)

	def reset_mantle_of_whispers(self):
		self.set_mantle_of_whispers(False)

	def set_shadow_lore(self, truefalse):
		self.shadow_lore = truefalse

	def use_shadow_lore(self):
		if self.get_shadow_lore():
			print("Already used Shadow Lore this Awake Cycle")
			return
		if not self.check_bardic_inspiration():
			print("Not enough Bardic Inspiration to use Shadow Lore")
		else:
			self.set_shadow_lore(True)

	def reset_shadow_lore(self):
		self.set_shadow_lore(False)

	def list_whispers_options(self):
		selection = int(

			input("What action are you counting?\n" + "[1]: Cast Spell\n" + "[2]: Reset Spells\n" +

			"[3]: Use Bardic Inspiration\n" + "[4]: Reset Bardic Inspiration\n" + "[5]: Use Psychic Blades\n" +

			"[6]: Reset Psychic Blades\n" + "[7]: Use Words of Terror\n" + "[8]: Reset Words of Terror\n" +

			"[9]: Use Mantle of Whispers\n" + "[10]: Reset Mantle of Whispers\n" + "[11]: Use Shadow Lore\n" +

			"[12]: Reset Shadow Lore\n" + "[13]: Use Hit Dice\n" + "[14]: Change Level\n" +

			"[15]: Change Charisma\n" + "[16]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		if selection ==2:
			self.set_current_list_spell_slots()
		if selection == 3:
			self.use_bardic_inspiration()
			print(self.get_current_bardic_inspiration(), "Current Bardic Inspiration")
		elif selection == 4:
			self.reset_bardic_inspiration()
		elif selection == 5:
			self.use_psychic_blades()
			print(self.get_psychic_blades(), "Current Psychic Blades")
		elif selection == 6:
			self.reset_psychic_blades()
		elif selection == 7:
			self.use_words_of_terror()
			print(self.get_words_of_terror(), "Current Words of Terror")
		elif selection == 8:
			self.reset_words_of_terror()
		elif selection == 9:
			self.use_mantle_of_whispers()
			print(self.get_mantle_of_whispers())
		elif selection == 10:
			self.reset_mantle_of_whispers()
		elif selection == 11:
			self.use_shadow_lore()
			print(self.get_shadow_lore(), "Current Shadow Lore")
		elif selection == 12:
			self.reset_shadow_lore()
		elif selection == 13:
			dice_to_use = int(input("How many dice did Bard use?"))
			self.set_hit_dice(dice_to_use)
		elif selection == 14:
			self.reset_current_hit_dice()
		elif selection == 15:
			self.change_level_option()
		elif selection == 16:
			self.charisma_option()
		elif selection == 15:
			print("Leaving")
			return

	def create_whispers_bard(self, name):
		name = name
		player = Whispers()
		player.set_level()
		player.set_charisma()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Bardic Inspiration:", (
			player.get_current_bardic_inspiration(), "Charisma:", + player.get_charisma()))

		return player


def main_bard_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Glamour":
		p1 = Glamour()
		p1 = p1.create_glamour_bard(name)
		class_options = Glamour.list_glamour_options
	elif player_subclass == "Swords":
		p1 = Swords()
		p1 = p1.create_swords_bard(name)
		class_options = Swords.list_swords_options
	elif player_subclass == "Whispers":
		p1 = Whispers()
		p1 = p1.create_whispers_bard(name)
		class_options = Whispers.list_whispers_options
	else:
		p1 = Bard()
		p1 = p1.create_bard(name)
		class_options = Bard.list_bard_options

	bard_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}








