import PyQt5.QtWidgets as qtw

class NewCampaignWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Create New Campaign')
		self.setLayout(qtw.QVBoxLayout())
		self.keypad()
		self.show()

	def options(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		btn_new = qtw.QPushButton('New', clicked = main)
		btn_load = qtw.QPushButton('Load')

		container.layout().addWidget(btn_new, 0, 0, 1, 4)
		container.layout().addWidget(btn_load, 1, 0, 1, 4)
		self.layout().addWidget(container)