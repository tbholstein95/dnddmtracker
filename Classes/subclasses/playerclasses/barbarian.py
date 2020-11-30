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

	def set_barb_level(self):
		self.set_level()
		self.set_hit_dice(self.get_level())

	def show_options(self):
		selection = int(input(self.new_options.get("0")))
		print(selection)
		self.new_options["{}".format(selection)]()


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
					"[9]: Set Barbarian Level\n[10]: Leave"
		self.berserker_options['6'] = self.use_frenzy
		self.berserker_options['7'] = self.use_reckless_strikes
		self.berserker_options['8'] = self.reset_reckless_strikes
		self.berserker_options['9'] = self.set_barb_level
		self.berserker_options['10'] = leave()
		self.berserker_options['list'] = self.list_options

		return self.berserker_options

	def list_options(self):
		selection = int(input(self.berserker_options.get("0")))
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
		self.ancestral_options['8'] = self.set_barb_level
		self.ancestral_options['9'] = leave()

	def list_options(self):
		selection = int(input(self.ancestral_options.get("0")))
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
		self.zealot_options['10'] = self.set_barb_level
		self.zealot_options['11'] = leave()

	def list_options(self):
		selection = int(input(self.zealot_options.get("0")))
		print(selection)
		self.zealot_options["{}".format(selection)]()


def create(name, subclass):
	name = name
	player = subclass()
	player.set_level()
	player.set_rage(player.get_level())
	player.set_hit_dice(player.get_level())
	player.set_name(name)
	return player


def create_barbarian(name):
	player = create(name, Barbarian)
	player_class = player.create_player_character_options()
	barb_opts = player.create_default_barb_options()
	merge_dicts(player_class, barb_opts)
	return player


def create_berserker_barbarian(name):
	player = create(name, Berserker)
	player.create_berserker_options()
	player_class = player.create_player_character_options()
	barb_opts = player.create_default_barb_options()
	merge_dicts(player_class, barb_opts)
	merge_dicts(barb_opts, player.berserker_options)
	player.new_options = barb_opts.copy()
	print(player.new_options)
	return player


def create_ancestral_barbarian(name):
	player = create(name, AncestralGuardian)
	player.create_ancestral_options()
	player_class = player.create_player_character_options()
	barb_opts = player.create_default_barb_options()
	merge_dicts(player_class, barb_opts)
	merge_dicts(barb_opts, player.ancestral_options)
	return player


def create_zealot_barbarian(name):
	player = create(name, Zealot)
	player.create_zealot_options()
	player_class = player.create_player_character_options()
	barb_opts = player.create_default_barb_options()
	merge_dicts(player_class, barb_opts)
	merge_dicts(barb_opts, player.zealot_options)
	return player


def main_barb_making(name, dictionary):
	player_subclass = input("What is their subclass?").capitalize()
	if player_subclass == "Berserker":
		p1 = create_berserker_barbarian(name)
		new_options = Berserker.list_options
	elif player_subclass == "Ancestral":
		p1 = create_ancestral_barbarian(name)
		new_options = AncestralGuardian.list_options
	elif player_subclass == "Zealot":
		p1 = create_zealot_barbarian(name)
		new_options = Zealot.list_options
	else:
		p1 = create_barbarian(name)
		new_options = 0

	player = p1

	print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Rage:', player.get_rage,
		' Hit Dice:', player.get_hit_dice())

	# barb_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
	# 				 "options": class_options, "new_options": new_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}
