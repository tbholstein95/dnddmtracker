from Classes.playercharacter import *
monk_dict = {}


class Monk(PlayerCharacter):

	def __init__(self):
		self.max_ki_points = 0
		self.current_ki_points = 0
		self.empty_body = False
		super().__init__()

	def set_max_ki_points(self, level):
		if level > 1:
			self.max_ki_points = level

	def set_current_ki_points(self, amount):
		self.current_ki_points = amount

	def get_current_ki_points(self):
		return self.current_ki_points

	def get_max_ki_points(self):
		return self.max_ki_points

	def reset_current_ki_points(self):
		self.current_ki_points = self.max_ki_points
		print("Ki points restored to max")

	def restore_ki_points(self, amount):
		self.set_current_ki_points(self.get_current_ki_points() + amount)

	def use_empty_body(self):
		current_ki = self.get_current_ki_points()
		if current_ki - 4 <= 0:
			print("The monk only has {} ki points".format(current_ki))
		else:
			self.set_current_ki_points(current_ki - 4)
			print("Monk used empty body")

	def use_ki_point(self):
		current_ki = self.get_current_ki_points()
		ki_to_use = int(input("How many ki points is the monk using?"))
		if current_ki - ki_to_use <= 0:
			print("The monk has 0 ki points")
		else:
			self.set_current_ki_points(current_ki - ki_to_use)
			print("Used 1 Ki Point")

	def create_basic_monk(self, name):
		name = name
		level = int(input("What level is this Monk?\n"))
		player = Monk()
		player.set_level()
		player.set_hit_dice(level)
		player.set_name(name)
		player.set_max_ki_points(level)
		player.set_current_ki_points(player.get_max_ki_points())
		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Hit Dice:', player.get_hit_dice(),)

		return player

	def list_basic_monk_options(self):
		selection = int(input("What action are you counting?\n" + "[1]: Use Ki Point \n " + "[2]: Restore Ki \n " + (
			"[3]: Use Empty Body \n " + "[4]: Use Hit Dice \n " + "[5]: Change Level\n" + (
				"[6]: Reset Hit Dice" + "[7]:Reset Ki" + "[8]: Exit\n"))))
		if selection == 1:
			self.use_ki_point()
		elif selection == 2:
			self.reset_current_ki_points()
		elif selection == 3:
			self.use_empty_body()
		elif selection == 4:
			self.use_hit_dice()
			print("Current hit dice: ", self.get_hit_dice())
		elif selection == 5:
			level = self.set_level()
			self.set_max_ki_points(level)
			self.set_hit_dice(level)
			print(self.get_level())
		elif selection == 6:
			self.reset_current_hit_dice()
		elif selection == 7:
			self.reset_current_ki_points()
		elif selection == 8:
			return 0


class OpenHand(Monk):

	def __init__(self):
		self.wholeness = False
		super().__init__()

	def use_quivering_palm(self):
		current_ki = self.get_current_ki_points()
		if current_ki - 3 <= 0:
			print("The monk only has {} ki points".format(current_ki))
		else:
			self.set_current_ki_points(current_ki - 3)
			print("Monk used Quivering Palm")

	def use_wholeness(self):
		if not self.wholeness:
			self.wholeness = True
			print("Used wholeness. Can't use again til next long rest")
		else:
			print("Monk already used wholeness this long rest")

	def create_open_hand_monk(self, name):
		name = name
		level = int(input("What level is this Monk?\n"))
		player = OpenHand()
		player.set_level()
		player.set_hit_dice(level)
		player.set_name(name)
		player.set_max_ki_points(level)
		player.set_current_ki_points(self.get_max_ki_points())
		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Hit Dice:', player.get_hit_dice(),)

		return player

	def list_open_hand_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Ki Point \n " + "[2]: Restore Ki \n " +

			"[3]: Use Empty Body \n " + "[4]: Use Quivering Palm" +"[5]: Use Wholeness" +

			"[6]: Use Hit Dice\n" + "[7]: Change Level\n" + "[8]: Reset Hit Dice" + "[9]:Reset Ki" + "[10]: Exit\n"))

		if selection == 1:
			self.use_ki_point()
		elif selection == 2:
			self.reset_current_ki_points()
		elif selection == 3:
			self.use_empty_body()
		elif selection == 4:
			self.use_quivering_palm()
		elif selection == 5:
			self.use_wholeness()
		elif selection == 6:
			self.use_hit_dice()
			print("Current hit dice: ", self.get_hit_dice())
		elif selection == 7:
			level = self.set_level()
			self.set_max_ki_points(level)
			self.set_hit_dice(level)
			print(self.get_level())
		elif selection == 8:
			self.reset_current_hit_dice()
		elif selection == 9:
			self.reset_current_ki_points()
		elif selection == 10:
			return 0

class FourElements(Monk):
	def __init__(self):
		super().__init__()

	def use_elemental_discipline(self, amount):
		maximum_ki_expend = ''
		if 5 <= self.get_level() <= 8:
			maximum_ki_expend = 3
		elif 9 <= self.get_level() <= 12:
			maximum_ki_expend = 4
		elif 13 <= self.get_level() <= 16:
			maximum_ki_expend = 5
		elif 17 <= self.get_level() <= 20:
			maximum_ki_expend = 6

		spell_level = int(input("What level are they casting this spell at?"))
		if amount + spell_level > maximum_ki_expend:
			print("Monk can't spend that much at once")
		else:
			self.set_current_ki_points(self.get_current_ki_points() - (amount + spell_level))
			print("Monk cast the spell for {} ki points".format(amount + spell_level))

	def create_four_elements_monk(self, name):
		name = name
		level = int(input("What level is this Monk?\n"))
		player = OpenHand()
		player.set_level()
		player.set_hit_dice(level)
		player.set_name(name)
		player.set_max_ki_points(level)
		player.set_current_ki_points(player.get_max_ki_points())
		print('Name:' + player.get_name(), ' Level:', player.get_level(), ' Hit Dice:', player.get_hit_dice(),)

		return player

	def list_four_elements_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Ki Point\n" + "[2]: Restore Ki\n" +

				"[3]: Use Empty Body \n " + "[4]: Use Quivering Palm" + "[5]: Use Hit Dice \n " + "[6]: Change Level\n" +

				"[7]: Reset Hit Dice" + "[8]:Reset Ki" + "[9]: Exit\n"))

		if selection == 1:
			self.use_ki_point()
		elif selection == 2:
			self.reset_current_ki_points()
		elif selection == 3:
			self.use_empty_body()
		elif selection == 4:
			self.use_elemental_discipline()
		elif selection == 5:
			self.use_hit_dice()
			print("Current hit dice: ", self.get_hit_dice())
		elif selection == 6:
			level = self.set_level()
			self.set_max_ki_points(level)
			self.set_hit_dice(level)
			print(self.get_level())
		elif selection == 7:
			self.reset_current_hit_dice()
		elif selection == 8:
			self.reset_current_ki_points()
		elif selection == 9:
			return 0


def main_monk_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Open Hand":
		p1 = OpenHand()
		p1 = p1.create_open_hand_monk(name)
		class_options = OpenHand.list_open_hand_options
	elif player_subclass == "Four Elements":
		p1 = FourElements()
		p1 = p1.create_four_elements_monk(name)
		class_options = FourElements.list_four_elements_options
	else:
		p1 = Monk()
		p1 = p1.create_basic_monk(name)
		class_options = Monk.list_basic_monk_options

	monk_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}
