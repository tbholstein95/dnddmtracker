from Classes.subclasses.full_caster import *

cleric_dict = {}


class Cleric(FullCaster):

	def __init__(self):
		self.channel_divinity_max = 1
		self.current_channel_divinity = 1
		self.divine_intervention = False
		self.divine_intervention_seven_days = False
		self.divine_intervention_day_timer = 7
		self.default_cleric_options = {}
		super().__init__()

	def get_current_channel_divinity(self):
		return self.current_channel_divinity

	def set_channel_divinity_max(self, level):
		if level < 6:
			self.channel_divinity_max = 1
			self.current_channel_divinity = 1
		if 6 <= level < 10:
			self.channel_divinity_max = 2
			self.current_channel_divinity = 2
		if level <= 18:
			self.channel_divinity_max = 3
			self.current_channel_divinity = 3

	def use_channel_divinity(self):
		if self.get_current_channel_divinity() > 0:
			self.current_channel_divinity -= 1
			print("Used Channel Divinity")
		else:
			print("Not enough Channel Divinity Left")
			return

	def reset_channel_divinity(self):
		self.current_channel_divinity = self.channel_divinity_max

	def get_divine_intervention(self):
		return self.divine_intervention

	def get_divine_intervention_seven_days(self):
		return self.divine_intervention_seven_days

	def set_divine_intervention(self, truefalse):
		self.divine_intervention = truefalse

	def set_divine_intervention_seven_days(self, truefalse):
		self.divine_intervention_seven_days = truefalse

	def get_divine_intervention_day_timer(self):
		return self.divine_intervention_day_timer

	def use_divine_intervention(self):
		if self.get_divine_intervention():
			print("Already used Divine Intervention")
		if self.get_divine_intervention_seven_days():
			days_left = self.get_divine_intervention_day_timer()
			print(f"There are {days_left} before Cleric can use Divine Intervention again")
		else:
			intervene = input("Did the Deity intervene?")
			intervene.capitalize()
			if intervene == "Yes":
				self.set_divine_intervention_seven_days(True)
			else:
				self.set_divine_intervention(True)
				if self.get_divine_intervention() == 0:
					self.set_divine_intervention(False)

	def remove_divine_intervention_day(self):
		if self.divine_intervention:
			print("Reset Divine Intervention")
			self.divine_intervention = False
		else:
			self.divine_intervention_day_timer -= 1

	def create_cleric_options(self):
		self.default_cleric_options['0'] = "[5]: Use Channel Divinity\n" + "[6]: Reset Channel Divinity\n" + \
						"[7]: Use Divine Intervention\n" + "[8]: Reset Divine Intervention\n"
		self.default_cleric_options['5'] = self.use_channel_divinity
		self.default_cleric_options['6'] = self.reset_channel_divinity
		self.default_cleric_options['7'] = self.use_divine_intervention
		self.default_cleric_options['8'] = self.remove_divine_intervention_day

		return self.default_cleric_options

	def change_level(self):
		self.set_level()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()
		self.set_hit_dice(self.get_level())


class Knowledge(Cleric):

	def __init__(self):
		self.visions_of_the_past = False
		self.knowledge_options = {}
		super().__init__()

	def set_visions_of_the_past(self, truefalse):
		self.visions_of_the_past = truefalse

	def get_visions_of_the_past(self):
		return self.visions_of_the_past

	def use_visions_of_the_past(self):
		if self.visions_of_the_past:
			print("Already used Visions of the Past this Awake Period")
			return
		else:
			self.set_visions_of_the_past(True)

	def reset_visions_of_the_past(self):
		self.set_visions_of_the_past(False)

	def create_knowledge_options(self):
		self.knowledge_options['0'] = "[9]: Use Visions of the Past\n" + "[10]: Reset Visions of the Past\n" + \
					"[11]: Change Level\n" + "[12]: Exit\n"
		self.knowledge_options['9'] = self.use_visions_of_the_past
		self.knowledge_options['10'] = self.reset_visions_of_the_past
		self.knowledge_options['11'] = self.change_level
		self.knowledge_options['12'] = leave

	def list_options(self):
		selection = int(input(self.knowledge_options.get("0")))
		print(selection)
		self.knowledge_options["{}".format(selection)]()


