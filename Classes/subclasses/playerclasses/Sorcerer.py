from Classes.subclasses.full_caster import *
sorcerer_dict = {}

class Sorcerer(FullCaster):

	def __init__(self):
		self.max_sorcery_points = 0
		self.current_sorcery_points = 0
		FullCaster.__init__(self)

	def set_max_sorcery_points(self, level):
		if level > 1:
			self.max_sorcery_points = level

	def get_max_sorcery_points(self):
		return self.max_sorcery_points

	def set_current_sorcery_points(self, amount):
		self.current_sorcery_points = amount

	def get_current_sorcery_points(self):
		return self.current_sorcery_points


	def reset_current_sorcery_points(self):
		amount = self.get_max_hit_dice()
		self.set_current_sorcery_points(amount)

	def add_sorcery_points(self, amount):
		current = self.get_current_sorcery_points()
		self.set_current_sorcery_points(current + amount)

	def use_sorcery_point(self, amount):
		current_sp = self.get_current_sorcery_points()
		if current_sp >= amount:
			self.set_current_sorcery_points(current_sp-amount)
		else:
			print("Sorcerer does not have that many sorcery points right now")

	def create_spell_slot(self):
		slot = int(input("What spell slot does the sorcerer want?"))
		point_cost = 0
		if slot == 1:
			point_cost = 2
		elif slot == 2:
			point_cost = 3
		elif slot == 3:
			point_cost = 5
		elif slot == 4:
			point_cost = 6
		elif slot == 5:
			point_cost = 7
		current_sp = self.get_current_sorcery_points()
		if point_cost > current_sp:
			print("Sorcerer only has {} sorcery points.".format(current_sp))
		if current_sp >= point_cost:
			self.use_sorcery_point(point_cost)
			self.add_spell_slot(slot)
			print("Added one slot to level {} spells.".format(slot))

	def create_sorcery_points(self):
		points = int(input("What level spell is the Sorcerer spending for this?"))
		slots = self.get_current_spell_slot(points)
		if slots >= 0:
			self.add_sorcery_points(points)
		else:
			print("Sorcerer doesn't have any remaining {} slots to spend".format(points))

	def use_careful_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")

	def use_distant_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")
	def use_empowered_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")
	def use_extended_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")
	def use_heightened_spell(self):
		self.use_sorcery_point(3)
		print("Spent 3 sorcery points")
	def use_quickened_spell(self):
		self.use_sorcery_point(2)
		print("Spent two sorcery point")
	def use_subtle_spell(self):
		self.use_sorcery_point(1)
		print("Spent one sorcery point")
	def use_twinned_spell(self):
		spell_level = int(input("What is the spell level?"))
		if self.get_current_spell_slot(spell_level) > 0:
			self.use_sorcery_point(spell_level)
			print("Spend {} sorcery point(s)".format(spell_level))
		else:
			print("No spell slots left for that level")

	def use_sorcerous_restoration(self):
		self.add_sorcery_points(4)

class Draconic(Sorcerer):
	def __init__(self):
		Sorcerer.__init__(self)

	def elemental_affinity_resistance(self):
		if self.level >= 6:
			self.use_sorcery_point(1)
			print("Sorcerer has resistance to whatever spell damage type was for an hour")
		else:
			print("Sorcerer needs to be at least level 6")

	def use_draconic_presence(self):
		if self.level >= 18:
			self.use_sorcery_point(5)
			print("Aura of fear created in 60 feet for 1 minute")
		else:
			print("Sorcerer needs to be level 18 first")

	def list_draconic_options(self):
		selection = int(input("What action are you counting?\n" + "[1]: Create Spell Slot\n" + (

			"[2]: Create Sorcery Point\n" + "[3]: Use Careful Spell\n" + "[4]: Use Distant Spell\n" +

			"[5]: Use Empowered Spell \n" + "[6]: Use Extended Spell\n" + "[7]: Use Heightened Spell\n" +

			"[8]: Use Quickened Spell\n" + "[9]Use Subtle Spell\n" + "[10]: Use Twinned Spell\n" +

			"[11]: Use Sorcerous Restoration\n" + "[12]: Use Elemental Affinity" + "[13]: Use Dragonic Presence" +

			"[14]: Use Hit Dice\n" + "[15]: Change Level\n" + (
				"[16]: Exit\n"))))

		if selection == 1:
			self.create_spell_slot()
		elif selection == 2:
			self.create_sorcery_points()
		elif selection == 3:
			self.use_careful_spell()
		elif selection == 4:
			self.use_distant_spell()
		elif selection == 5:
			self.use_empowered_spell()
		elif selection == 6:
			self.use_extended_spell()
		elif selection == 7:
			self.use_heightened_spell()
		elif selection == 8:
			self.use_quickened_spell()
		elif selection == 9:
			self.use_subtle_spell()
		elif selection == 10:
			self.use_twinned_spell()
		elif selection == 11:
			self.use_sorcerous_restoration()
		elif selection == 12:
			self.elemental_affinity_resistance()
		elif selection == 13:
			self.use_draconic_presence()
		elif selection == 14:
			self.use_hit_dice()
		elif selection == 15:
			self.set_level()
			self.set_hit_dice(self.get_level())
		elif selection == 16:
			print("Leaving")
			return

class Wild_Magic(Sorcerer):
	def __init__(self):
		tides_of_chaos = False
		Sorcerer.__init__(self)

	def use_bend_luck(self):
		self.use_sorcery_point(2)
		print("Used bend luck")

