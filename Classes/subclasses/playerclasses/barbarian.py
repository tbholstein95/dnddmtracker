from Classes.playercharacter import *
barb_dict = {}


class Barbarian(PlayerCharacter):

	def __init__(self):
		# self.name = None
		# self.level = 0
		self.max_rage = 0
		self.rage = 0
		# self.hit_dice = 0
		self.is_rage = False
		self.reckless_strikes = False
		PlayerCharacter.__init__(self)

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


class Berserker(Barbarian):

	def __init__(self):
		self.frenzy = 0
		Barbarian.__init__(self)

	def use_frenzy(self):
		self.frenzy += 1

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
		player.set_rage(self.get_level())
		player.set_hit_dice(self.get_level())
		player.set_name(name)
		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Rage:', player.get_rage(

		), ' Hit Dice:', player.get_hit_dice(), ' Frenzy:', player.get_frenzy())

		return player

	def list_berserker_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Rage \n " + "[2]: Frenzy \n " + (
			"[3]: Use Reckless Strikes\n " + "[4]: Reset Reckless Strike" + "[5]: Use Hit Dice \n " + "[6]: Change Level\n" + (
				"[7]: Exit\n"))))
		if selection == 1:
			self.use_b_rage()
			print(self.get_rage())
		elif selection == 2:
			self.use_frenzy()
			print(self.get_frenzy())
		elif selection == 3:
			self.use_reckless_strikes()
		elif selection == 4:
			self.reset_reckless_strikes()
		elif selection == 5:
			self.use_hit_dice()
			print("Current hit dice: ", self.get_hit_dice())
		elif selection == 6:
			self.set_level()
			print("Barbarian is now level ", self.get_level())
		elif selection == 7:
			print("Leaving")
			return 0


class AncestralGuardian(Barbarian):

	def __init__(self):
		self.consult_spirits = False
		Barbarian.__init__(self)

	def get_consult_spirits(self):
		return self.consult_spirits

	def use_consult_spirits(self):
		self.consult_spirits = True

	def create_ancestral_barbarian(self, name):
		name = name
		level = int(input("What level is this barbarian?\n"))
		player = AncestralGuardian()
		player.set_level(level)
		player.set_rage(level)
		player.set_hit_dice(level)
		player.set_name(name)
		print("Name: " + player.get_name(), ' Level: ', player.get_level(), ' Rage: ', player.get_rage(

		), ' Hit Dice: ', player.get_hit_dice(), 'Consult Spirits: ', player.get_consult_spirits())

		return player

	def list_ancestral_options(self):
		selection = 0
		selection = int(
			input("What action are you counting?\n" + "[1]: Rage \n " + "[2]: Consult Spirits \n " + (
				"[3]: Recklessly Strike" + "[4]: Reset Reckless Strike" + "[5]: Use Hit Dice \n " + (
					"[6]: Change Level\n" + "[7]: Exit\n"))))
		if selection == 1:
			self.use_rage()
			print(self.get_rage())

		elif selection == 2:
			if not self.get_consult_spirits():
				print("Used Consult Spirits. Cannot again until Long Rest")
				self.use_consult_spirits()
				print(self.get_consult_spirits)
			else:
				print("Already used Consult Spirits this long rest")

		elif selection == 3:
			self.use_reckless_strikes()

		elif selection == 4:
			self.reset_reckless_strikes()

		elif selection == 5:
			dice = int(input("How many dice?"))
			self.use_hit_dice(dice)
			print("Current hit dice: ", self.get_hit_dice())

		elif selection == 6:
			level = int(input("What level should this character be?"))
			self.set_level(level)
			print(self.get_level())

		elif selection == 7:
			return 0


