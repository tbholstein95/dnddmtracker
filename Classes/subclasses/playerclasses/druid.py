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

	def list_druid_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Wildshape\n" + (

			"[2]: Reset Wildshape\n" + "[3]: Use Hit Dice\n" + "[4]: Reset Hit Dice" + "[5]: Change Level\n" + "[6]: Exit\n")))

		if selection == 1:
			self.use_wild_shape()
		elif selection == 2:
			self.set_current_wild_shape()
		elif selection == 3:
			self.use_hit_dice()
		elif selection == 4:
			amount = self.get_level()
			self.set_hit_dice(amount)
		elif selection == 5:
			self.set_level()
			level = self.get_level()
			self.set_max_list_spell_slots(level)
			self.copy_slots(self.max_slots)
		elif selection == 6:
			print("backing")
			return 0


	def create_druid(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Druid()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(level)
		player.copy_slots(player.max_slots)
		player.set_hit_dice()
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player



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
					if quant_restoring * restoring > restore_up_to or quant_restoring * restoring > \
						self.max_slots[restoring]:
						print("This is too many")
					else:
						self.current_slots[restoring] += quant_restoring
			self.set_natural_recovery(True)

	def create_land_druid(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Land()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(level)
		player.copy_slots(player.max_slots)
		player.set_hit_dice(level)
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


class Moon(Druid):
	def __init__(self):
		Druid.__init__(self)

	def use_combat_wildshape_heal(self):
		to_use = int(input("What level spell slot is the player using?"))
		current_slot = self.get_current_spell_slot(to_use)
		if current_slot == 0:
			print("No remaining slots of this level")
		else:
			self.use_cur_spell_slot(to_use)

	def create_moon_druid(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Moon()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(level)
		player.copy_slots(player.max_slots)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

	def list_moon_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Wildshape\n" + (

			"[2]: Reset Wildshape\n" + "[3]: Use Combat WildShape Heal" + "[4]: Use Hit Dice\n" +
			"[5]: Reset Hit Dice" + "[6]: Change Level\n" + "[7]: Exit\n")))

		if selection == 1:
			self.use_wild_shape()
		elif selection == 2:
			self.set_current_wild_shape()
		elif selection == 3:
			self.use_combat_wildshape_heal()
		elif selection == 4:
			self.use_hit_dice()
		elif selection == 5:
			amount = self.get_level()
			self.set_hit_dice(amount)
		elif selection == 6:
			self.set_level()
			level = self.get_level()
			self.set_max_list_spell_slots(level)
			self.copy_slots(self.max_slots)
		elif selection == 7:
			print("backing")
			return 0


