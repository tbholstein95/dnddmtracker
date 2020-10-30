from Classes.subclasses.playerclasses.barbarian import *
from Classes.subclasses.playerclasses.bard import *
from Classes.subclasses.playerclasses.cleric import *
from Classes.subclasses.playerclasses.druid import *
from Classes.subclasses.playerclasses.monk import *
from Classes.subclasses.playerclasses.sorcerer import *
# VAR
player_dictionary = {}


def main():
	running = True
	number_of_players = int(input("How many players are in your party?"))
	for x in range(number_of_players):
		p1 = None
		player_name = input("What is this player's name?")
		player_class = input("What is this player's class?")
		player_class = player_class.capitalize()
		if player_class == "Barbarian":
			main_barb_making(player_name, player_dictionary)
		if player_class == "Bard":
			main_bard_making(player_name, player_dictionary)
		if player_class == "Cleric":
			main_cleric_making(player_name, player_dictionary)
		if player_class == "Druid":
			main_druid_making(player_name, player_dictionary)
		if player_class == "Monk":
			main_monk_making(player_name, player_dictionary)
		if player_class == "Sorcerer":
			main_sorcerer_making(player_name, player_dictionary)


	while running:
		current_player = input("Who are you modifying?\n")
		if current_player == "exit":
			print("Stopping")
			running = False
			break
		# set current player
		current_mod = player_dictionary[f'{current_player}']["character"]
		print(current_mod)
		print(player_dictionary)
		# get current player's options
		player_dictionary[f'{current_player}']['options'](current_mod)


if __name__ == '__main__':
	main()