from Classes.playercharacter import *

#TODO: Rework as well as half-caster
class FullCaster(PlayerCharacter):
	def __init__(self):
		self.max_level_one_spell_slots = 0
		self.max_level_two_spell_slots = 0
		self.max_level_three_spell_slots = 0
		self.max_level_four_spell_slots = 0
		self.max_level_five_spell_slots = 0
		self.max_level_six_spell_slots = 0
		self.max_level_seven_spell_slots = 0
		self.max_level_eight_spell_slots = 0
		self.max_level_nine_spell_slots = 0

		self.cur_level_one_spell_slots = 0
		self.cur_level_two_spell_slots = 0
		self.cur_level_three_spell_slots = 0
		self.cur_level_four_spell_slots = 0
		self.cur_level_five_spell_slots = 0
		self.cur_level_six_spell_slots = 0
		self.cur_level_seven_spell_slots = 0
		self.cur_level_eight_spell_slots = 0
		self.cur_level_nine_spell_slots = 0

		self.max_slots = [0] * 21
		self.current_slots = [0] * 21

		super().__init__()

	def set_max_list_spell_slots(self, level):
		if level == 1:
			self.max_slots[1] = 2
		if level == 2:
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




	# def set_spell_slots(self, level):
	# 	if level >= 1:
	# 		self.max_level_one_spell_slots = 2
	# 		self.cur_level_one_spell_slots = 2
	# 	if level >= 2:
	# 		self.max_level_one_spell_slots = 3
	# 		self.cur_level_one_spell_slots = 3
	# 	if level >= 3:
	# 		self.max_level_one_spell_slots = 4
	# 		self.cur_level_one_spell_slots = 4
	# 		self.max_level_two_spell_slots = 2
	# 		self.cur_level_two_spell_slots = 2
	# 	if level >= 4:
	# 		self.max_level_two_spell_slots = 3
	# 		self.cur_level_two_spell_slots = 3
	# 	if level >= 5:
	# 		self.max_level_three_spell_slots = 2
	# 		self.cur_level_three_spell_slots = 2
	# 	if level >= 6:
	# 		self.max_level_three_spell_slots = 3
	# 		self.cur_level_three_spell_slots = 3
	# 	if level >= 7:
	# 		self.max_level_four_spell_slots = 1
	# 		self.cur_level_four_spell_slots = 1
	# 	if level >= 8:
	# 		self.max_level_four_spell_slots = 2
	# 		self.cur_level_four_spell_slots = 2
	# 	if level >= 9:
	# 		self.max_level_four_spell_slots = 3
	# 		self.cur_level_four_spell_slots = 3
	#
	# 		self.max_level_five_spell_slots = 1
	# 		self.cur_level_five_spell_slots = 1
	#
	# 	if level >= 10:
	# 		self.max_level_five_spell_slots = 2
	# 		self.cur_level_five_spell_slots = 2
	#
	# 	if level >= 11 or level >= 12:
	# 		self.max_level_six_spell_slots = 1
	# 		self.cur_level_six_spell_slots = 1
	# 	if level >= 13 or level >= 14:
	# 		self.max_level_seven_spell_slots = 1
	# 		self.cur_level_seven_spell_slots = 1
	# 	if level >= 15 or level >= 16:
	# 		self.max_level_eight_spell_slots = 1
	# 		self.cur_level_eight_spell_slots = 1
	# 	if level >= 17:
	# 		self.max_level_nine_spell_slots = 1
	# 		self.cur_level_nine_spell_slots = 1
	# 	if level >= 18:
	# 		self.max_level_five_spell_slots = 2
	# 		self.cur_level_five_spell_slots = 2
	# 	if level >= 19:
	# 		self.max_level_six_spell_slots = 2
	# 		self.cur_level_six_spell_slots = 2
	# 	if level >= 20:
	# 		self.max_level_six_spell_slots = 2
	# 		self.cur_level_six_spell_slots = 2

	def get_cur_spell_slot(self, level):
		if level == 1:
			return self.cur_level_one_spell_slots
		if level == 2:
			return self.cur_level_two_spell_slots
		if level == 3:
			return self.cur_level_three_spell_slots
		if level == 4:
			return self.cur_level_four_spell_slots
		if level == 5:
			return self.cur_level_five_spell_slots
		if level == 6:
			return self.cur_level_six_spell_slots
		if level == 7:
			return self.cur_level_seven_spell_slots
		if level == 8:
			return self.cur_level_eight_spell_slots
		if level == 9:
			return self.cur_level_nine_spell_slots

	# def use_cur_spell_slot(self, level):
	# 	if level == 1:
	# 		self.cur_level_one_spell_slots -= 1
	# 	if level == 2:
	# 		self.cur_level_two_spell_slots -= 1
	# 	if level == 3:
	# 		self.cur_level_three_spell_slots -= 1
	# 	if level == 4:
	# 		self.cur_level_four_spell_slots -= 1
	# 	if level == 5:
	# 		self.cur_level_five_spell_slots -= 1
	# 	if level == 6:
	# 		self.cur_level_six_spell_slots -= 1
	# 	if level == 7:
	# 		self.cur_level_seven_spell_slots -= 1
	# 	if level == 8:
	# 		self.cur_level_eight_spell_slots -= 1
	# 	if level == 9:
	# 		self.cur_level_nine_spell_slots -= 1

	# def use_cur_spell_slot(self, level):
	# 	check = self.get_current_spell_slot(level)
	# 	if check == 0:
	# 		print(f"Out of slots for Level {level} levels")
	# 	else:
	# 		self.current_slots[level] -= 1
	# 		print(f"{self.get_current_spell_slot(level)} level {level} slots left")
	#
	# def use_spell_slot(self):
	# 	slot_to_use = int(input("What level spell slot is being used?"))
	# 	current_slots = self.get_cur_spell_slot(slot_to_use)
	# 	if current_slots == 0:
	# 		print(f"No slots of {slot_to_use} level")
	# 		return 0
	# 	else:
	# 		self.use_cur_spell_slot(slot_to_use)
	# 		print(f"Used Level {slot_to_use} spell")
	# 	return slot_to_use

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
			self.cur_level_one_spell_slots += 1
		elif level == 2:
			self.cur_level_two_spell_slots += 1
		elif level == 3:
			self.cur_level_three_spell_slots += 1
		elif level == 4:
			self.cur_level_four_spell_slots += 1
		elif level == 5:
			self.cur_level_five_spell_slots += 1
		elif level == 6:
			self.cur_level_six_spell_slots += 1
		elif level == 7:
			self.cur_level_seven_spell_slots += 1
		elif level == 8:
			self.cur_level_eight_spell_slots += 1
		elif level == 9:
			self.cur_level_nine_spell_slots += 1
