from Classes.playercharacter import *
barb_dict = {}


def merge_dicts(higher, deeper):
	concat_string = higher['0'] + deeper['0']
	deeper.update(higher)
	deeper['0'] = concat_string
	return deeper

class Barbarian(PlayerCharacter):

	def __init__(self):
		self.max_rage = 0
		self.rage = 0
		self.is_rage = False
		self.reckless_strikes = False
		self.default_barb_options = {}
		super().__init__()

	def get_rage(self):
		return self.rage

	def get_max_rage(self):
		return self.max_rage

	def set_rage(self, level):
		if level < 3:
			self.rage = self.max_rage = 2
		elif 3 <= level < 6:
			self.rage = self.max_rage = 3
		elif 6 <= level < 12:
			self.rage = self.max_rage = 4
		elif 12 <= level < 20:
			self.rage = 5
			self.max_rage = 5
		elif level >= 20:
			self.rage = self.max_rage = 100

	def use_rage(self):
		self.rage -= 1
		print(self.get_rage, " rages left")

	def is_rage(self):
		if not self.is_rage:
			self.is_rage = True
			self.use_rage()
		else:
			self.is_rage = False

	def get_reckless_strikes(self):
		return self.reckless_strikes

	def set_reckless_strikes(self):
		self.reckless_strikes = True

	def use_reckless_strikes(self):
		if not self.get_reckless_strikes:
			print("Used Reckless Strikes. Attacks against this character have advantage")
			self.set_reckless_strikes()
		else:
			print("Is already Recklessly Striking")

	def reset_reckless_strikes(self):
		self.reckless_strikes = False
		print("Reset Reckless Strikes")

	def create_barbarian(self, name):
		name = name
		player = Barbarian()
		player.set_level()
		player.set_rage(player.get_level())
		player.set_hit_dice(player.get_level())
		player.set_name(name)
		print("Name: " + player.get_name(), ' Level: ', player.get_level(), ' Rage: ', player.get_rage(

		), ' Hit Dice: ', player.get_hit_dice())

		return player

	def create_default_barb_options(self):
		self.default_barb_options['0'] = "[3]: Use Rage\n[4]: Use Reckless Strikes\n[5]: Reset Restless Strikes\n"
		self.default_barb_options['3'] = self.use_rage
		self.default_barb_options['4'] = self.use_reckless_strikes
		self.default_barb_options['5'] = self.reset_reckless_strikes

		return self.default_barb_options

	def set_barb_level(self):
		self.set_level()
		self.set_hit_dice(self.get_level())

	def leave(self):
		print("Leaving")
		return 0


class Berserker(Barbarian):

	def __init__(self):
		self.frenzy = 0
		self.berserker_options = {}
		super().__init__()

	def use_frenzy(self):
		self.frenzy += 1
		print("FRENZY")

	def set_frenzy(self, amount):
		self.frenzy = amount

	def get_frenzy(self):
		return self.frenzy

	def use_b_rage(self):
		self.rage -= 1

	def create_berserker_barbarian(self, name):
		name = name
		player = Berserker()
		player.set_level()
		player.set_rage(player.get_level())
		player.set_hit_dice(player.get_level())
		player.set_name(name)
		player.create_berserker_options()
		player_class = player.create_player_character_options()
		barb_opts = player.create_default_barb_options()
		merge_dicts(player_class, barb_opts)
		merge_dicts(barb_opts, player.berserker_options)
		print(player.berserker_options)

		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Rage:', player.get_rage(

		), ' Hit Dice:', player.get_hit_dice(), ' Frenzy:', player.get_frenzy())

		return player

	def create_berserker_options(self):
		# Options 3-5 taken by default barb. Don't use those as keys.
		self.berserker_options['0'] = "[6]: Use Frenzy\n[7]: Use Reckless Strikes\n[8]: Reset Reckless Strikes\n[9]: Set Barbarian Level\n[10]: Leave"
		self.berserker_options['6'] = self.use_frenzy
		self.berserker_options['7'] = self.use_reckless_strikes
		self.berserker_options['8'] = self.reset_reckless_strikes
		self.berserker_options['9'] = self.set_barb_level
		self.berserker_options['10'] = self.leave
		self.berserker_options['list'] = self.list_options

		return self.berserker_options

	def list_options(self):
		selection = int(input(self.berserker_options.get("0")))
		print(selection)
		x = self.berserker_options["{}".format(selection)]()


