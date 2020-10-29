from Classes.playercharacter import *
rogue_dict = {}

class Rogue(PlayerCharacter):

	def __init__(self):
		self.stroke_of_luck = False
		PlayerCharacter.__init__(self)

	def get_stroke_of_luck(self):
		return self.stroke_of_luck

	def use_stroke_of_luck(self):
		if not self.get_stroke_of_luck():
			print("Used Stroke of Luck")
			self.stroke_of_luck = False
		else:
			print("Can't use Stroke of Luck until end of short of long rest")

## Todo: Arcane Trickster (after half-caster)