from Classes.playercharacter import *
warlock_dict = {}


class Warlock(PlayerCharacter):
	def __init__(self):
		self.max_slots = [0] * 6
		self.current_slots = [0] * 6
		self.mystic_arcanum = False
		self.eldritch_master = False
		super().__init__()

	def set_max_spell_slots(self, level):
		if level >= 1:
			self.max_slots[1] = 1
		if level >= 2:
			self.max_slots[1] = 2
		if level >= 3:
			self.max_slots[1] = 0
			self.max_slots[2] = 2
		if level >= 5:
			self.max_slots[2] = 0
			self.max_slots[3] = 2
		if level >= 7:
			self.max_slots[3] = 0
			self.max_slots[4] = 2
		if level >= 9:
			self.max_slots[4] = 0
			self.max_slots[5] = 2
		if level >= 11:
			self.max_slots[5] = 3
		if level >= 17:
			self.max_slots[5] = 4

	def set_current_spell_slots(self):
		self.current_slots[1] = self.max_slots[1]
		self.current_slots[2] = self.max_slots[2]
		self.current_slots[3] = self.max_slots[3]
		self.current_slots[4] = self.max_slots[4]
		self.current_slots[5] = self.max_slots[5]

	def use_spell(self):
		spell_level = 0
		if 1 <= self.get_level() == 2:
			spell_level = 1
		if 3 <= self.get_level() <= 4:
			spell_level = 2
		if 5 <= self.get_level() <= 6:
			spell_level = 3
		if 7 <= self.get_level() <= 8:
			spell_level = 4
		if 9 <= self.get_level() <= 20:
			spell_level = 5
		if self.check_spell(spell_level):
			self.current_slots[spell_level] -= 1
			print("Used spell slot")
		if not self.check_spell(spell_level):
			print("Not enough slots left")

	def check_spell(self, level):
		if self.current_slots[level] > 0:
			return True
		else:
			print("Warlock out of spell slots until next short/long rest.")
			return False

	def get_mystic_arcanum(self):
		return self.mystic_arcanum

	def use_mystic_arcanum(self):
		if not self.get_mystic_arcanum():
			self.mystic_arcanum = True
			print("Used Mystic Arcanum")
		else:
			print("Need to long rest first")

	def reset_mystic_arcanum(self):
		if self.get_mystic_arcanum():
			print("Reset Mystic Arcanum")
			self.mystic_arcanum = False
		else:
			print("Can still use Mystic Arcanum")

	def get_eldritch_master(self):
		return self.eldritch_master

	def use_eldritch_master(self):
		if not self.get_eldritch_master():
			self.set_current_spell_slots()
		else:
			print("Need to long rest before using Eldritch Master again")

	def list_warlock_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" +

			      "[2]: Reset Spell Slots" + "[3]: Use Mystic Arcanum" + "[4]: Reset Mystic Arcanum" +

			      "[5]: Use Hit Dice\n" + "[6]: Reset Hit Dice\n" + "[7]: Change Level\n" + "[8]: Exit\n"))

		if selection == 1:
			self.use_spell()
		if selection == 2:
			self.set_current_spell_slots()
		if selection == 3:
			self.use_mystic_arcanum()
		if selection == 4:
			self.reset_mystic_arcanum()
		elif selection == 5:
			self.use_hit_dice()
		elif selection == 6:
			self.reset_current_hit_dice()
		elif selection == 7:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_spell_slots(self.get_level())
		elif selection == 8:
			print("Leaving")
			return

	def create_warlock(self, name):
		name = name
		level = int(input("What level is this Wizard?"))
		player = Warlock()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(level)
		player.set_current_spell_slots()
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player


