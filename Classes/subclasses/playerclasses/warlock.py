from Classes.playercharacter import *
warlock_dict = {}


class Warlock(PlayerCharacter):
	def __init__(self):
		self.max_slots = [0] * 6
		self.current_slots = [0] * 6
		self.mystic_arcanum = False
		self.eldritch_master = False
		self.warlock_options = {}
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

	def reset_eldritch_master(self):
		if self.get_eldritch_master():
			print("Reset Eldritch Master")
			self.eldritch_master = False
		else:
			print("Can still use Eldritch Master this long rest")

	def create_warlock_options(self):
		self.warlock_options['0'] = "[3]: Use Spell Slot\n" + "[4]: Reset Spell Slots\n" + \
					"[5]: Use Mystic Arcanum\n" + "[6]: Reset Mystic Arcanum\n" + \
					"[7]: Use Eldritch Master" + "[8]: Reset Eldritch Master"

		self.warlock_options['3'] = self.use_spell
		self.warlock_options['4'] = self.set_current_spell_slots
		self.warlock_options['5'] = self.use_mystic_arcanum
		self.warlock_options['6'] = self.reset_mystic_arcanum
		self.warlock_options['7'] = self.use_eldritch_master
		self.warlock_options['8'] = self.reset_eldritch_master
		return self.warlock_options

	def list_options(self):
		selection = int_checker(self.warlock_options.get("0"))
		print(selection)
		self.warlock_options["{}".format(selection)]()

	def set_base_warlock_level(self):
		self.base_change_level()
		self.set_max_spell_slots(self.get_level())
		self.set_current_spell_slots()


class Archfey(Warlock):
	def __init__(self):
		self.fey_presence = False
		self.misty_escape = False
		self.dark_delirium = False
		self.archfey_options = {}
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

	def create_archfey_options(self):
		self.archfey_options['0'] = "[9]: Use Fey Presence\n" + "[10]: Reset Fey Presence\n" + "[11]: Use Misty Escape\n" + \
					"[12]: Reset Misty Escape\n" + "[13]: Use Dark Delirium\n" + "[14]: Reset Dark Delirium\n" + \
					"[15]: Change Level\n" + "[16]: Exit\n"

		self.archfey_options['9'] = self.use_fey_presence
		self.archfey_options['10'] = self.reset_fey_presence
		self.archfey_options['11'] = self.use_misty_escape
		self.archfey_options['12'] = self.reset_misty_escape
		self.archfey_options['13'] = self.use_dark_delirium
		self.archfey_options['14'] = self.reset_dark_delirium
		self.archfey_options['15'] = self.set_base_warlock_level
		self.archfey_options['16'] = leave
		return self.archfey_options

	def list_options(self):
		selection = int_checker(self.archfey_options.get("0"))
		print(selection)
		self.archfey_options["{}".format(selection)]()


class Fiend(Warlock):
	def __init__(self):
		self.dark_ones_own_luck = False
		self.hurl_through_hell = False
		self.fiend_options = {}
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

	def create_fiend_options(self):
		self.fiend_options['0'] = "[9]: Use Dark One's Own Luck\n" + "[10]: Reset Dark One's Own Luck\n" + \
					"[11]: Use Hurl Through Hell\n" + "[12]: Reset Hurl Through Hell\n" + \
					"[13]: Change Level\n" + "[14]: Exit\n"

		self.fiend_options['9'] = self.use_dark_ones_own_luck
		self.fiend_options['10'] = self.reset_dark_ones_own_luck
		self.fiend_options['11'] = self.use_hurl_through_hell
		self.fiend_options['12'] = self.reset_hurl_through_hell
		self.fiend_options['13'] = self.set_base_warlock_level
		self.fiend_options['14'] = leave

	def list_options(self):
		selection = int_checker(self.fiend_options.get("0"))
		print(selection)
		self.fiend_options["{}".format(selection)]()


class Old(Warlock):
	def __init__(self):
		self.entropic_ward = False
		self.old_options = {}
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

	def create_old_options(self):
		self.old_options['0'] = "[9]: Use Entropic Ward\n" + "[10]: Reset Entropic Ward\n" + \
					"[11]: Change Level\n" + "[12]: Exit\n"
		self.old_options['9'] = self.use_entropic_ward
		self.old_options['10'] = self.reset_entropic_ward
		self.old_options['11'] = self.set_base_warlock_level
		self.old_options['12'] = leave
		return self.old_options

	def list_options(self):
		selection = int_checker(self.old_options.get("0"))
		print(selection)
		self.old_options["{}".format(selection)]()


def merge_base_warlock_dicts(player):
	warlock_opts = player.create_warlock_options()
	merge_dicts(player.create_player_character_options(), warlock_opts)
	return warlock_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_warlock(name):
	player = create(name, Warlock)
	player.set_base_warlock_level()
	merge_base_warlock_dicts(player)
	return player


def create_archfey_warlock(name):
	player = create(name, Archfey)
	player.set_base_warlock_level()
	merge_dicts(merge_base_warlock_dicts(player), player.create_archfey_options())
	return player


def create_fiend_warlock(name):
	player = create(name, Fiend)
	player.set_base_warlock_level()
	merge_dicts(merge_base_warlock_dicts(player), player.create_fiend_options())
	return player


def create_old_warlock(name):
	player = create(name, Old)
	player.set_base_warlock_level()
	merge_dicts(merge_base_warlock_dicts(player), player.create_old_options())
	return player


def main_warlock_making(name, dictionary):
	player_subclass = input("What is their subclass?").capitalize()
	if player_subclass == "Archfey":
		p1 = create_archfey_warlock(name)
		class_options = Archfey.list_options
	elif player_subclass == "Fiend":
		p1 = create_fiend_warlock(name)
		class_options = Fiend.list_options
	elif player_subclass == "Old":
		p1 = create_old_warlock(name)
		class_options = Old.list_options
	else:
		p1 = create_warlock(name)
		class_options = Warlock.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "options": class_options}
