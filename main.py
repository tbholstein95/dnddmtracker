from Classes.subclasses.playerclasses.barbarian import *
from Classes.subclasses.playerclasses.bard import *
from Classes.subclasses.playerclasses.cleric import *
from Classes.subclasses.playerclasses.druid import *
from Classes.subclasses.playerclasses.fighter import *
from Classes.subclasses.playerclasses.monk import *
from Classes.subclasses.playerclasses.paladin import *
from Classes.subclasses.playerclasses.ranger import *
from Classes.subclasses.playerclasses.rogue import *
from Classes.subclasses.playerclasses.sorcerer import *
from Classes.subclasses.playerclasses.warlock import *
from Classes.subclasses.playerclasses.wizard import *
from Classes.playercharacter import *
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow , QPushButton , QWidget, QGridLayout, QAction, QLineEdit, QMessageBox, QLabel, QComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui
import sys


# VAR
player_dictionary = {}
lists = []


def main():
	global player_dictionary
	campaign_list = {}
	try:
		infile = open('campaigns', 'rb')
	except:
		create_campaign(campaign_list)

	else:
		campaign_list = pickle.load(infile)
		new_game_check = int_checker("[1]: New Party or [2]: Load Campaign")
		if new_game_check == 1:
			create_campaign(campaign_list)
		if new_game_check == 2:
			infile = open('campaigns', 'rb')
			new_dict = pickle.load(infile)
			infile.close()
			keys_list = list(campaign_list)
			print(keys_list)
			select = int_checker("What campaign to load?")
			values = campaign_list.values()
			values_list = list(values)
			player_dictionary = values_list[select - 1]

	while True:
		for x in range(len(player_dictionary)):
			print("[{}]:".format(x), list(player_dictionary.keys())[x])
		current_player_index = int_checker("Who are you modifying? ('Enter number')\n")
		current_player = list(player_dictionary.keys())[current_player_index]
		if current_player == "exit":
			print("Stopping")
			break
		# set current player
		current_mod = player_dictionary[f'{current_player}']["character"]
		player_dictionary[f'{current_player}']['new_options'](current_mod)


def character_class_select(player_name, player_dict):
	while True:
		player_class = input("What is this player's class?").capitalize()
		if player_class == "Barbarian":
			return main_barb_making(player_name, player_dict)
		if player_class == "Bard":
			return main_bard_making(player_name, player_dict)
		if player_class == "Cleric":
			return main_cleric_making(player_name, player_dict)
		if player_class == "Druid":
			return main_druid_making(player_name, player_dict)
		if player_class == "Fighter":
			return main_fighter_making(player_name, player_dict)
		if player_class == "Monk":
			return main_monk_making(player_name, player_dict)
		if player_class == "Paladin":
			return main_paladin_making(player_name, player_dict)
		if player_class == "Ranger":
			return main_ranger_making(player_name, player_dict)
		if player_class == "Rogue":
			return main_rogue_making(player_name, player_dict)
		if player_class == "Sorcerer":
			return main_sorcerer_making(player_name, player_dict)
		if player_class == "Warlock":
			return main_warlock_making(player_name, player_dict)
		if player_class == "Wizard":
			return main_wizard_making(player_name, player_dict)


def create_campaign(campaign_list):
	campaign_name = input("What is the name of your campaign?")
	filename = 'campaigns'
	outfile_campaign_list = open(filename, 'wb')
	number_of_players = int_checker("How many players are in this party?")
	for x in range(number_of_players):
		player_name = input("What is this player's name?")
		character_class_select(player_name, player_dictionary)
	campaign_list[
		('[{}]: '.format(len(campaign_list) + 1) + '{}'.format(campaign_name))] = player_dictionary

	pickle.dump(campaign_list, outfile_campaign_list)
	outfile_campaign_list.close()


def app_create_campaign(campaign_list, campaign_name):
	filename = 'campaigns'
	outfile_campaign_list = open(filename, 'wb')
	campaign_list[
		('[{}]: '.format(len(campaign_list) + 1) + '{}'.format(campaign_name))] = player_dictionary

	pickle.dump(campaign_list, outfile_campaign_list)
	outfile_campaign_list.close()


