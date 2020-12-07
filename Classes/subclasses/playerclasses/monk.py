from Classes.playercharacter import *
monk_dict = {}


class Monk(PlayerCharacter):

	def __init__(self):
		self.max_ki_points = 0
		self.current_ki_points = 0
		self.empty_body = False
		self.monk_options = {}
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
		ki_to_use = int_checker("How many ki points is the monk using?")
		if current_ki - ki_to_use <= 0:
			print("The monk has 0 ki points")
		else:
			self.set_current_ki_points(current_ki - ki_to_use)
			print("Used 1 Ki Point")

	def create_basic_monk_options(self):
		self.monk_options['0'] = "[3]: Use Ki Point \n " + "[4]: Restore Ki \n " + "[5]: Use Empty Body \n "
		self.monk_options['3'] = self.use_ki_point
		self.monk_options['4'] = self.reset_current_ki_points
		self.monk_options['5'] = self.use_empty_body
		return self.monk_options

	def change_monk_level(self):
		self.base_change_level()
		self.set_max_ki_points(self.get_level())
		self.reset_current_ki_points()

	def list_options(self):
		selection = int_checker(self.monk_options.get("0"))
		print(selection)
		self.monk_options["{}".format(selection)]()


class OpenHand(Monk):

	def __init__(self):
		self.wholeness = False
		self.open_hand_options = {}
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

	def reset_wholeness(self):
		if self.wholeness:
			print("Reset Wholeness")
			self.wholeness = False
		else:
			print("Can still use Wholeness this rest period")

	def create_open_hand_options(self):
		self.open_hand_options['0'] = "[4]: Use Quivering Palm" + "[5]: Use Wholeness" + "[6]: Reset Wholeness" + \
					"[7]: Change Level\n" + "[10]: Exit\n"
		self.open_hand_options['4'] = self.use_quivering_palm
		self.open_hand_options['5'] = self.use_wholeness
		self.open_hand_options['6'] = self.reset_wholeness
		self.open_hand_options['7'] = self.change_monk_level
		self.open_hand_options['8'] = leave
		return self.open_hand_options

	def list_options(self):
		selection = int_checker(self.open_hand_options.get("0"))
		print(selection)
		self.open_hand_options["{}".format(selection)]()


class FourElements(Monk):
	def __init__(self):
		self.elements_options = {}
		super().__init__()

	def use_elemental_discipline(self):
		amount = int_checker("How many ki points?")
		maximum_ki_expend = 0
		if 5 <= self.get_level() <= 8:
			maximum_ki_expend = 3
		elif 9 <= self.get_level() <= 12:
			maximum_ki_expend = 4
		elif 13 <= self.get_level() <= 16:
			maximum_ki_expend = 5
		elif 17 <= self.get_level() <= 20:
			maximum_ki_expend = 6

		spell_level = int_checker("What level are they casting this spell at?")
		if amount + spell_level > maximum_ki_expend:
			print("Monk can't spend that much at once")
		else:
			self.set_current_ki_points(self.get_current_ki_points() - (amount + spell_level))
			print("Monk cast the spell for {} ki points".format(amount + spell_level))

	def create_four_elements_options(self):
		self.elements_options['0'] = "[4]: Use Elemental Discipline" + "[5]: Change Level" + "[6]: Exit\n"
		self.elements_options['4'] = self.use_elemental_discipline
		self.elements_options['5'] = self.change_monk_level
		self.elements_options['6'] = leave
		return self.elements_options

	def list_options(self):
		selection = int_checker(self.elements_options.get("0"))
		print(selection)
		self.elements_options["{}".format(selection)]()


def merge_base_monk_dicts(player):
	player_class = player.create_player_character_options()
	monk_opts = player.create_monk_options()
	merge_dicts(player_class, monk_opts)
	return monk_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_basic_monk(name):
	player = create(name, Monk)
	player.change_monk_level()
	merge_base_monk_dicts(player)
	return player


def create_open_hand_monk(name):
	player = create(name, OpenHand)
	player.change_monk_level()
	merge_dicts(merge_base_monk_dicts(player), player.create_open_hand_options())
	return player


def create_four_elements_monk(name):
	player = create(name, FourElements)
	player.change_monk_level()
	merge_dicts(merge_base_monk_dicts(player), player.create_four_elements_options())
	return player


def main_monk_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?").capitalize()
	if player_subclass == "Open Hand":
		p1 = create_open_hand_monk(name)
		new_options = OpenHand.list_options
	elif player_subclass == "Four Elements":
		p1 = create(name, FourElements)
		new_options = FourElements.list_options
	else:
		p1 = create(name, Monk)
		new_options = Monk.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}
