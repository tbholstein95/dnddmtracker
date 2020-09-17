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

		print("Name:" + player.get_name(), "Level:", + player.get_level())

		return player

	def list_knowledge_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Channel Divinity\n" + (

			"[2]: Reset Channel Divinity\n" + "[3]: Use Divine Intervention\n" + "[4]: Use Visions of the Past\n"

				+ "[5]: Reset Visions of the Past" + "[6]: Use Hit Dice\n" + "[7]: Change Level\n" + "[8]: Exit\n")))

		if selection == 1:
			self.use_channel_divinity()
		elif selection == 2:
			level = self.get_level()
			self.set_channel_divinity_max(level)
		elif selection == 3:
			self.use_divine_intervention()
		elif selection == 4:
			self.use_visions_of_the_past()
		elif selection == 5:
			self.set_visions_of_the_past(False)
		elif selection == 6:
			self.use_hit_dice()
		elif selection == 7:
			self.set_level()
		elif selection == 8:
			print("backing")
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

		print("Name:" + player.get_name(), "Level:", + player.get_level(), + "Wisdom:", + player.get_wisdom(), "Warding:", (
			+ player.get_max_warding_flare(), "Slots" + player.get_cur_spell_slot(level)))

	def list_light_options(self):
		selection = 0
		selection = int(input("What action are you counting?\n" + "[1]: Use Channel Divinity\n" + (

			"[2]: Reset Channel Divinity\n" + "[3]: Use Divine Intervention\n" + "[4]: Reset Divine Intervention\n" +

			"[5]: Use Warding Flare\n" + "[6]: Reset Warding Flare\n" + "[7]: Change Hit Dice\n" + "[8]: Change Level\n" +(
				"[9]: Exit"))))

		if selection == 1:
			self.use_channel_divinity()
		elif selection == 2:
			level = self.get_level()
			self.set_channel_divinity_max(level)
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



