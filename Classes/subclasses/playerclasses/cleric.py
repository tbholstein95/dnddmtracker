from Classes.subclasses.full_caster import *
cleric_dict = {}


class Cleric(FullCaster):

	def __init__(self):
		self.channel_divinity_max = 1
		self.current_channel_divinity = 1
		self.divine_intervention = False
		self.divine_intervention_seven_days = False
		self.divine_intervention_day_timer = 7
		FullCaster.__init__(self)

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
			self.current_channel_divinity =3

	def use_channel_divinity(self):
		if self.get_current_channel_divinity() > 0:
			self.current_channel_divinity -= 1
			print("Used Channel Divinity")
		else:
			print("Not enough Channel Divinity Left")
			return

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
		self.divine_intervention_day_timer -= 1

	def create_cleric(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Cleric()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Slots" + player.get_cur_spell_slot(level))

		return player

	def list_cleric_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Channel Divinity\n" +

			"[2]: Reset Channel Divinity\n" + "[3]: Use Divine Intervention\n" + "[4]: Reset Divine Intervention\n" +

			"[5]: Use Hit Dice\n" + "[6]: Reset Hit Dice" + "[7]: Change Level\n" + "[8]: Exit"))

		if selection == 1:
			self.use_channel_divinity()
		elif selection == 2:
			self.set_channel_divinity_max(self.get_level())
		elif selection == 3:
			self.use_divine_intervention()
		elif selection == 4:
			self.set_divine_intervention(False)
		elif selection == 5:
			self.use_hit_dice()
		elif selection == 6:
			self.reset_current_hit_dice()
		elif selection == 7:
			self.set_level()
			self.set_hit_dice(self.get_level())
		elif selection == 8:
			print("Leaving")
			return


class Knowledge(Cleric):

	def __init__(self):
		self.visions_of_the_past = False
		Cleric.__init__(self)

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

	def create_knowledge_cleric(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Knowledge()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

	def list_knowledge_options(self):
		selection = int(input("What action are you counting?\n" + "[1]: Use Channel Divinity\n" +

			"[2]: Reset Channel Divinity\n" + "[3]: Use Divine Intervention\n" + "[4]:Reset Divine Intervention" +

			"[5]: Use Visions of the Past\n" + "[6]: Reset Visions of the Past" + "[7]: Use Hit Dice\n" +

			"[8]: Reset Hit Dice" + "[9]: Change Level\n" + "[10]: Exit\n"))

		if selection == 1:
			self.use_channel_divinity()
		elif selection == 2:
			self.set_channel_divinity_max(self.get_level())
		elif selection == 3:
			self.use_divine_intervention()
		elif selection == 4:
			self.set_divine_intervention(False)
		elif selection == 5:
			self.use_visions_of_the_past()
		elif selection == 6:
			self.set_visions_of_the_past(False)
		elif selection == 7:
			self.use_hit_dice()
		elif selection == 8:
			self.reset_current_hit_dice()
		elif selection == 9:
			self.set_level()
		elif selection == 10:
			print("Leaving")
			return 0


class Light(Cleric):
	def __init__(self):
		self.wisdom = 0
		self.max_warding_flare = 0
		self.cur_warding_flare = 0
		Cleric.__init__(self)

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

	def create_light_cleric(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Light()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_wisdom()
		player.set_max_warding_flare()
		player.reset_current_warding_flare()
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Wisdom:", + player.get_wisdom(), "Warding:", (
			+ player.get_max_warding_flare(), "Slots" + player.get_cur_spell_slot(level)))

		return player

	def list_light_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Channel Divinity\n" +

			"[2]: Reset Channel Divinity\n" + "[3]: Use Divine Intervention\n" + "[4]: Reset Divine Intervention\n" +

			"[5]: Use Warding Flare\n" + "[6]: Reset Warding Flare\n" + "[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice\n" +

			"[8]: Change Level\n" + "[9]: Exit\n"))

		if selection == 1:
			self.use_channel_divinity()
		elif selection == 2:
			self.set_channel_divinity_max(self.get_level())
		elif selection == 3:
			self.use_divine_intervention()
		elif selection == 4:
			self.set_divine_intervention(False)
		elif selection == 5:
			self.use_warding_flare()
		elif selection == 6:
			self.reset_current_warding_flare()
		elif selection == 7:
			self.use_hit_dice()
		elif selection == 8:
			self.set_level()
			self.set_hit_dice(self.get_level())
		elif selection == 9:
			print("Leaving")
			return

class Tempest(Cleric):

	def __init__(self):
		self.max_wrath_of_the_storm = 0
		self.cur_wrath_of_the_storm = 0
		self.wisdom = 0
		Cleric.__init__(self)

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

	def create_tempest_cleric(self, name):
		name = name
		level = int(input("What level is this cleric?"))
		player = Tempest()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_wisdom()
		player.set_max_wrath_of_the_storm()
		player.reset_cur_wrath_of_the_storm()
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Wisdom:", + player.get_wisdom(), "Warding:", (
			+ player.get_max_wrath_of_the_storm(), "Slots" + player.get_cur_spell_slot(level)))

		return player


	def list_tempest_options(self):
		selection = 0
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Channel Divinity\n" +"[2]: Reset Channel Divinity\n" +

			"[3]: Use Divine Intervention\n" + "[4]: Reset Divine Intervention\n" + "[5]: Wrath of the Storm\n" +

			"[6]: Reset Wrath of the Storm\n" + "[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice\n" +

			"[9]: Change Level\n" +"[10]: Exit\n"))

		if selection == 1:
			self.use_channel_divinity()
		elif selection == 2:
			self.set_channel_divinity_max(self.get_level())
		elif selection == 3:
			self.use_divine_intervention()
		elif selection == 4:
			self.set_divine_intervention(False)
		elif selection == 5:
			self.use_wrath_of_the_storm()
		elif selection == 6:
			self.reset_cur_wrath_of_the_storm()
		elif selection == 7:
			self.use_hit_dice()
		elif selection == 8:
			self.reset_current_hit_dice()
		elif selection == 8:
			self.set_level()
			self.set_hit_dice(self.get_level())
		elif selection == 9:
			print("Leaving")
			return

