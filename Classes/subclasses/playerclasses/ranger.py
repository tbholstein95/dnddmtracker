from Classes.subclasses.half_caster import *
ranger_dict = {}

class Ranger(HalfCaster):
	def __init__(self):
		self.ranger_options = {}
		super().__init__()

	def create_ranger_options(self):
		self.ranger_options['0'] = "[5]: Change Level\n" + "[6]: Exit\n"
		self.ranger_options['5'] = self.change_half_caster_level
		self.ranger_options['6'] = leave
		return self.ranger_options

	def list_options(self):
		selection = int_checker(self.ranger_options.get("0"))
		print(selection)
		self.ranger_options["{}".format(selection)]()


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_ranger(name):
	player = create(name, Ranger)
	player.change_half_caster_level()
	merge_dicts(player.merge_player_and_half(), player.create_ranger_options())
	return player


def main_ranger_making(name, dictionary):
	player_subclass = input("What is their subclass?").capitalize()
	p1 = create_ranger(name)
	class_options = Ranger.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "options": class_options}