class Zealot(Barbarian):

	def __init__(self):
		self.fanatical_focus = False
		self.zealous_presence = False
		Barbarian.__init__(self)

	def get_fanatical_focus(self):
		return self.fanatical_focus

	def use_fanatical_focus(self):
		self.fanatical_focus = True

	def get_zealous_presence(self):
		return self.zealous_presence

	def use_zealous_presence(self):
		self.fanatical_focus = True

	def create_Zealot_barbarian(self, name):
		name = name
		level = int(input("What level is this barbarian?\n"))
		player = Zealot()
		player.set_level(level)
		player.set_rage(level)
		player.set_hit_dice(level)
		player.set_name(name)
		print("Name: " + player.get_name(), ' Level: ', player.get_level(), ' Rage: ', player.get_rage(

		), ' Hit Dice: ', player.get_hit_dice(), 'Fanatical Focus: ', player.get_fanatical_focus(

		), 'Zealous Presence: ', player.get_zealous_presence())

		return player

	def list_zealot_options(self):
		selection = 0
		selection = int(
			input("What action are you counting?\n" + "[1]: Rage \n " + "[2]: Use Fanatical Focus \n " + (
				"[3]: Use Zealous Presence\n " + "[4]: Recklessly Strike" + "[5]: Reset Reckless Strikes" + (
					"[6]: Use Hit Dice \n " + "[7]: Change Level\n" + "[8]: Exit\n"))))
		if selection == 1:
			self.use_rage()
			print(self.get_rage())

		elif selection == 2:
			if not self.use_fanatical_focus():
				print("Used Fanatical Focus. Cannot use again until Long Rest")
				self.use_fanatical_focus()
				print(self.get_fanatical_focus())
			else:
				print("Already used Fanatical Focus this long rest")

		elif selection == 3:
			self.use_reckless_strikes()

		elif selection == 4:
			self.reset_reckless_strikes()

		elif selection == 5:
			if not self.use_zealous_presence():
				print("Used Zealous Presence. Cannot use again until Long Rest")
				self.use_zealous_presence()
				print(self.get_zealous_presence())

		elif selection == 6:
			dice = int(input("How many dice?"))
			self.use_hit_dice(dice)
			print("Current hit dice: ", self.get_hit_dice())

		elif selection == 7:
			level = int(input("What level should this character be?"))
			self.set_level(level)
			print(self.get_level())

		elif selection == 8:
			return 0


class Bland(Barbarian):

	def __init__(self):
		Barbarian.__init__(self)

	def create_bland_barbarian(self, name):
		name = name
		level = int(input("What level is this barbarian?\n"))
		player = Bland()
		player.set_level(level)
		player.set_rage(level)
		player.set_hit_dice(level)
		player.set_name(name)
		print("Name: " + player.get_name(), ' Level: ', player.get_level(), ' Rage: ', player.get_rage(

		), ' Hit Dice: ', player.get_hit_dice())

		return player

	def list_bland_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Rage \n " + "[2]: Recklessly Strike" + (
			"[3]: Reset Reckless Strikes" + "[4]: Use Hit Dice \n " + "[5]: Change Level\n" + "[6]: Exit\n")))
		if selection == 1:
			self.use_rage()
			print(self.get_rage())
		elif selection == 2:
			self.use_reckless_strikes()

		elif selection == 3:
			self.reset_reckless_strikes()

		elif selection == 4:
			dice = int(input("How many dice?"))
			self.use_hit_dice(dice)
			print("Current hit dice: ", self.get_hit_dice())

		elif selection == 5:
			level = int(input("What level should this character be?"))
			self.set_level(level)
			print(self.get_level())

		elif selection == 6:
			return 0


def main_barb_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Berserker":
		p1 = Berserker()
		p1 = p1.create_berserker_barbarian(name)
		class_options = Berserker.list_berserker_options
	elif player_subclass == "Ancestral":
		p1 = AncestralGuardian()
		p1 = p1.create_ancestral_barbarian(name)
		class_options = AncestralGuardian.list_ancestral_options
	elif player_subclass == "Zealot":
		p1 = Zealot()
		p1 = p1.create_Zealot_barbarian(name)
		class_options = Zealot.list_zealot_options

	else:
		p1 = Bland()
		p1 = p1.create_bland_barbarian(name)
		class_options = Bland.list_bland_options

	barb_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}