class CharacterGenerationWindow(QWidget):
	def __init__(self, parent=None):
		super(CharacterGenerationWindow, self).__init__(parent)
		self.setLayout(QGridLayout())
		self.campaign_dict = {}
		self.campaign_name = ''
		self.campaign_label = QLabel(self)
		self.no_players = QLabel(self)

		self.layout().addWidget(self.campaign_label, 1,0,)
		self.layout().addWidget(self.no_players, 1,1)

		self.character_name_label = QLabel(self)
		self.character_name_label.setText("Character: Name")
		self.character_name_box = QLineEdit(self)

		self.layout().addWidget(self.character_name_label, 1, 0, 1, 1)
		self.layout().addWidget(self.character_name_box, 1, 1, 1, 1)

		self.character_class_label = QLabel(self)
		self.character_class_label.setText('Class Select')
		self.character_class_drop = QComboBox(self)
		self.character_class_drop.addItem("Select Player's Class")
		self.character_class_drop.addItem("Barbarian")
		self.character_class_drop.addItem("Bard")
		self.character_class_drop.addItem("Cleric")

		self.level_drop_label = QLabel(self)
		self.level_drop_label.setText('Set Level')
		self.level_drop = QComboBox(self)
		for x in range(1, 21):
			self.level_drop.addItem(str(x))


		self.save_character_button = QPushButton("Save Character", self)
		self.finish_button = QPushButton("Finish", self)
		self.layout().addWidget(self.save_character_button, 3,1,1,2)
		self.layout().addWidget(self.finish_button, 3,5,1,1)
		self.layout().addWidget(self.character_class_label,2,0,1,1)
		self.layout().addWidget(self.character_class_drop,2,1,1,3)
		self.layout().addWidget(self.level_drop_label, 2,4,1,1)
		self.layout().addWidget(self.level_drop, 2,5,1,1)




		self.character_class_drop.currentIndexChanged.connect(self.on_Changed)

		self.save_character_button.clicked.connect(self.submit_character)
		self.finish_button.clicked.connect(self.submit_campaign)

		self.subclass = ''

	def on_Changed(self, i):
		if self.character_class_drop.currentText() == "Barbarian":
			barbarian_label = QLabel(self)
			barbarian_label.setText = "Choose Barbarian SubClass"
			barbarian_drop = QComboBox(self)
			barbarian_drop.addItem("Berserker")
			self.subclass = 'Berserker'
			self.layout().addWidget(barbarian_label,3,0)
			self.layout().addWidget(barbarian_drop,3,0)

		print("Items in the list are :")
		for count in range(self.character_class_drop.count()):
			print(self.character_class_drop.itemText(count))
		print("Current index", i, "selection changed ", self.character_class_drop.currentText())

	def submit_character(self):
		print("did i do it")
		if self.character_class_drop.currentText() == "Barbarian":
			print("hey man")
			print(self.character_name_box.text())
			print(player_dictionary)
			print(self.subclass)
			print(self.level_drop.currentText())
			app_main_barb_making(self.character_name_box.text(), player_dictionary, self.subclass, int(self.level_drop.currentText()))
		print(player_dictionary)

	def submit_campaign(self):
		campaign_list = {}
		try:
			infile = open('campaigns', 'rb')
		except:
			print("excepted submit campaign")
			campaign_name = self.newCampaignWindow.campaignNameBox.text()
			app_create_campaign(self.campaign_dict, self.campaign_name)

		else:
			print(self.campaign_name)
			app_create_campaign(self.campaign_dict, self.campaign_name)


class CampaignOverviewWindow(QWidget):
	def __init__(self, parent=None):
		global player_dictionary
		super(CampaignOverviewWindow, self).__init__(parent)
		self.setLayout(QGridLayout())
		self.dicti = get_campaign_list()
		self.keys_list = list(self.dicti)
		z = 0
		for i in range(len(self.keys_list)):
			self.btn = QPushButton('{}'.format(self.keys_list[i]), self)
			text = self.btn.text()
			# self.btn.clicked.connect(lambda ch, text=text: print("\n{}".format(text)))
			ind = self.keys_list.index(text)
			val = self.dicti.values()
			self.values_list = list(val)
			# self.btn.clicked.connect(lambda ch, ind=ind: print("\n{}".format(ind + 1)))
			self.btn.clicked.connect(lambda ch, ind=ind: self.set_player_dict(self.values_list[ind]))
			self.layout().addWidget(self.btn, z, 1)
			z += 3
		self.submit_button = QPushButton("Select", self)
		self.layout().addWidget(self.submit_button, 100, 1)

	def set_player_dict(self, item):
		global player_dictionary
		player_dictionary = item
		print(player_dictionary)


