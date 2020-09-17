bard_dict = {}

class Bard:

	def __init__(self):
		self.name = None
		self.level = 0
		self.hit_dice = 0
		self.max_level_one_spell_slots = 0
		self.max_level_two_spell_slots = 0
		self.max_level_three_spell_slots = 0
		self.max_level_four_spell_slots = 0
		self.max_level_five_spell_slots =0
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

		self.charisma = 0
		self.counter_charm = False
		self.max_bardic_inspiration = 0
		self.current_bardic_inspiration = 0

	def get_name(self):
		return self.name

	def get_level(self):
		return self.level

	def get_hit_dice(self):
		return self.hit_dice

	def get_max_bardic_inspiration(self):
		return self.max_bardic_inspiration

	def get_current_bardic_inspiration(self):
		return self.current_bardic_inspiration

	def get_charisma(self):
		return self.charisma

	def set_name(self, name):
		self.name = name

	def set_level(self, amount):
		self.level = amount

	def set_hit_dice(self, level):
		self.hit_dice = level

	def set_charisma(self, amount):
		self.charisma = amount

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

	def set_max_bardic_inspiration(self):
		cur_charisma = self.get_charisma()
		self.max_bardic_inspiration = cur_charisma

	def set_cur_bardic_inspiration(self, amount):
		self.current_bardic_inspiration = amount

	def use_bardic_inspiration(self):
		self.current_bardic_inspiration -= 1
		print("Used Bardic Inspiration!")

	def use_hit_dice(self, amount):
		self.hit_dice -= amount




class Lore(Bard):

	def __init__(self):
		self.enthralling_performance = False
		self.mantle_of_majesty = False
		self.unbreakable_majesty = False
		Bard.__init__(self)

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

	def create_lore_bard(self, name):
		name = name
		level = int(input("What level is this Bard?"))
		charisma = int(input("How much Charisma does this Bard have?"))
		player = Bard()
		player.set_level(level)
		player.set_charisma(charisma)
		player.set_name(name)

		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Bardic Inspiration:", + (
			player.get_current_bardic_inspiration(), "Charisma:", + player.get_charisma()))

		return player

	def list_lore_options(self):
		selection = 0
		selection = input("What action are you counting?\n" + "[1]: Use Bardic Inspiration\n" + (
			"[2]: Use Enthralling Performance\n" + "[3]: Use Mantle of Majesty\n" + "[4]: Use Unbreakable Majesty\n" + (
				"[5]: Use Hit Dice\n" + "[6]: Change Level\n" + "[7]: Exit")))

		if selection == 1:
			self.use_bardic_inspiration()
			print(self.get_current_bardic_inspiration(), "Current Bardic Inspiration")
		elif selection == 2:
			self.use_enthralling_performance()
			print(self.get_current_bardic_inspiration(), "Current Bardic Inspiration")
		elif selection == 3:
			self.use_mantle_of_majesty()
			print(self.mantle_of_majesty)
		elif selection == 4:
			self.use_unbreakable_majesty()
			print(self.unbreakable_majesty)
		elif selection == 5:
			dice_to_use = int(input("How many dice did Bard use?"))
			self.set_hit_dice(dice_to_use)
		elif selection == 6:
			level_should_be = int(input("What level should this Bard be now?"))
			self.set_level(level_should_be)
		elif selection == 7:
			return 0