class AncestralGuardian(Barbarian):

	def __init__(self):
		self.consult_spirits = False
		self.ancestral_options = {}
		super().__init__()

	def get_consult_spirits(self):
		return self.consult_spirits

	def use_consult_spirits(self):
		if not self.consult_spirits:
			print("Used consult spirits")
			self.consult_spirits = True
		else:
			print("Already used Consult Spirits this rest")

	def reset_consult_spirits(self):
		if self.consult_spirits:
			print("Reset Consult Spirits")
			self.consult_spirits = False
		else:
			print("Can still use Consult Spirits this rest")

	def create_ancestral_options(self):
		self.ancestral_options['0'] = "[6]: Consult Spirits\n[7]: Reset Consult Spirits\n[8]:Set Barbarian Level\n[9]:Exit\n"
		self.ancestral_options['6'] = self.consult_spirits
		self.ancestral_options['7'] = self.reset_consult_spirits
		self.ancestral_options['8'] = self.set_barb_level
		self.ancestral_options['9'] = self.leave

	def create_ancestral_barbarian(self, name):
		name = name
		player = AncestralGuardian()
		player.set_level()
		player.set_rage(player.get_level())
		player.set_hit_dice(player.get_level())
		player.set_name(name)
		player.merge_dicts()
		print("Name: " + player.get_name(), ' Level: ', player.get_level(), ' Rage: ', player.get_rage(

		), ' Hit Dice: ', player.get_hit_dice(), 'Consult Spirits: ', player.get_consult_spirits())

		return player

	def list_options(self):
		selection = int(input(self.ancestral_options.get("0")))
		print(selection)
		x = self.ancestral_options["{}".format(selection)]()

	# def list_ancestral_options(self):
	# 	selection = int(
	# 		input("What action are you counting?\n" + "[1]: Rage \n " + "[2]: Consult Spirits \n " +
	#
	# 		      "[3]: Recklessly Strike\n" + "[4]: Reset Reckless Strike\n" + "[5]: Use Hit Dice \n " +
	#
	# 		      "[6]: Reset Hit Dice\n" + "[6]: Change Level\n" + "[7]: Exit\n"))
	#
	# 	if selection == 1:
	# 		self.use_rage()
	# 		print(self.get_rage())
	# 	elif selection == 2:
	# 		if not self.get_consult_spirits():
	# 			print("Used Consult Spirits. Cannot again until Long Rest")
	# 			self.use_consult_spirits()
	# 			print(self.get_consult_spirits)
	# 		else:
	# 			print("Already used Consult Spirits this long rest")
	# 	elif selection == 3:
	# 		self.use_reckless_strikes()
	# 	elif selection == 4:
	# 		self.reset_reckless_strikes()
	# 	elif selection == 5:
	# 		self.use_hit_dice()
	# 		print("Current hit dice: ", self.get_hit_dice())
	# 	elif selection == 6:
	# 		self.reset_current_hit_dice()
	# 	elif selection == 7:
	# 		self.set_level()
	# 		print(self.get_level())
	# 	elif selection == 8:
	# 		print("Leaving")
	# 		return

