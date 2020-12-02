from Classes.playercharacter import *
full_caster_dict = {}

class FullCaster(PlayerCharacter):
	def __init__(self):
		self.max_slots = [0] * 10
		self.current_slots = [0] * 10
		super().__init__()

	def set_max_list_spell_slots(self, level):
		if level >= 1:
			self.max_slots[1] = 2
		if level >= 2:
			self.max_slots[1] = 3
		if level >= 3:
			self.max_slots[1] = 4
			self.max_slots[2] = 2
		if level >= 4:
			self.max_slots[2] = 3
		if level >= 5:
			self.max_slots[3] = 2
		if level >= 6:
			self.max_slots[3] = 3
		if level >= 7:
			self.max_slots[4] = 1
		if level >= 8:
			self.max_slots[4] = 2
		if level >= 9:
			self.max_slots[4] = 3
			self.max_slots[5] = 1
		if level >= 10:
			self.max_slots[5] = 2
		if level >= 11:
			self.max_slots[6] = 1
		if level >= 13:
			self.max_slots[7] = 1
		if level >= 15:
			self.max_slots[8] = 1
		if level >= 17:
			self.max_slots[9] = 1
		if level >= 18:
			self.max_slots[5] = 2
		if level >= 19:
			self.max_slots[6] = 2

	def set_current_list_spell_slots(self):
		current_level = self.get_level()
		if current_level >= 1:
			self.current_slots[1] = self.get_max_slot_int(1)
		if current_level >= 3:
			self.current_slots[2] = self.get_max_slot_int(2)
		if current_level >= 5:
			self.current_slots[3] = self.get_max_slot_int(3)
		if current_level >= 7:
			self.current_slots[4] = self.get_max_slot_int(4)
		if current_level >= 9:
			self.current_slots[5] = self.get_max_slot_int(5)
		if current_level >= 11:
			self.current_slots[6] = self.get_max_slot_int(6)
		if current_level >= 13:
			self.current_slots[7] = self.get_max_slot_int(7)
		if current_level >= 15:
			self.current_slots[8] = self.get_max_slot_int(8)
		if current_level >= 17:
			self.current_slots[9] = self.get_max_slot_int(9)

	def get_max_slot_int(self, level):
		return int(self.max_slots[level])

	def get_current_spell_slot(self, level):
		print(self.current_slots[level])
		return self.current_slots[level]

	def get_all_current_spell_slots(self, level):
		print(self.current_slots[1: level])
		return self.current_slots[1:level]

	def use_cur_spell_slot(self):
		level = int(input("What level spell slot is being used?"))
		check = self.get_current_spell_slot(level)
		if check == 0:
			print(f"Out of slots for Level {level} levels")
		else:
			self.current_slots[level] -= 1
			print(f"{self.get_current_spell_slot(level)} level {level} slots left")

	def copy_slots(self, li1):
		li_copy = li1[:]
		return li_copy

	def add_spell_slot(self, level):
		if level == 1:
			self.current_slots[1] += 1
		elif level == 2:
			self.current_slots[2] += 1
		elif level == 3:
			self.current_slots[3] += 1
		elif level == 4:
			self.current_slots[4] += 1
		elif level == 5:
			self.current_slots[5] += 1
		elif level == 6:
			self.current_slots[6] += 1
		elif level == 7:
			self.current_slots[7] += 1
		elif level == 8:
			self.current_slots[8] += 1
		elif level == 9:
			self.current_slots[9] += 1

	def create_fullcaster_character_options(self):
		# Player class uses 1 & 2. Fill out 0 for merging later.  Starts at 3
		full_caster_dict['0'] = "[3]: Cast Spell\n[4]: Reset Spells\n"
		full_caster_dict['3'] = self.use_cur_spell_slot
		full_caster_dict['4'] = self.set_current_list_spell_slots
		return full_caster_dict

	def merge_base_and_fullspell_options(self):
		player_class = self.create_player_character_options()
		spell_opts = self.create_fullcaster_character_options()
		merge_dicts(player_class, spell_opts)
		return spell_opts

	def change_fullcaster_level(self):
		self.base_change_level()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()
