from Classes.playercharacter import *

class HalfCaster(PlayerCharacter):
	def __init__(self):
		self.max_slots = [0] * 10
		self.current_slots = [0] * 10
		super().__init__()

	def set_max_spell_slots(self, level):
		if level == 1:
			self.max_slots[1] = 0
		if level >= 2:
			self.max_slots[1] = 2
		if level >= 3:
			self.max_slots[1] = 3
		if level >= 5:
			self.max_slots[1] = 4
			self.max_slots[2] = 2
		if level >= 7:
			self.max_slots[2] = 3
		if level >= 9:
			self.max_slots[3] = 2
		if level >= 11:
			self.max_slots[3] = 3
		if level >= 13:
			self.max_slots[4] = 1
		if level >= 15:
			self.max_slots[4] = 2
		if level >= 17:
			self.max_slots[4] = 3
			self.max_slots[5] = 1
		if level >= 19:
			self.max_slots[5] = 2
		print(self.max_slots)

	def get_max_slot_int(self, level):
		return int(self.max_slots[level])

	def set_current_spell_slots(self, player_level):
		if player_level == 1:
			print("No spells as a half caster at level 1")
		if player_level >= 2:
			self.current_slots[1] = self.get_max_slot_int(1)
		if player_level >=5:
			self.current_slots[2] = self.get_max_slot_int(2)
		if player_level >= 9:
			self.current_slots[3] = self.get_max_slot_int(3)
		if player_level >= 13:
			self.current_slots[4] = self.get_max_slot_int(4)
		if player_level >= 17:
			self.current_slots[5] = self.get_max_slot_int(5)

	def get_current_spell_slot(self, level):
		print(self.current_slots[level])
		return self.current_slots[level]

	def use_cur_spell_slot(self):
		level = int(input("What level spell slot is being used?"))
		check = self.get_current_spell_slot(level)
		if check == 0:
			print(f"Out of slots for Level {level} levels")
		else:
			self.current_slots[level] -= 1
			print(f"{self.get_current_spell_slot(level)} level {level} slots left")

	def get_all_current_spell_slots(self, level):
		print(self.current_slots[1: level])
		return self.current_slots[1:level]


