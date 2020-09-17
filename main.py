from playercharacter import *
from barbarian import *
from bard import *

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