class War(Cleric):

	def __init__(self):
		self.max_bonus_attack = 0
		self.cur_bonus_attack = 0
		self.wisdom = 0
		Cleric.__init__(self)

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
		level = int(input("What level is this cleric?"))
		player = War()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_wisdom()
		player.set_max_bonus_attack()
		player.reset_cur_bonus_attack()
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Wisdom:", + player.get_wisdom(),
		      "Warding:", (
			      + player.get_max_bonus_attack(), "Slots" + player.get_cur_spell_slot(level)))

		return player

	def list_war_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Channel Divinity\n" +

			"[2]: Reset Channel Divinity\n" + "[3]: Use Divine Intervention\n" + "[4]: Reset Divine Intervention\n" +

			"[5]: Use Bonus Attack\n" + "[6]: Reset Bonus Attacks\n" + "[7]: Use Hit Dice\n" + "[8]: Reset Hit Dice\n" +

			"[8]: Change Level\n" + "[9]: Exit\n"))

		if selection == 1:
			self.use_channel_divinity()
		elif selection == 2:
			self.set_channel_divinity_max(self.get_level())
		elif selection == 3:
			self.use_divine_intervention()
		elif selection == 4:
			self.set_divine_intervention(False)
		elif selection == 5:
			self.use_bonus_attack()
		elif selection == 6:
			self.reset_cur_bonus_attack()
		elif selection == 7:
			self.use_hit_dice()
		elif selection == 8:
			self.reset_current_hit_dice()
		elif selection == 8:
			self.set_level()
			self.set_hit_dice(self.get_level())
		elif selection == 9:
			print("Leaving")
			return

class Grave(Cleric):

	def __init__(self):
		self.max_eyes_of_the_grave = 0
		self.cur_eyes_of_the_grave = 0
		self.max_sentinel_at_deaths_door = 0
		self.cur_sentinel_at_deaths_door = 0
		self.wisdom = 0
		Cleric.__init__(self)

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
		level = int(input("What level is this cleric?"))
		player = Grave()
		player.set_level()
		player.set_name(name)
		player.set_spell_slots(level)
		player.set_wisdom()
		player.set_max_sentinel_at_deaths_door()
		player.set_max_eyes_of_the_grave()
		player.reset_cur_sentinel_at_deaths_door()
		player.reset_cur_eyes_of_the_grave()
		player.set_hit_dice(level)
		print("Name:" + player.get_name(), "Level:", + player.get_level(), "Wisdom:", + player.get_wisdom(), (
			"Eyes of the Grave:", + player.get_max_eyes_of_the_grave(), (
				"Sentinel:", + player.get_max_sentinel_at_deaths_door(), "Slots" + player.get_cur_spell_slot(level))))

		return player

	def list_grave_options(self):
		selection = int(
			input("What action are you counting?\n" + "[1]: Use Channel Divinity\n" + "[2]: Reset Channel Divinity\n" +

			"[3]: Use Divine Intervention\n" + "[4]: Reset Divine Intervention\n" + "[5]: Use Sentinel at Deaths Door\n" +

			"[6]: Reset Sentinel at Death's Door\n" + "[7]: Use Eyes of the Grave\n" + "[8] Reset Eyes of the Grave\n" +

			"[9]: Use Hit Dice\n" + "[10]: Reset Hit Dice\n" + "[10]: Change Level\n" + "[11]: Exit\n"))

		if selection == 1:
			self.use_channel_divinity()
		elif selection == 2:
			self.set_channel_divinity_max(self.get_level())
		elif selection == 3:
			self.use_divine_intervention()
		elif selection == 4:
			self.set_divine_intervention(False)
		elif selection == 5:
			self.use_sentinel_at_deaths_door()
		elif selection == 6:
			self.reset_cur_sentinel_at_deaths_door()
		elif selection == 7:
			self.use_eyes_of_the_grave()
		elif selection == 8:
			self.reset_cur_eyes_of_the_grave()
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

def main_cleric_making(name, dictionary):
	name = name
	player_subclass = input("What is their subclass?")
	player_subclass = player_subclass.capitalize()
	if player_subclass == "Knowledge":
		p1 = Knowledge()
		p1 = p1.create_knowledge_cleric(name)
		class_options = Knowledge.list_knowledge_options
	elif player_subclass == "Light":
		p1 = Light()
		p1 = p1.create_light_cleric(name)
		class_options = Light.list_light_options
	elif player_subclass == "Tempest":
		p1 = Tempest()
		p1 = p1.create_tempest_cleric(name)
		class_options = Tempest.list_tempest_options
	elif player_subclass == "War":
		p1 = War()
		p1 = p1.create_war_cleric(name)
		class_options = War.list_war_options
	elif player_subclass == "Grave":
		p1 = Grave()
		p1.create_grave_cleric(name)
		class_options = Grave.list_grave_options
	else:
		p1 = Cleric()
		p1 = p1.create_cleric(name)
		class_options = Cleric.list_cleric_options

	cleric_dict[f'{p1.get_name()}'] = {"character": p1, "subclass": player_subclass,
					 "options": class_options}

	dictionary[f'{name}'] = {"character": p1, "subclass": player_subclass,
				 "options": class_options}