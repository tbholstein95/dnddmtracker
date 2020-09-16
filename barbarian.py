barb_dict = {}


class Barbarian:

	def __init__(self):
		self.name = None
		self.level = 0
		self.max_rage = 0
		self.rage = 0
		self.hit_dice = 0
		self.is_rage = False

	def get_name(self):
		return self.name

	def get_level(self):
		return self.level

	def get_rage(self):
		return self.rage

	def get_max_rage(self):
		return self.max_rage

	def get_hit_dice(self):
		return self.hit_dice

	def set_name(self, name):
		self.name = name

	def set_level(self, level):
		self.level = level
		self.set_rage(level)

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

	def set_hit_dice(self, level):
		self.hit_dice = level

	def use_hit_dice(self, amount):
		self.hit_dice -= amount

	def use_rage(self):
		self.rage -= 1

	def is_rage(self):
		if not self.is_rage:
			self.is_rage = True
			self.use_rage()
		else:
			self.is_rage = False


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
		# name = input("What is the barbarian's name?\n")
		level = int(input("What level is this barbarian?\n"))
		player = Berserker()
		player.set_level(level)
		player.set_rage(level)
		player.set_hit_dice(level)
		player.set_name(name)
		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Rage:', player.get_rage(

		), ' Hit Dice:', player.get_hit_dice(), ' Frenzy:', player.get_frenzy())

		return player


	def list_berserker_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Rage \n " + "[2]: Frenzy \n " + (
			"[3]: Use Hit Dice \n " + "[4]: Change Level\n" + "[5]: Exit\n")))
		if selection == 1:
			self.use_b_rage()
			print(self.get_rage())
		elif selection == 2:
			self.use_frenzy()
			print(self.get_frenzy())
		elif selection == 3:
			dice = int(input("How many dice?"))
			self.use_hit_dice(dice)
			print("Current hit dice: ", self.get_hit_dice())
		elif selection == 4:
			level = int(input("What level should this character be?"))
			self.set_level(level)
			print(self.get_level())
		elif selection == 5:
			return 0



class AncestralGuardian(Barbarian):

	def __init__(self, name):
		self.consult_spirits = 1
		Barbarian.__init__(self, name)

	def get_consult_spirits(self):
		return self.consult_spirits

	def set_consult_spirits(self, amount):
		self.consult_spirits = amount

	def create_ancestral_barbarian(self):
		name = input("What is the barbarian's name?\n")
		level = int(input("What level is this barbarian?\n"))
		player = AncestralGuardian(str(name))
		player.set_level(level)
		player.set_rage(level)
		player.set_hit_dice(level)
		print("Name: " + player.get_name(), ' Level: ', player.get_level(), ' Rage: ', player.get_rage(

		), ' Hit Dice: ', player.get_hit_dice(), 'Consult Spirits: ', player.get_consult_spirits())


class Zealot(Barbarian):

	def __init__(self, name):
		self.fanatical_focus = True
		self.zealous_presence = True
		Barbarian.__init__(self, name)

	def get_fanatical_focus(self):
		return self.fanatical_focus

	def set_fanatical_focus(self):
		self.fanatical_focus = False

	def get_zealous_presence(self):
		return self.zealous_presence

	def set_zealous_presence(self):
		self.fanatical_focus = True

	def create_Zealot_barbarian(self):
		name = input("What is the barbarian's name?\n")
		level = int(input("What level is this barbarian?\n"))
		player = Zealot(str(name))
		player.set_level(level)
		player.set_rage(level)
		player.set_hit_dice(level)
		print("Name: " + player.get_name(), ' Level: ', player.get_level(), ' Rage: ', player.get_rage(

		), ' Hit Dice: ', player.get_hit_dice(), 'Fanatical Focus: ', player.get_fanatical_focus(

		), 'Zealous Presence: ', player.get_zealous_presence())

def main_barb_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Berserker":
		p1 = Berserker()
		p1 = p1.create_berserker_barbarian(name)
		class_options = Berserker.list_berserker_options
	elif player_subclass == "Ancestral":
		p1 = AncestralGuardian.create_ancestral_barbarian(p1)
	elif player_subclass == "Zealot":
		p1 = Zealot.create_Zealot_barbarian(p1)



	barb_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
						 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
						 "options": class_options}
