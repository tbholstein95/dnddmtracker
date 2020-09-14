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
		player_subclass = input("What is their subclass?")
		player_subclass = player_subclass.capitalize()
		if player_subclass == "Berserker":
			p1 = Berserker.create_berserker_barbarian(p1)
		elif player_subclass == "Ancestral":
			p1 = AncestralGuardian.create_ancestral_barbarian(p1)
		elif player_subclass == "Zealot":
			p1 = Zealot.create_Zealot_barbarian(p1)

	player_dictionary['p' + str(x)] = p1


while running:
	task = input("What would you like to do?\n")
	task = task.capitalize()
	if task == "Rage":
		p1.use_b_rage()
		print(p1.get_rage())

	else:
		running = False