class Light(Cleric):
	def __init__(self):
		self.wisdom = 0
		self.max_warding_flare = 0
		self.cur_warding_flare = 0
		self.light_options = {}
		super().__init__()

	def get_wisdom(self):
		return self.wisdom

	def set_wisdom(self):
		wis = int(input("What is this Cleric's Wisdom?"))
		self.wisdom = wis

	def set_max_warding_flare(self):
		flare = self.get_wisdom()
		self.max_warding_flare = flare

	def get_max_warding_flare(self):
		return self.max_warding_flare

	def get_cur_warding_flare(self):
		return self.cur_warding_flare

	def reset_current_warding_flare(self):
		amount = self.get_max_warding_flare()
		self.cur_warding_flare = amount

	def use_warding_flare(self):
		if self.get_cur_warding_flare() == 0:
			print("Not enough Warding Flares left")
			return
		else:
			self.cur_warding_flare -= 1

	def change_light_level(self):
		self.change_level()
		self.set_max_warding_flare()
		self.reset_current_warding_flare()
		self.set_wisdom()

	def create_light_options(self):
		self.light_options['0'] = "[9]: Use Warding Flare\n" + "[10]: Reset Warding Flare\n" + \
					"[11]: Change Level\n" + "[12]: Exit\n"
		self.light_options['9'] = self.use_warding_flare
		self.light_options['10'] = self.reset_current_warding_flare
		self.light_options['11'] = self.change_light_level
		self.light_options['12'] = leave
		return self.light_options

	def list_options(self):
		selection = int(input(self.light_options.get("0")))
		print(selection)
		self.light_options["{}".format(selection)]()


class Tempest(Cleric):

	def __init__(self):
		self.max_wrath_of_the_storm = 0
		self.cur_wrath_of_the_storm = 0
		self.wisdom = 0
		self.tempest_options = {}
		super().__init__()

	def get_wisdom(self):
		return self.wisdom

	def set_wisdom(self):
		wis = int(input("What is this Cleric's Wisdom?"))
		self.wisdom = wis

	def set_max_wrath_of_the_storm(self):
		wrath = self.get_wisdom()
		self.max_wrath_of_the_storm = wrath

	def get_max_wrath_of_the_storm(self):
		return self.max_wrath_of_the_storm

	def get_cur_wrath_of_the_storm(self):
		return self.cur_wrath_of_the_storm

	def reset_cur_wrath_of_the_storm(self):
		amount = self.get_max_wrath_of_the_storm()
		self.cur_wrath_of_the_storm = amount

	def use_wrath_of_the_storm(self):
		if self.get_cur_wrath_of_the_storm() == 0:
			print("Not enough Warding Flares left")
			return
		else:
			self.cur_wrath_of_the_storm -= 1

	def change_tempest_level(self):
		self.change_level()
		self.set_wisdom()
		self.set_max_wrath_of_the_storm()
		self.reset_cur_wrath_of_the_storm()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()

	def list_tempest_options(self):
		self.tempest_options['0'] = "[9]: Wrath of the Storm\n" + "[10]: Reset Wrath of the Storm\n" + \
					"[13]: Change Level\n" + "[14]: Exit\n"
		self.tempest_options['9'] = self.use_wrath_of_the_storm
		self.tempest_options['10'] = self.reset_cur_wrath_of_the_storm
		self.tempest_options['11'] = self.change_tempest_level
		self.tempest_options['12'] = leave

	def list_options(self):
		def list_options(self):
			selection = int(input(self.tempest_options.get("0")))
			print(selection)
			self.tempest_options["{}".format(selection)]()



