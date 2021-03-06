from Classes.playercharacter import *
barb_dict = {}


class Barbarian(PlayerCharacter):

	def __init__(self):
		self.max_rage = 0
		self.rage = 0
		self.is_rage = False
		self.reckless_strikes = False
		self.default_barb_options = {}
		self.new_options = {}
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

	def create_default_barb_options(self):
		self.default_barb_options['0'] = "[3]: Use Rage\n[4]: Use Reckless Strikes\n[5]: Reset Restless Strikes\n"
		self.default_barb_options['3'] = self.use_rage
		self.default_barb_options['4'] = self.use_reckless_strikes
		self.default_barb_options['5'] = self.reset_reckless_strikes
		return self.default_barb_options

	def change_barb_level(self):
		self.set_level()
		self.set_rage(self.get_level())
		self.set_max_hit_dice(self.get_level())
		self.set_hit_dice(self.get_level())

	def list_options(self):
		selection = int(input(self.default_barb_options.get("0")))
		print(selection)
		self.default_barb_options["{}".format(selection)]()


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

	def create_berserker_options(self):
		# Options 3-5 taken by default barb. Don't use those as keys.
		self.berserker_options['0'] = "[6]: Use Frenzy\n[7]: Use Reckless Strikes\n[8]: Reset Reckless Strikes\n" \
					"[9]: Set Barbarian Level\n[10]: Leave\n"
		self.berserker_options['6'] = self.use_frenzy
		self.berserker_options['7'] = self.use_reckless_strikes
		self.berserker_options['8'] = self.reset_reckless_strikes
		self.berserker_options['9'] = self.change_barb_level
		self.berserker_options['10'] = leave()
		return self.berserker_options

	def list_options(self):
		selection = int_checker(self.berserker_options.get("0"))
		print(selection)
		self.berserker_options["{}".format(selection)]()


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
		self.ancestral_options['8'] = self.change_barb_level
		self.ancestral_options['9'] = leave()
		return self.ancestral_options

	def list_options(self):
		selection = int_checker(self.ancestral_options.get("0"))
		print(selection)
		self.ancestral_options["{}".format(selection)]()


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
		self.zealot_options['0'] = "[6]: Use Fanatical Focus\n[7]: Reset Fanatical Focus\n[8]: Use Zealous Presence\n" \
					"[9]:Reset Zealous Presence\n[10]:Set Barbarian Level\n[11]:Exit\n"
		self.zealot_options['6'] = self.use_fanatical_focus
		self.zealot_options['7'] = self.reset_fanatical_focus
		self.zealot_options['8'] = self.use_zealous_presence
		self.zealot_options['9'] = self.reset_zealous_presence
		self.zealot_options['10'] = self.change_barb_level
		self.zealot_options['11'] = leave()
		return self.zealot_options

	def list_options(self):
		selection = int_checker(self.zealot_options.get("0"))
		print(selection)
		self.zealot_options["{}".format(selection)]()


def merge_base_barb_dicts(player):
	player_class = player.create_player_character_options()
	barb_opts = player.create_default_barb_options()
	merge_dicts(player_class, barb_opts)
	return barb_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_barbarian(name):
	player = create(name, Barbarian)
	player.change_barb_level()
	merge_base_barb_dicts(player)
	return player


def create_berserker_barbarian(name):
	player = create(name, Berserker)
	player.change_barb_level()
	player.create_berserker_options()
	merge_dicts(merge_base_barb_dicts(player), player.berserker_options)
	return player


def create_ancestral_barbarian(name):
	player = create(name, AncestralGuardian)
	player.change_barb_level()
	player.create_ancestral_options()
	merge_dicts(merge_base_barb_dicts(player), player.ancestral_options)
	return player


def create_zealot_barbarian(name):
	player = create(name, Zealot)
	player.change_barb_level()
	player.create_zealot_options()
	merge_dicts(merge_base_barb_dicts(player), player.zealot_options)
	return player


def main_barb_making(name, dictionary):
	player_subclass = int_checker("What is their subclass?\n[1]: Berserker\n[2]: Ancestral\n[3]:Zealot[4]: Other\n")
	if player_subclass == "1":
		p1 = create_berserker_barbarian(name)
		new_options = Berserker.list_options
	elif player_subclass == "2":
		p1 = create_ancestral_barbarian(name)
		new_options = AncestralGuardian.list_options
	elif player_subclass == "3":
		p1 = create_zealot_barbarian(name)
		new_options = Zealot.list_options
	else:
		p1 = create_barbarian(name)
		new_options = Barbarian.list_options

	print('Name:' + p1.get_name(), ' Level:', p1.get_level(), ' Rage:', p1.get_rage, ' Hit Dice:', p1.get_hit_dice())

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}