class Zealot(Barbarian):

	def __init__(self):
		self.fanatical_focus = False
		self.zealous_presence = False
		self.zealot_options = {}
		super().__init__()

	def get_fanatical_focus(self):
		return self.fanatical_focus
	
	def use_fanatical_focus(self):
		if not self.fanatical_focus:
			print("Used Fanatical Focus")
			self.fanatical_focus = True
		else:
			print("Already use Fanatical Focus this long rest")

	def reset_fanatical_focus(self):
		if self.fanatical_focus:
			print("Reset Fanatical Focus")
			self.fanatical_focus = False
		else:
			print("Can still use Fanatical Focus this long rest")
		
	def get_zealous_presence(self):
		return self.zealous_presence
	
	def use_zealous_presence(self):
		if not self.zealous_presence:
			self.zealous_presence = True
			print("Used Zealous Presence")
		else:
			print("Already used Zealous Presence this rest")

	def reset_zealous_presence(self):
		if self.zealous_presence:
			self.zealous_presence = False
			print("Reset Zealous Presence")
		else:
			print("Can still use Zealous Presence this rest")
	
	def create_zealot_options(self):
		self.zealot_options['0'] = "[6]: Use Fanatical Focus\n[7]: Reset Fanatical Focus\n[8]: Use Zealous Presence\n[9]:Reset Zealous Presence\n[10]:Set Barbarian Level\n[11]:Exit\n"
		self.zealot_options['6'] = self.use_fanatical_focus
		self.zealot_options['7'] = self.reset_fanatical_focus
		self.zealot_options['8'] = self.use_zealous_presence
		self.zealot_options['9'] = self.reset_zealous_presence
		self.zealot_options['10'] = self.set_barb_level
		self.zealot_options['11'] = self.leave

	def list_options(self):
		selection = int(input(self.zealot_options.get("0")))
		print(selection)
		x = self.zealot_options["{}".format(selection)]()

	def create_zealot_barbarian(self, name):
		name = name
		player = Zealot()
		player.set_level()
		player.set_rage(player.get_level())
		player.set_hit_dice(player.get_level())
		player.set_name(name)
		player.merge_dicts()
		print("Name: " + player.get_name(), ' Level: ', player.get_level(), ' Rage: ', player.get_rage(

		), ' Hit Dice: ', player.get_hit_dice(), 'Fanatical Focus: ', player.get_fanatical_focus(

		), 'Zealous Presence: ', player.get_zealous_presence())

		return player

	# def list_zealot_options(self):
	# 	selection = int(
	# 		input("What action are you counting?\n" + "[1]: Rage \n " + "[2]: Use Fanatical Focus \n " +
	#
	# 			"[3]: Use Zealous Presence\n " + "[4]: Recklessly Strike\n" + "[5]: Reset Reckless Strikes\n" +
	#
	# 			"[6]: Use Hit Dice \n " + "[7]: Reset Hit Dice\n" + "[7]: Change Level\n" + "[8]: Exit\n"))
	#
	# 	if selection == 1:
	# 		self.use_rage()
	# 		print(self.get_rage())
	# 	elif selection == 2:
	# 		if not self.use_fanatical_focus():
	# 			print("Used Fanatical Focus. Cannot use again until Long Rest")
	# 			self.use_fanatical_focus()
	# 			print(self.get_fanatical_focus())
	# 		else:
	# 			print("Already used Fanatical Focus this long rest")
	# 	elif selection == 3:
	# 		self.use_reckless_strikes()
	# 	elif selection == 4:
	# 		self.reset_reckless_strikes()
	# 	elif selection == 5:
	# 		if not self.use_zealous_presence():
	# 			print("Used Zealous Presence. Cannot use again until Long Rest")
	# 			self.use_zealous_presence()
	# 			print(self.get_zealous_presence())
	# 	elif selection == 6:
	# 		self.use_hit_dice()
	# 		print("Current hit dice: ", self.get_hit_dice())
	# 	elif selection == 7:
	# 		self.reset_current_hit_dice()
	# 	elif selection == 8:
	# 		self.set_level()
	# 		print(self.get_level())
	# 	elif selection == 9:
	# 		return 0


def main_barb_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Berserker":
		p1 = Berserker()
		p1 = p1.create_berserker_barbarian(name)
		# class_options = Berserker.list_berserker_options
		new_options = Berserker.list_options
	elif player_subclass == "Ancestral":
		p1 = AncestralGuardian()
		p1 = p1.create_ancestral_barbarian(name)
		# class_options = AncestralGuardian.list_ancestral_options
		new_options = AncestralGuardian.list_options
	elif player_subclass == "Zealot":
		p1 = Zealot()
		p1 = p1.create_zealot_barbarian(name)
		# class_options = Zealot.list_options
		new_options = Zealot.list_options
	else:
		p1 = Barbarian()
		p1 = p1.create_barbarian(name)
		class_options = Barbarian.list_barbarian_options
		new_options = 0

	# barb_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
	# 				 "options": class_options, "new_options": new_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}