class SelectedCampaignWindow(QWidget):
	def __init__(self, parent=None):
		super(SelectedCampaignWindow, self).__init__(parent)
		self.setLayout(QGridLayout())
		z = 0
		for k, v in player_dictionary.items():
			print(k, "hey big man")
			print(player_dictionary['{}'.format(k)]['new_options'])
			character_name = QLabel('{}'.format(k))

			current_mod = player_dictionary[f'{k}']["character"]
			print("fraklin the tophat wearin turtle")
			print(current_mod, current_mod)
			print(player_dictionary[f'{k}']['new_options'])
			x = player_dictionary[f'{k}']['new_options']()
			for a in x:
				print(a, x[a])


			# current_mod = player_dictionary[f'{current_player}']["character"]
			# player_dictionary[f'{current_player}']['new_options'](current_mod)


			self.layout().addWidget(character_name, 0, z, 1, 1)
			z += 3


class NewCampaignWindow(QWidget):

	def __init__(self, parent=None):
		super(NewCampaignWindow, self).__init__(parent)
		self.setLayout(QGridLayout())

		self.backBTN = QPushButton('Back', self)
		self.backBTN.move(50, 350)

		self.nameLabel_campaignName = QLabel(self)
		self.nameLabel_campaignName.setText('Campaign Name:')
		self.campaignNameBox = QLineEdit(self)
		self.submit_CampaignName = QPushButton("Submit")


		self.layout().addWidget(self.nameLabel_campaignName, 1,0,1,1)
		self.layout().addWidget(self.campaignNameBox, 1,1,1,1)


		self.layout().addWidget(self.submit_CampaignName,3,2,1,1)

		self.layout().addWidget(self.backBTN, 3,0,1,1)


class CampaignMenu(QWidget):
	def __init__(self, parent=None):
		super(CampaignMenu, self).__init__(parent)
		self.new_campaign_button = QPushButton("New Campaign", self)
		self.load_campaign_button = QPushButton("Load Campaign", self)
		self.setLayout(QGridLayout())
		self.layout().addWidget(self.new_campaign_button, 1,0,1,1)
		self.layout().addWidget(self.load_campaign_button, 2,0,1,1)


class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setGeometry(50, 50, 400, 450)
		self.setFixedSize(900, 900)
		self.campaign_list = {}
		try:
			infile = open('campaigns', 'rb')
			self.campaign_list = pickle.load(infile)
			print("Loaded")
			keys_list = list(self.campaign_list)
			print(keys_list)
			values = self.campaign_list.values()
			values_list = list(values)
			print(values_list)
			infile.close()
		except:
			filename = 'campaigns'
			infile = open('campaigns', 'rb')
			self.campaign_list = pickle.load(infile)
			print("Excepted in main")

		self.startcampaignmenu()



	def startcampaignmenu(self):
		self.campaignMenu = CampaignMenu(self)
		self.setWindowTitle("DNDMTracker")
		self.setCentralWidget(self.campaignMenu)
		self.campaignMenu.new_campaign_button.clicked.connect(self.startNewCampaignWindow)
		self.campaignMenu.load_campaign_button.clicked.connect(self.startCampaignOverviewWindow)
		self.show()

	def startNewCampaignWindow(self):
		self.newCampaignWindow = NewCampaignWindow(self)
		self.setWindowTitle("New Campaign")
		self.setCentralWidget(self.newCampaignWindow)
		self.newCampaignWindow.backBTN.clicked.connect(self.startcampaignmenu)
		self.newCampaignWindow.submit_CampaignName.clicked.connect(self.startCharacterGenerationWindow)
		self.show()

	def startCharacterGenerationWindow(self):
		self.charactergenerationwindow = CharacterGenerationWindow(self)
		campaign_name = self.newCampaignWindow.campaignNameBox.text()
		self.charactergenerationwindow.campaign_name = campaign_name
		self.charactergenerationwindow.campaign_dict = self.campaign_list
		self.setWindowTitle("Characters in the {} campaign".format(campaign_name))
		self.setCentralWidget(self.charactergenerationwindow)
		self.charactergenerationwindow.finish_button.clicked.connect(self.startCampaignOverviewWindow)
		self.show()

	def startCampaignOverviewWindow(self):
		self.campaign_overview_window = CampaignOverviewWindow(self)
		self.setCentralWidget(self.campaign_overview_window)
		self.campaign_overview_window.submit_button.clicked.connect(self.startSelectedCampaignWindow)
		self.show()

	def startSelectedCampaignWindow(self):
		self.selected_campaign_window = SelectedCampaignWindow(self)
		self.setCentralWidget(self.selected_campaign_window)
		self.show()


def get_campaign_list():
	infile = open('campaigns', 'rb')
	franklin = pickle.load(infile)
	infile.close()
	chooch = list(franklin)
	print(franklin)
	return franklin



if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())
	main()
