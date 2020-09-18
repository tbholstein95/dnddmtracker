from Classes.subclasses.full_caster import *
druid_dict = {}

class Druid(FullCaster):
	def __init__(self):
		self.max_wild_shape = 2
		self.current_wild_shape = 2
		FullCaster.__init__(self)

	def get_max_wild_shape(self):
		return self.max_wild_shape

	def get_current_wild_shape(self):
		return self.current_wild_shape

	def set_max_wild_shape(self):
		amount = int(input("How many times can this Druid wildshape?"))
		self.max_wild_shape = amount

	def set_current_wild_shape(self):
		amount = int(input("How many times can this Druid wildshape?"))
		self.current_wild_shape = amount

	def use_wild_shape(self):
		if self.get_current_wild_shape() == 0:
			print("Cannot Wild Shape anymore til Long Rest")
			return
		else:
			self.current_wild_shape -= 1


class Land(Druid):
	def __init__(self):
		self.natural_recovery = False
		Druid.__init__(self)

	def get_natural_recovery(self):
		return self.natural_recovery

	def set_natural_recovery(self, truefalse):
		self.natural_recovery = truefalse

	def use_natural_recovery(self):
		if self.get_natural_recovery():
			print("Already used Natural Recovery this long rest")
			return
		else:
			cur_level = self.get_level()
			restore_up_to = cur_level / 2
			temp_restore_up_to = restore_up_to
			print(f"Player can restore up to {restore_up_to} combined spell slot levels")
			while temp_restore_up_to > 0:
				restoring = int(input("What level spell is player recovering? Type '0' to stop early"))
				if restoring > restore_up_to or restoring >= 6:
					print("Spell slot too great")
				if restoring == 0:
					break
				else:
					quant_restoring = int(input("How many of these spell slots?"))
					if quant_restoring * restoring > restore_up_to or quant_restoring * restoring > self.max_slots[restoring]:
						print("This is too many")
					else:
						self.current_slots[restoring] += quant_restoring
			self.set_natural_recovery(True)

	def create_Land_cleric(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Land()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(level)
		player.copy_slots(player.max_slots)

		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

	def list_land_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Wildshape\n" + (

			"[2]: Reset Wildshape\n" + "[3]: Use Natural Recovery\n" + "[4]: Reset Natural Recovery\n" +

			"[5]: Use Hit Dice\n" + "[6]: Reset Hit Dice" + "[7]: Change Level\n" + "[8]: Exit\n")))

		if selection == 1:
			self.use_wild_shape()
		elif selection == 2:
			self.set_current_wild_shape()
		elif selection == 3:
			self.use_natural_recovery()
		elif selection == 4:
			self.set_natural_recovery(False)
		elif selection == 5:
			self.use_hit_dice()
		elif selection == 6:
			amount = self.get_level()
			self.set_hit_dice(amount)
		elif selection == 7:
			self.set_level()
			level = self.get_level()
			self.set_max_list_spell_slots(level)
			self.copy_slots(self.max_slots)
		elif selection == 8:
			print("backing")
			return 0