class Archfey(Warlock):
	def __init__(self):
		self.fey_presence = False
		self.misty_escape = False
		self.dark_delirium = False
		super().__init__()

	def get_fey_presence(self):
		return self.fey_presence

	def get_misty_escape(self):
		return self.misty_escape

	def get_dark_delirium(self):
		return self.dark_delirium

	def use_fey_presence(self):
		if not self.get_fey_presence():
			print("Used Fey Presence")
			self.fey_presence = True
		else:
			print("Already used Fey Presence this short/long rest")
			return

	def use_misty_escape(self):
		if not self.get_misty_escape():
			print("Used Misty Escape")
			self.misty_escape = True
		else:
			print("Already used Misty Escape this short/long rest")
			return

	def use_dark_delirium(self):
		if not self.get_dark_delirium():
			print("Used Dark Delirium")
			self.dark_delirium = True
		else:
			print("Already used Dark Delirium this short/long rest")

	def reset_fey_presence(self):
		if self.get_fey_presence():
			print("Reset Fey Presence")
			self.fey_presence = False
		else:
			print("Can still use Fey Presence")

	def reset_misty_escape(self):
		if self.get_misty_escape():
			print("Reset Misty Escape")
			self.misty_escape = False
		else:
			print("Can still use Misty Escape")

	def reset_dark_delirium(self):
		if self.get_dark_delirium():
			print("Reset Dark Delirium")
			self.dark_delirium = False
		else:
			print("Can still use Dark Delirium")

	def list_archfey_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" +

			      "[2]: Reset Spell Slots\n" + "[3]: Use Mystic Arcanum\n" + "[4]: Reset Mystic Arcanum\n" +

			      "[5]: Use Fey Presence\n" + "[6]: Reset Fey Presence\n" + "[7]: Use Misty Escape\n" + "[8]: Reset Misty Escape\n" +

			      "[9]: Use Dark Delirium\n" + "[10]: Reset Dark Delirium\n" + "[11]: Use Hit Dice\n" + "[12]: Reset Hit Dice\n" +

			      "[13]: Change Level\n" + "[14]: Exit\n"))

		if selection == 1:
			self.use_spell()
		if selection == 2:
			self.set_current_spell_slots()
		if selection == 3:
			self.use_mystic_arcanum()
		if selection == 4:
			self.reset_mystic_arcanum()
		if selection == 5:
			self.use_fey_presence()
		if selection == 6:
			self.reset_fey_presence()
		if selection == 7:
			self.use_misty_escape()
		if selection == 8:
			self.reset_misty_escape()
		if selection == 9:
			self.use_dark_delirium()
		if selection == 10:
			self.reset_dark_delirium()
		elif selection == 11:
			self.use_hit_dice()
		elif selection == 12:
			self.reset_current_hit_dice()
		elif selection == 13:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_spell_slots(self.get_level())
		elif selection == 14:
			print("Leaving")
			return

	def create_archfey_warlock(self, name):
		name = name
		player = Archfey()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(player.get_level())
		player.set_current_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

