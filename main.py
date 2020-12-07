from Classes.subclasses.playerclasses.barbarian import *
from Classes.subclasses.playerclasses.bard import *
from Classes.subclasses.playerclasses.cleric import *
from Classes.subclasses.playerclasses.druid import *
from Classes.subclasses.playerclasses.fighter import *
from Classes.subclasses.playerclasses.monk import *
from Classes.subclasses.playerclasses.paladin import *
from Classes.subclasses.playerclasses.ranger import *
from Classes.subclasses.playerclasses.rogue import *
from Classes.subclasses.playerclasses.sorcerer import *
from Classes.subclasses.playerclasses.warlock import *
from Classes.subclasses.playerclasses.wizard import *
from Classes.playercharacter import *

# VAR
player_dictionary = {}


def main():
	number_of_players = int_checker("How many players are in this party?")
	for x in range(number_of_players):
		player_name = input("What is this player's name?")
		character_class_select(player_name, player_dictionary)

	while True:
		for x in range(len(player_dictionary)):
			print("[{}]:".format(x), list(player_dictionary.keys())[x])
		current_player_index = int_checker("Who are you modifying? ('Enter number')\n")
		current_player = list(player_dictionary.keys())[current_player_index]
		if current_player == "exit":
			print("Stopping")
			break
		# set current player
		current_mod = player_dictionary[f'{current_player}']["character"]
		player_dictionary[f'{current_player}']['new_options'](current_mod)


def character_class_select(player_name, player_dict):
	while True:
		player_class = input("What is this player's class?").capitalize()
		if player_class == "Barbarian":
			return main_barb_making(player_name, player_dict)
		if player_class == "Bard":
			return main_bard_making(player_name, player_dict)
		if player_class == "Cleric":
			return main_cleric_making(player_name, player_dict)
		if player_class == "Druid":
			return main_druid_making(player_name, player_dict)
		if player_class == "Fighter":
			return main_fighter_making(player_name, player_dict)
		if player_class == "Monk":
			return main_monk_making(player_name, player_dict)
		if player_class == "Paladin":
			return main_paladin_making(player_name, player_dict)
		if player_class == "Ranger":
			return main_ranger_making(player_name, player_dict)
		if player_class == "Rogue":
			return main_rogue_making(player_name, player_dict)
		if player_class == "Sorcerer":
			return main_sorcerer_making(player_name, player_dict)
		if player_class == "Warlock":
			return main_warlock_making(player_name, player_dict)
		if player_class == "Wizard":
			return main_wizard_making(player_name, player_dict)


if __name__ == '__main__':
	main()