class War(Cleric):

	def __init__(self):
		self.max_bonus_attack = 0
		self.cur_bonus_attack = 0
		self.wisdom = 0
		self.war_options = {}
		super().__init__()

	def get_wisdom(self):
		return self.wisdom

	def set_wisdom(self):
		wis = int(input("What is this Cleric's Wisdom?"))
		self.wisdom = wis

	def set_max_bonus_attack(self):
		bonus = self.get_wisdom()
		self.max_bonus_attack = bonus

	def get_max_bonus_attack(self):
		return self.max_bonus_attack

	def get_cur_bonus_attack(self):
		return self.cur_bonus_attack

	def reset_cur_bonus_attack(self):
		amount = self.get_max_bonus_attack()
		self.cur_bonus_attack = amount

	def use_bonus_attack(self):
		if self.get_cur_bonus_attack() == 0:
			print("Not enough Warding Flares left")
			return
		else:
			self.cur_bonus_attack -= 1

	def create_war_cleric(self, name):
		name = name
		player = War()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(player.get_level())
		player.set_current_list_spell_slots()
		player.set_wisdom()
		player.set_max_bonus_attack()
		player.reset_cur_bonus_attack()
		player.set_hit_dice(player.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Wisdom:", + player.get_wisdom(),

		      "Warding:", (+ player.get_max_bonus_attack(), "Slots" + player.get_cur_spell_slot(self.get_level())))

		return player

	def list_war_options(self):
		selection = int(input(
			"What action are you counting?\n" + "[1]: Cast Spell\n" + "[2]: Reset Spells\n" + "[3]: Use Channel Divinity\n" +

			"[4]: Reset Channel Divinity\n" + "[5]: Use Divine Intervention\n" + "[6]: Reset Divine Intervention\n" +

			"[7]: Use Bonus Attack\n" + "[8]: Reset Bonus Attacks\n" + "[9]: Use Hit Dice\n" + "[10]: Reset Hit Dice\n" +

			"[11]: Change Level\n" + "[12]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		if selection == 2:
			self.set_current_list_spell_slots()
		if selection == 3:
			self.use_channel_divinity()
		elif selection == 4:
			self.set_channel_divinity_max(self.get_level())
		elif selection == 5:
			self.use_divine_intervention()
		elif selection == 6:
			self.set_divine_intervention(False)
		elif selection == 7:
			self.use_bonus_attack()
		elif selection == 8:
			self.reset_cur_bonus_attack()
		elif selection == 9:
			self.use_hit_dice()
		elif selection == 10:
			self.reset_current_hit_dice()
		elif selection == 11:
			self.set_level()
			self.set_hit_dice(self.get_level())
		elif selection == 12:
			print("Leaving")
			return


class Grave(Cleric):

	def __init__(self):
		self.max_eyes_of_the_grave = 0
		self.cur_eyes_of_the_grave = 0
		self.max_sentinel_at_deaths_door = 0
		self.cur_sentinel_at_deaths_door = 0
		self.wisdom = 0
		super().__init__()

	def get_wisdom(self):
		return self.wisdom

	def set_wisdom(self):
		wis = int(input("What is this Cleric's Wisdom?"))
		self.wisdom = wis

	def set_max_eyes_of_the_grave(self):
		eyes = self.get_wisdom()
		self.max_eyes_of_the_grave = eyes

	def set_max_sentinel_at_deaths_door(self):
		sentinel = self.get_wisdom()
		self.max_sentinel_at_deaths_door = sentinel

	def get_max_eyes_of_the_grave(self):
		return self.max_eyes_of_the_grave

	def get_max_sentinel_at_deaths_door(self):
		return self.max_sentinel_at_deaths_door

	def get_cur_eyes_of_the_grave(self):
		return self.cur_eyes_of_the_grave

	def get_cur_sentinel_at_deaths_door(self):
		return self.cur_sentinel_at_deaths_door

	def reset_cur_eyes_of_the_grave(self):
		amount = self.get_max_eyes_of_the_grave()
		self.cur_eyes_of_the_grave = amount

	def reset_cur_sentinel_at_deaths_door(self):
		amount = self.get_max_sentinel_at_deaths_door()
		self.cur_sentinel_at_deaths_door = amount

	def use_eyes_of_the_grave(self):
		if self.get_cur_eyes_of_the_grave() == 0:
			print("Not enough Warding Flares left")
			return
		else:
			self.cur_eyes_of_the_grave -= 1

	def use_sentinel_at_deaths_door(self):
		if self.get_cur_sentinel_at_deaths_door() == 0:
			print("Not enough Warding Flares left")
			return
		else:
			self.cur_sentinel_at_deaths_door -= 1

	def create_grave_cleric(self, name):
		name = name
		player = Grave()
		player.set_level()
		player.set_name(name)
		player.set_max_list_spell_slots(self.get_level())
		player.set_current_list_spell_slots()
		player.set_wisdom()
		player.set_max_sentinel_at_deaths_door()
		player.set_max_eyes_of_the_grave()
		player.reset_cur_sentinel_at_deaths_door()
		player.reset_cur_eyes_of_the_grave()
		player.set_hit_dice(self.get_level())
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Wisdom:", + player.get_wisdom(), (
			"Eyes of the Grave:", + player.get_max_eyes_of_the_grave(), (
				"Sentinel:", + player.get_max_sentinel_at_deaths_door(),
				"Slots" + player.get_cur_spell_slot(self.get_level()))))

		return player

	def list_grave_options(self):
		selection = int(
			input(
				"What action are you counting?\n" + "[1]: Cast Spell\n" + "[2]: Reset Spells\n" + "[3]: Use Channel Divinity\n" +

				"[4]: Reset Channel Divinity\n" + "[5]: Use Divine Intervention\n" + "[6]: Reset Divine Intervention\n" +

				"[7]: Use Sentinel at Deaths Door\n" + "[8]: Reset Sentinel at Death's Door\n" +

				"[9]: Use Eyes of the Grave\n" + "[10] Reset Eyes of the Grave\n" + "[11]: Use Hit Dice\n" +

				"[12]: Reset Hit Dice\n" + "[13]: Change Level\n" + "[14]: Exit\n"))

		if selection == 1:
			self.use_cur_spell_slot()
		elif selection == 2:
			self.set_current_list_spell_slots()
		elif selection == 3:
			self.use_channel_divinity()
		elif selection == 4:
			self.set_channel_divinity_max(self.get_level())
		elif selection == 5:
			self.use_divine_intervention()
		elif selection == 6:
			self.set_divine_intervention(False)
		elif selection == 7:
			self.use_sentinel_at_deaths_door()
		elif selection == 8:
			self.reset_cur_sentinel_at_deaths_door()
		elif selection == 9:
			self.use_eyes_of_the_grave()
		elif selection == 10:
			self.reset_cur_eyes_of_the_grave()
		elif selection == 11:
			self.use_hit_dice()
		elif selection == 12:
			self.reset_current_hit_dice()
		elif selection == 13:
			self.set_level()
			self.set_hit_dice(self.get_level())
		elif selection == 14:
			print("Leaving")
			return


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	# player.set_level()
	# player.set_max_list_spell_slots(player.get_level())
	# player.set_current_list_spell_slots()
	# player.set_hit_dice(player.get_level())
	return player


