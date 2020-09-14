class Barbarian:

	def __init__(self, name):
		self.name = name
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

	def __init__(self, name):
		self.frenzy = 0
		Barbarian.__init__(self, name)

	def set_frenzy(self):
		self.frenzy += 1

	def get_frenzy(self):
		return self.frenzy

	def use_b_rage(self):
		self.rage -= 1
		self.frenzy += 1

	def create_berserker_barbarian(self):
		name = input("What is the barbarian's name?\n")
		level = int(input("What level is this barbarian?\n"))
		player = Berserker(str(name))
		player.set_level(level)
		player.set_rage(level)
		player.set_hit_dice(level)
		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Rage:', player.get_rage(

		), ' Hit Dice:', player.get_hit_dice(), ' Frenzy:', player.get_frenzy())
		return player


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
