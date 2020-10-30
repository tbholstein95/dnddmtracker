from Classes.subclasses.half_caster import *
paladin_dict = {}

class Paladin(HalfCaster):
	def __init__(self):
		self.max_divine_sense = 0
		self.current_divine_sense = 0
		self.max_lay_on_hands = 0
		self.current_lay_on_hands = 0
		self.charisma = 0
		self.channel_divinity = False
		HalfCaster.__init__(self)

	def set_charisma(self):
		char = int(input("What is this Paladin's charisma modifier?"))
		self.charisma = char

	def get_charisma(self):
		return self.charisma

	def set_max_divine_sense(self):
		char = self.get_charisma()
		self.max_divine_sense = char

	def set_current_divine_sense(self):
		self.current_divine_sense = self.max_divine_sense

	def get_current_divine_sense(self):
		return self.current_divine_sense

	def use_divine_sense(self):
		cur_divine_sense = self.get_current_divine_sense()
		if cur_divine_sense > 0:
			print("Paladin used Divine Sense")
			self.current_divine_sense -= 1
		else:
			print("Not enough points in Divine Sense left")

	def set_max_lay_on_hands_pool(self):
		cur_level = self.get_level()
		pool = 5 * cur_level
		self.max_lay_on_hands = pool

	def set_current_lay_on_hands_pool(self):
		self.current_lay_on_hands = self.max_lay_on_hands

	def get_current_lay_on_hands(self):
		return self.current_lay_on_hands

	def use_lay_on_hands_to_heal(self):
		amount = int(input("How many points would the Paladin like to use?"))
		if amount <= self.get_current_lay_on_hands():
			self.current_lay_on_hands -= amount
		else:
			print("Paladin only has {} points left".format(self.get_current_lay_on_hands()))

	def use_lay_on_hands_remove_poison(self):
		if self.get_current_lay_on_hands() >= 5:
			print("Spending 5 points to remove poison/disease")
			self.current_lay_on_hands = self.get_current_lay_on_hands() - 5
		else:
			print("Paladin only has {} points left".format(self.get_current_lay_on_hands()))