class Fiend(Warlock):
	def __init__(self):
		self.dark_ones_own_luck = False
		self.hurl_through_hell = False
		super().__init__()

	def get_dark_ones_own_luck(self):
		return self.get_dark_ones_own_luck()

	def get_hurl_through_hell(self):
		return self.hurl_through_hell

	def use_dark_ones_own_luck(self):
		if not self.get_dark_ones_own_luck():
			print("Warlock used Dark One's Own Luck")
			self.dark_ones_own_luck = True
		else:
			print("Already used Dark One's Own Luck this rest")
			return
	def use_hurl_through_hell(self):
		if not self.get_hurl_through_hell():
			print("Warlock used Hurl Through Hell")
			self.hurl_through_hell = True
		else:
			print("Warlock already used Hurl Through Hell this rest")
			return

	def reset_dark_ones_own_luck(self):
		if self.get_dark_ones_own_luck():
			print("Reset Dark One's Own Luck")
			self.dark_ones_own_luck = False
		else:
			print("Can still use Dark One's Own Luck this rest period")

	def reset_hurl_through_hell(self):
		if self.get_hurl_through_hell():
			print("Reset Hurl Through Hell")
			self.hurl_through_hell = False
		else:
			print("Hurl Through Hell Still Usable this rest period")

	def list_fiend_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" +

			      "[2]: Reset Spell Slots\n" + "[3]: Use Mystic Arcanum\n" + "[4]: Reset Mystic Arcanum\n" +

			      "[5]: Use Dark One's Own Luck\n" + "[6]: Reset Dark One's Own Luck\n" + "[7]: Use Hurl Through Hell\n" +

			      "[8]: Reset Hurl Through Hell\n" + "[9]: Use Hit Dice\n" + "[10]: Reset Hit Dice\n" +

			      "[11]: Change Level\n" + "[12]: Exit\n"))

		if selection == 1:
			self.use_spell()
		if selection == 2:
			self.set_current_spell_slots()
		if selection == 3:
			self.use_mystic_arcanum()
		if selection == 4:
			self.reset_mystic_arcanum()
		if selection == 5:
			self.use_dark_ones_own_luck()
		if selection == 6:
			self.reset_dark_ones_own_luck()
		if selection == 7:
			self.use_hurl_through_hell()
		if selection == 8:
			self.reset_hurl_through_hell()
		elif selection == 9:
			self.use_hit_dice()
		elif selection == 10:
			self.reset_current_hit_dice()
		elif selection == 11:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_spell_slots(self.get_level())
		elif selection == 12:
			print("Leaving")
			return

	def create_fiend_warlock(self, name):
		name = name
		player = Fiend()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(player.get_level())
		player.set_current_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

class Old(Warlock):
	def __init__(self):
		self.entropic_ward = False
		super().__init__()

	def get_entropic_ward(self):
		return self.entropic_ward

	def use_entropic_ward(self):
		if not self.get_entropic_ward():
			print("Warlock used Entropic Ward")
			self.entropic_ward = True
		else:
			print("Already used Entropic Ward this rest")

	def reset_entropic_ward(self):
		if self.get_entropic_ward():
			print("Reset Entropic Ward")
			self.entropic_ward = False
		else:
			print("Can still use Entropic Ward this rest period")

	def list_old_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Spell Slot\n" +

			      "[2]: Reset Spell Slots\n" + "[3]: Use Mystic Arcanum\n" + "[4]: Reset Mystic Arcanum\n" +

			      "[5]: Use Dark One's Own Luck\n" + "[6]: Reset Dark One's Own Luck\n" + "[9]: Use Hit Dice\n" +

			      "[10]: Reset Hit Dice\n" + "[11]: Change Level\n" + "[12]: Exit\n"))

		if selection == 1:
			self.use_spell()
		if selection == 2:
			self.set_current_spell_slots()
		if selection == 3:
			self.use_mystic_arcanum()
		if selection == 4:
			self.reset_mystic_arcanum()
		if selection == 5:
			self.use_entropic_ward()
		if selection == 6:
			self.reset_entropic_ward()
		elif selection == 9:
			self.use_hit_dice()
		elif selection == 10:
			self.reset_current_hit_dice()
		elif selection == 11:
			self.set_level()
			self.set_hit_dice(self.get_level())
			self.set_max_spell_slots(self.get_level())
		elif selection == 12:
			print("Leaving")
			return

	def create_old_warlock(self, name):
		name = name
		player = Old()
		player.set_level()
		player.set_name(name)
		player.set_max_spell_slots(player.get_level())
		player.set_current_spell_slots()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

def main_warlock_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Archfey":
		p1 = Archfey()
		p1 = p1.create_archfey_warlock(name)
		class_options = Archfey.list_archfey_options
	elif player_subclass == "Fiend":
		p1 = Fiend()
		p1 = p1.create_fiend_warlock(name)
		class_options = Fiend.list_fiend_options
	elif player_subclass == "Old":
		p1 = Old()
		p1 = p1.create_old_warlock(name)
		class_options = Old.list_old_options
	else:
		p1 = Warlock()
		p1 = p1.create_warlock(name)
		class_options = Warlock.list_warlock_options

	warlock_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}



