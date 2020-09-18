from Classes.playercharacter import *
barb_dict = {}


class Fighter(PlayerCharacter):
	def __init__(self):
		self.second_wind = False
		self.action_surge = False
		self.max_indomitable = 0
		self.current_indomitable = 0
		PlayerCharacter.__init__(self)

	def set_second_wind(self, truefalse):
		self.second_wind = truefalse

	def set_action_surge(self, truefalse):
		self.action_surge = truefalse


	def set_max_indomitable(self):
		level = self.get_level()
		if level >= 9:
			self.max_indomitable = 1
		elif level >= 13:
			self.max_indomitable = 2
		elif level >= 17:
			self.max_indomitable = 3

	def set_current_indomitable(self):
		amount = self.get_max_indomitable()
		self.current_indomitable = amount

	def use_current_indomitable(self):
		self.current_indomitable -= 1

	def get_second_wind(self):
		return self.second_wind

	def get_action_surge(self):
		return self.action_surge

	def get_max_indomitable(self):
		return self.max_indomitable

	def get_current_indomitable(self):
		return self.current_indomitable

	def use_indomitable(self):
		current = self.get_current_indomitable()
		if current == 0:
			print("Out of uses until the next Long Rest")
			return
		else:
			self.use_current_indomitable()

	def use_second_wind(self):
		if self.get_second_wind():
			print("Cannot use Second Wind until short or long rest")
			return
		else:
			print("Used Second Wind")
			self.set_second_wind(True)

	def use_action_surge(self):
		if self.get_action_surge:
			print("Cannot use Action Surge until short or long rest")
			return
		else:
			print("Used Action Surge")
			self.set_action_surge(True)



class BattleMaster(Fighter):
	def __init__(self):
		self.max_superiority_dice = 0
		self.current_superiority_dice = 0
		Fighter.__init__(self)

	def set_max_superiority_dice(self):
		level = self.get_level()
		if level < 7:
			self.max_superiority_dice = 4
		elif level >= 7:
			self.max_superiority_dice = 5
		elif level >= 15:
			self.max_superiority_dice = 6

	def set_current_superiority_dice(self):
		amount = self.get_max_superiority_dice()
		self.current_superiority_dice = amount

	def get_max_superiority_dice(self):
		return self.get_max_superiority_dice()

	def get_current_superiority_dice(self):
		return self.current_superiority_dice

	def use_current_superiority_dice(self):
		self.current_superiority_dice -= 1

	def use_superiority_dice(self):
		current_dice = self.get_current_superiority_dice()
		if current_dice == 0:
			print("Not enough Superiority Dice remaining")
			return
		else:
			self.use_current_superiority_dice()

	def create_battlemaster_fighter(self, name):
		name = name
		level = int(input("What level is this Barbarian?\n"))
		player = BattleMaster()
		player.set_level()
		player.set_hit_dice(level)
		player.set_name(name)
		player.set_max_superiority_dice()
		player.set_current_superiority_dice()
		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Hit Dice:', player.get_hit_dice())

		return player

	def list_berserker_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Second Wind\n" + "[2]: Reset Second Wind \n " + (
			"[3]: Use Action Surge\n " + "[4]: Reset Action Surge" + "[5]: Use Indomitable" + "[6]: Reset Indomitable" +
			"[7]: Use Hit Dice \n " + "[8]: Reset Hit Dice" + "[9]: Change Level\n" + "[10]: Exit\n")))
		if selection == 1:
			self.use_second_wind()
		elif selection == 2:
			self.set_second_wind(True)
		elif selection == 3:
			self.use_action_surge()
		elif selection == 4:
			self.set_action_surge(True)
		elif selection == 5:
			self.use_indomitable()
		elif selection == 6:
			self.set_current_indomitable()
		elif selection == 7:
			dice = int(input("How many dice?"))
			self.use_hit_dice(dice)
			print("Current hit dice: ", self.get_hit_dice())
		elif selection == 8:
			amount = self.get_level()
			self.set_hit_dice(amount)
		elif selection == 9:
			self.set_level()
			amount = self.get_level()
			self.set_hit_dice(amount)
		elif selection == 10:
			return 0

class Eldritch(Fighter):



