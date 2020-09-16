from playercharacter import *
from barbarian import *

# BOOL
running = True

# VAR
player_dictionary = {}
# ################################################Program###############################################################
number_of_players = int(input("How many players are in your party?"))
for x in range(number_of_players):
	p1 = None
	player_class = input("What is this player's class?")
	player_class = player_class.capitalize()
	if player_class == "Barbarian":
		p1 = None
		pcur = 0
		player_subclass = input("What is their subclass?")
		player_subclass = player_subclass.capitalize()
		if player_subclass == "Berserker":
			p1 = Berserker()
			p1 = p1.create_berserker_barbarian()
		elif player_subclass == "Ancestral":
			p1 = AncestralGuardian.create_ancestral_barbarian(p1)
		elif player_subclass == "Zealot":
			p1 = Zealot.create_Zealot_barbarian(p1)

		player_dictionary[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass}
		print(player_dictionary)



while running:
	current_player = input("Who are you modifying?\n")
	if current_player == "exit":
		print("Stopping")
		running = False
		break
	# current_mod = player_dictionary.get(f'{current_player}')
	current_mod = player_dictionary[f'{current_player}']["character"]
	print(current_mod)
	print(player_dictionary[f'{current_player}']["subclass"])
	current_mod.list_berserker_options()
	# task = input("What would you like to do?\n")
	# task = task.capitalize()
	# if task == "Rage":
	# 	current_mod.use_b_rage()
	# 	print(current_mod.get_rage())

