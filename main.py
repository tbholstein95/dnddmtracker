from playercharacter import *
from barbarian import *

# BOOL



# VAR
player_dictionary = {}
# ################################################Program###############################################################


def main():
	running = True
	number_of_players = int(input("How many players are in your party?"))
	for x in range(number_of_players):
		p1 = None
		player_name = input("What is this player's name?")
		player_class = input("What is this player's class?")
		player_class = player_class.capitalize()
		if player_class == "Barbarian":

			# 	p1 = None
			# 	pcur = 0
			# 	player_subclass = input("What is their subclass?")
			# 	player_subclass = player_subclass.capitalize()
			# 	if player_subclass == "Berserker":
			# 		p1 = Berserker()
			# 		p1 = p1.create_berserker_barbarian()
			# 		class_options = Berserker.list_berserker_options
			# 	elif player_subclass == "Ancestral":
			# 		p1 = AncestralGuardian.create_ancestral_barbarian(p1)
			# 	elif player_subclass == "Zealot":
			# 		p1 = Zealot.create_Zealot_barbarian(p1)

			# main_make_barb(player_class)
			main_barb_making(player_name, player_dictionary)
			print(player_dictionary, "player dictionary")




		# player_dictionary[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass, "options": class_options}
		# print(player_dictionary)



	while running:
		current_player = input("Who are you modifying?\n")
		if current_player == "exit":
			print("Stopping")
			running = False
			break
		# current_mod = player_dictionary.get(f'{current_player}')
		current_mod = player_dictionary[f'{current_player}']["character"]
		cur_sub_class = (player_dictionary[f'{current_player}']["subclass"])

		player_dictionary[f'{current_player}']['options'](current_mod)



def main_make_barb(player_class):
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Berserker":
		p1 = Berserker()
		p1 = p1.create_berserker_barbarian()
		class_options = Berserker.list_berserker_options
	elif player_subclass == "Ancestral":
		p1 = AncestralGuardian.create_ancestral_barbarian(p1)
	elif player_subclass == "Zealot":
		p1 = Zealot.create_Zealot_barbarian(p1)

	player_dictionary[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
						 "options": class_options}

if __name__ == '__main__':
	main()