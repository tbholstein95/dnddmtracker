from barbarian import Barbarian
from barbarian import Berserker
from barbarian import *

player_class = input("What is this player's class?")
player_class = playerclass.capitalize()
if player_class == "Barbarian":
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	player = None
	if player_subclass == "Berserker":
		Berserker.create_berserker_barbarian(player)
	elif player_subclass == "Ancestral":
		AncestralGuardian.create_ancestral_barbarian(player)