class Dream(Druid):
	def __init__(self):
		self.max_summer_court_dice = 0
		self.cur_summer_court_dice = 0
		self.wisdom = 0
		self.max_hidden_paths = 0
		self.current_hidden_paths = 0
		self.walker_in_dreams = False
		Druid.__init__(self)

	def set_wisdom(self):
		amount = int(input("What is this Druid's wisdom modifier?"))
		self.wisdom = amount

	def set_max_summer_court_dice(self):
		amount = self.get_level
		self.max_summer_court_dice = amount

	def set_max_hidden_paths(self):
		amount = self.get_wisdom
		self.max_hidden_paths = amount

	def set_current_summer_court_dice(self):
		amount = self.get_max_summer_court_dice()
		self.current_hidden_paths = amount

	def use_current_summer_court_dice(self, amount):
		self.cur_summer_court_dice -= amount

	def use_current_hidden_paths(self):
		self.current_hidden_paths -= 1
		print(f"Used Hidden Paths! {self.get_current_hidden_paths()} Hidden Paths left!")

	def set_current_hidden_paths(self):
		amount = self.get_max_hidden_paths
		self.current_hidden_paths = amount

	def get_wisdom(self):
		return self.wisdom

	def get_max_summer_court_dice(self):
		return self.max_summer_court_dice

	def get_max_hidden_paths(self):
		return self.max_hidden_paths

	def get_current_summer_court_dice(self):
		return self.cur_summer_court_dice

	def get_current_hidden_paths(self):
		return self.current_hidden_paths

	def use_summer_court(self):
		cur_amount = self.get_current_summer_court_dice()
		if cur_amount == 0:
			print("No more dice to spend")
			return
		else:
			amount_to_use = int(input(f"Player can use {self.get_current_summer_court_dice()}" + (

				"Summer Court Dice. How many dice did they use?")))
			self.use_current_summer_court_dice(amount_to_use)

	def use_hidden_paths(self):
		cur_amount = self.get_current_hidden_paths()
		if cur_amount == 0:
			print("Not available to use until after Long Rest")
			return
		else:
			self.use_current_hidden_paths()

	def create_dream_druid(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Dream()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(level)
		player.copy_slots(player.max_slots)
		player.set_max_hidden_paths()
		player.set_max_summer_court_dice()
		player.set_current_hidden_paths()
		player.set_current_summer_court_dice()
		player.set_wisdom()
		player.set_max_hidden_paths()
		player.set_current_hidden_paths()
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

	def list_dream_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Wildshape\n" + (

			"[2]: Reset Wildshape\n" + "[3]: Use Balm of the Summer Court\n" + "[4]: Reset Balm of the Summer court\n" +
			"[5]: Use Hidden Paths\n" + "[6]: Reset Hidden Paths" + "[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice\n" +
			"[9]: Change Level\n" + "[10]: Exit\n")))

		if selection == 1:
			self.use_wild_shape()
		elif selection == 2:
			self.set_current_wild_shape()
		elif selection == 3:
			self.use_summer_court()
		elif selection == 4:
			self.set_current_summer_court_dice()
		elif selection == 5:
			self.use_hidden_paths()
		elif selection == 6:
			self.set_current_hidden_paths()
		elif selection == 7:
			self.use_hit_dice()
		elif selection == 8:
			amount = self.get_level()
			self.set_hit_dice(amount)
		elif selection == 9:
			self.set_level()
			level = self.get_level()
			self.set_max_list_spell_slots(level)
			self.copy_slots(self.max_slots)
			self.set_wisdom()

		elif selection == 10:
			print("backing")
			return 0

class Shepherd(Druid):
	def __init__(self):
		self.spirit_totem = False
		self.faithful_summons = False
		Druid.__init__(self)

	def get_spirit_totem(self):
		return self.spirit_totem

	def get_faithful_summons(self):
		return self.faithful_summons

	def set_spirit_totem(self, truefalse):
		self.spirit_totem = truefalse

	def set_faithful_summons(self, truefalse):
		self.faithful_summons = truefalse

	def use_spirit_totem(self):
		current_spirit = self.get_spirit_totem()
		if self.get_spirit_totem:
			print("Already used this Short/Long Rest")
			return
		else:
			print("Used Spirit Totem")
			self.set_spirit_totem(True)

	def use_faithful_summons(self):
		current_faithful = self.get_faithful_summons()
		if current_faithful:
			print("Already used Faithful Summons this Long Rest")
			return
		else:
			print("Used Faithful Summons")
			self.set_faithful_summons(True)

	def create_shepherd_druid(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Shepherd()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(level)
		player.copy_slots(player.max_slots)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

	def list_shepherd_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Wildshape\n" + (

			"[2]: Reset Wildshape\n" + "[3]: Use Spirit Totem" + "[4]: Reset Spirit Totem" + "[5]: Use Faithful Summons" +
			"[6]: Reset Faithful Summons" + "[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice" + "[9]: Change Level\n" +
			"[10]: Exit\n")))

		if selection == 1:
			self.use_wild_shape()
		elif selection == 2:
			self.set_current_wild_shape()
		elif selection == 3:
			self.use_spirit_totem()
		elif selection == 4:
			self.set_spirit_totem(False)
		elif selection == 5:
			self.use_faithful_summons()
		elif selection == 6:
			self.set_faithful_summons((False))
		elif selection == 7:
			self.use_hit_dice()
		elif selection == 8:
			amount = self.get_level()
			self.set_hit_dice(amount)
		elif selection == 9:
			self.set_level()
			level = self.get_level()
			self.set_max_list_spell_slots(level)
			self.copy_slots(self.max_slots)
		elif selection == 10:
			print("backing")
			return 0