def create_cleric(name):
	player = create(name, Cleric)
	default_player_opts = player.create_player_character_options()
	cleric_opts = player.create_cleric_options()
	merge_dicts(default_player_opts, cleric_opts)
	return player


def create_knowledge_cleric(name):
	player = create(name, Knowledge)
	player.change_level()
	player.create_knowledge_options()
	default_player_opts = player.create_player_character_options()
	default_spell_opts = player.create_fullcaster_character_options()
	cleric_opts = player.create_cleric_options()
	merge_dicts(default_player_opts, default_spell_opts)
	merge_dicts(default_spell_opts, cleric_opts)
	merge_dicts(cleric_opts, player.knowledge_options)
	return player


def create_light_cleric(name):
	player = create(name, Light)
	player.change_light_level()
	player.create_light_options()
	default_player_opts = player.create_player_character_options()
	default_spell_opts = player.create_fullcaster_character_options()
	cleric_opts = player.create_cleric_options()
	light_opts = player.light_options
	merge_dicts(default_player_opts, default_spell_opts)
	merge_dicts(default_spell_opts, cleric_opts)
	merge_dicts(cleric_opts, light_opts)
	return player


def create_tempest_cleric(name):
	player = create(name, Tempest)
	player.change_tempest_level()
	default_player_opts = player.create_player_character_options()
	default_spell_opts = player.create_fullcaster_character_options()
	cleric_opts = player.create_cleric_options()
	tempest_opts = player.tempest_options
	merge_dicts(default_player_opts, default_spell_opts)
	merge_dicts(default_player_opts, cleric_opts)
	merge_dicts(cleric_opts, tempest_opts)
	return player


def main_cleric_making(name, dictionary):
	player_subclass = input("What is their subclass?").capitalize()
	if player_subclass == "Knowledge":
		p1 = create_knowledge_cleric(name)
		new_options = Knowledge.list_options
	elif player_subclass == "Light":
		p1 = create_light_cleric(name)
		new_options = Light.list_options
	elif player_subclass == "Tempest":
		p1 = create_tempest_cleric(name)
		new_options = Tempest.list_options
	elif player_subclass == "War":
		p1 = War()
		p1 = p1.create_war_cleric(name)
		class_options = War.list_war_options
	elif player_subclass == "Grave":
		p1 = Grave()
		p1.create_grave_cleric(name)
		class_options = Grave.list_grave_options
	else:
		p1 = create_cleric(name)
		new_options = 0

	# cleric_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass, "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}
