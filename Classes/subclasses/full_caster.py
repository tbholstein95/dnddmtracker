from Classes.playercharacter import *


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

		PlayerCharacter.__init__(self)

	def set_spell_slots(self, level):
		if level == 1:
			self.max_level_one_spell_slots = 2
			self.cur_level_one_spell_slots = 2
		elif level == 2:
			self.max_level_one_spell_slots = 3
			self.cur_level_one_spell_slots = 3
		elif level >= 3:
			self.max_level_one_spell_slots = 4
			self.cur_level_one_spell_slots = 4
			self.max_level_two_spell_slots = 2
			self.cur_level_two_spell_slots = 2
			if level >= 4:
				self.max_level_two_spell_slots = 3
				self.cur_level_two_spell_slots = 3
				if level >= 5:
					self.max_level_three_spell_slots = 2
					self.cur_level_three_spell_slots = 2
					if level >= 6:
						self.max_level_three_spell_slots = 3
						self.cur_level_three_spell_slots = 3
						if level >= 7:
							self.max_level_four_spell_slots = 1
							self.cur_level_four_spell_slots = 1
							if level >= 8:
								self.max_level_four_spell_slots = 2
								self.cur_level_four_spell_slots = 2
								if level >= 9:
									self.max_level_four_spell_slots = 3
									self.cur_level_four_spell_slots = 3

									self.max_level_five_spell_slots = 1
									self.cur_level_five_spell_slots = 1

									if level >= 10:
										self.max_level_five_spell_slots = 2
										self.cur_level_five_spell_slots = 2

										if level >= 11 or level >= 12:
											self.max_level_six_spell_slots = 1
											self.cur_level_six_spell_slots = 1
											if level >= 13 or level >= 14:
												self.max_level_seven_spell_slots = 1
												self.cur_level_seven_spell_slots = 1
												if level >= 15 or level >= 16:
													self.max_level_eight_spell_slots = 1
													self.cur_level_eight_spell_slots = 1
													if level >= 17:
														self.max_level_nine_spell_slots = 1
														self.cur_level_nine_spell_slots = 1
														if level >= 18:
															self.max_level_five_spell_slots = 2
															self.cur_level_five_spell_slots = 2
															if level >= 19:
																self.max_level_six_spell_slots = 2
																self.cur_level_six_spell_slots = 2
																if level >= 20:
																	self.max_level_six_spell_slots = 2
																	self.cur_level_six_spell_slots = 2

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

	def use_cur_spell_slot(self, level):
		if level == 1:
			self.cur_level_one_spell_slots -= 1
		if level == 2:
			self.cur_level_two_spell_slots -= 1
		if level == 3:
			self.cur_level_three_spell_slots -= 1
		if level == 4:
			self.cur_level_four_spell_slots -= 1
		if level == 5:
			self.cur_level_five_spell_slots -= 1
		if level == 6:
			self.cur_level_six_spell_slots -= 1
		if level == 7:
			self.cur_level_seven_spell_slots -= 1
		if level == 8:
			self.cur_level_eight_spell_slots -= 1
		if level == 9:
			self.cur_level_nine_spell_slots -= 1

	def use_spell_slot(self):
		slot_to_use = int(input("What level spell slot is being used?"))
		current_slots = self.get_cur_spell_slot(slot_to_use)
		if current_slots == 0:
			print(f"No slots of {slot_to_use} level")
			return 0
		else:
			self.use_cur_spell_slot(slot_to_use)
			print(f"Used Level {slot_to_use} spell")

