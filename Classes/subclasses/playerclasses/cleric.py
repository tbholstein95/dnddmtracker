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

	def set_channel_divinity_max(self):
		level = self.get_level()
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
			intervene = int_checker("Did the Deity intervene?\n[1]: Yes\n[2]: No")
			if intervene == 1:
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
		self.base_change_level()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()
		self.set_channel_divinity_max()
		self.reset_channel_divinity()

	def list_options(self):
		selection = int_checker(self.default_cleric_options.get("0"))
		print(selection)
		self.default_cleric_options["{}".format(selection)]()


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
		selection = int_checker(self.knowledge_options.get("0"))
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
		wis = int_checker("What is this Cleric's Wisdom?")
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
		selection = int_checker(self.light_options.get("0"))
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
		wis = int_checker("What is this Cleric's Wisdom?")
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

	def create_tempest_options(self):
		self.tempest_options['0'] = "[9]: Wrath of the Storm\n" + "[10]: Reset Wrath of the Storm\n" + \
					"[13]: Change Level\n" + "[14]: Exit\n"
		self.tempest_options['9'] = self.use_wrath_of_the_storm
		self.tempest_options['10'] = self.reset_cur_wrath_of_the_storm
		self.tempest_options['11'] = self.change_tempest_level
		self.tempest_options['12'] = leave
		return self.tempest_options

	def list_options(self):
		selection = int_checker(self.tempest_options.get("0"))
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
		wis = int_checker("What is this Cleric's Wisdom?")
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

	def change_war_level(self):
		self.set_level()
		self.set_max_list_spell_slots(self.get_level())
		self.set_current_list_spell_slots()
		self.set_wisdom()
		self.set_max_bonus_attack()
		self.reset_cur_bonus_attack()
		self.set_hit_dice(self.get_level())

	def create_war_options(self):
		self.war_options['0'] = "[9]: Use Bonus Attack\n" + "[10]: Reset Bonus Attacks\n" + "[11]: Change Level\n" \
					+ "[12]: Exit\n"
		self.war_options['9'] = self.use_bonus_attack
		self.war_options['10'] = self.reset_cur_bonus_attack
		self.war_options['11'] = self.change_war_level
		self.war_options['12'] = leave
		return self.war_options

	def list_options(self):
		selection = int_checker(self.war_options.get("0"))
		print(selection)
		self.war_options["{}".format(selection)]()


class Grave(Cleric):

	def __init__(self):
		self.max_eyes_of_the_grave = 0
		self.cur_eyes_of_the_grave = 0
		self.max_sentinel_at_deaths_door = 0
		self.cur_sentinel_at_deaths_door = 0
		self.wisdom = 0
		self.grave_options = {}
		super().__init__()

	def get_wisdom(self):
		return self.wisdom

	def set_wisdom(self):
		wis = int_checker("What is this Cleric's Wisdom?")
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

	def change_grave_level(self):
		self.change_level()
		self.set_wisdom()
		self.set_max_sentinel_at_deaths_door()
		self.set_max_eyes_of_the_grave()
		self.reset_cur_sentinel_at_deaths_door()
		self.reset_cur_eyes_of_the_grave()

	def create_grave_options(self):
		self.grave_options['0'] = "[9]: Use Sentinel at Deaths Door\n" + "[10]: Reset Sentinel at Death's Door\n" + \
					"[11]: Use Eyes of the Grave\n" + "[12] Reset Eyes of the Grave\n" + "[13]: Change Level\n" + "[14]: Exit\n"
		self.grave_options['9'] = self.use_sentinel_at_deaths_door
		self.grave_options['10'] = self.reset_cur_sentinel_at_deaths_door
		self.grave_options['11'] = self.use_eyes_of_the_grave
		self.grave_options['12'] = self.reset_cur_eyes_of_the_grave
		self.grave_options['13'] = self.change_grave_level
		self.grave_options['14'] = leave
		return self.grave_options

	def list_options(self):
		selection = int_checker(self.grave_options.get("0"))
		print(selection)
		self.grave_options["{}".format(selection)]()


def merge_base_cleric_dicts(player):
	cleric_opts = player.create_cleric_options()
	merge_dicts(player.merge_base_and_fullspell_options(), cleric_opts)
	return cleric_opts


def create(name, subclass):
	player = subclass()
	player.set_name(name)
	return player


def create_cleric(name):
	player = create(name, Cleric)
	player.change_level()
	merge_base_cleric_dicts(player)
	return player


def create_grave_cleric(name):
	player = create(name, Grave)
	player.change_grave_level()
	merge_dicts(merge_base_cleric_dicts(player), player.create_grave_options())
	return player


def create_knowledge_cleric(name):
	player = create(name, Knowledge)
	player.change_level()
	player.create_knowledge_options()
	merge_dicts(merge_base_cleric_dicts(player), player.create_knowledge_options())
	return player


def create_light_cleric(name):
	player = create(name, Light)
	player.change_light_level()
	merge_dicts(merge_base_cleric_dicts(player), player.create_light_options())
	return player


def create_tempest_cleric(name):
	player = create(name, Tempest)
	player.change_tempest_level()
	merge_dicts(merge_base_cleric_dicts(player), player.create_tempest_options())
	return player


def create_war_cleric(name):
	player = create(name, War)
	player.change_war_level()
	merge_dicts(merge_base_cleric_dicts(player), player.create_tempest_options())
	return player


def main_cleric_making(name, dictionary):
	player_subclass = int_checker("What is their subclass?\n[1]: Knowledge\n[2]: Light\n[3]:Tempest\n" +
				"[4]: War\n[5]: Grave\n[6]: Other\n")
	if player_subclass == "1":
		p1 = create_knowledge_cleric(name)
		new_options = Knowledge.list_options
	elif player_subclass == "2":
		p1 = create_light_cleric(name)
		new_options = Light.list_options
	elif player_subclass == "3":
		p1 = create_tempest_cleric(name)
		new_options = Tempest.list_options
	elif player_subclass == "4":
		p1 = create_war_cleric(name)
		new_options = War.list_options
	elif player_subclass == "5":
		p1 = create_grave_cleric(name)
		new_options = Grave.list_options
	else:
		p1 = create_cleric(name)
		new_options = Cleric.list_options

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass, "new_options": new_options}
