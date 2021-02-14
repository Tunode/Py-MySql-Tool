import os

class gui:

	def os_fix(self):
		os.system("title MYSQL_TOOL_0.2")
		os.system('clear')

	def Main_Menu(self):
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		print("- 1 -| Connect to existing DB? ")
		print("- 2 -| Create new DB? ")
		print("- 3 -| DB List ")
		print("- 4 -| Remove DB ")
		print("- 5 -| Close ")
		print("")
		mm_select = input("- Valinta - |")
		self.os_fix()
		return mm_select

	def DB_Menu(self):
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		print("- 1 -| Altter existing DB? ")
		print("- 2 -| Close ")
		print("")
		mm_select = input("- Valinta - |")
		self.os_fix()
		return mm_select

	def Alter_DB(self):
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		print("- 1 -| Add table ")
		print("- 2 -| Add Column ")
		print("- 3 -| Remove Table ")
		print("- 4 -| Remove Column ")
		print("- 5 -| Close ")
		print("")
		mm_select = input("- Valinta - |")
		self.os_fix()
		return mm_select



#Code:
gui=gui()

gui.Main_Menu()
gui.DB_Menu()
gui.Alter_DB()