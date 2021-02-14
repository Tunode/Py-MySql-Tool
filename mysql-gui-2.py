import mysqltool1
import os

class gui:

	def os_fix(self): #Changes terminal color to green, Changes terminal title + Clear's Terminal.
		os.system("color 2")
		os.system("title MYSQL_TOOL_0.2")
		os.system('clear')

	def main_menu(self): #Main menu.
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
		return int(mm_select)

	def ask_mysql_server(self): #Ask mysql server loggin details.
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.hostip = input("MySQL_IP: ")
		self.username = input("MySQL_Ùsername: ")
		self.passwd = input("MySQL_Password: ")
		#ADD Functionality here.
		self.os_fix()
		
	def ask_mysql_server_and_db_name(self): #Ask mysql server loggin details + db name.
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.hostip = input("MySQL_IP: ")
		self.username = input("MySQL_Ùsername: ")
		self.passwd = input("MySQL_Password: ")
		self.db_name = input("MySQL_DB_Name: ")
		#ADD Functionality here.
		self.os_fix()

	def db_menu(self): #Altter of close DB Menu.
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		print("- 1 -| Altter existing DB? ")
		print("- 2 -| DB List ")
		print("- 3 -| Remove DB ")
		print("- 4 -| Create new DB ")
		print("- 5 -| Close ")
		print("")
		mm_select = input("- Valinta - |")
		self.os_fix()
		return int(mm_select)

	def alter_db(self): #Show's all DB alltering settings.
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
		return int(mm_select)

	def db_list(self):
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		#ADD Functionality here.
		db_list=""
		print("DB List:"+db_list)
		self.os_fix()

	def remove_db(self):
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.remove_db_name = input("Name of database to remove: ")
		#ADD Functionality here.
		self.os_fix()

	def add_table(self):
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.add_table_name = input("Name of table to add: ")
		#ADD Functionality here.
		self.os_fix()

	def add_column(self):
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.add_column_name = input("Name of column to add: ")
		#ADD Functionality here.
		self.os_fix()

	def remove_table(self):
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.remove_column_name = input("Name of table to remove: ")
		#ADD Functionality here.
		self.os_fix()

	def remove_column(self):
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.remove_column_name = input("Name of column to remove: ")
		#ADD Functionality here.
		self.os_fix()

	def new_db_name(self):
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.add_database_name = input("Name of database to Create: ")
		#ADD Functionality here.
		self.os_fix()

#Code:
gui=gui()

mm = True
while mm == True:
	mm_select = gui.main_menu()
	if mm_select == 1: #Connect to existing DB.
		gui.ask_mysql_server_and_db_name()
		db_m = True
		while db_m == True:
			dbm_select = gui.db_menu()
			if dbm_select == 1: #Alter DB
				alt_db = True
				while alt_db == True:
					adb_select = gui.alter_db()
					if adb_select == 1: #Add table.
						gui.add_table()
					if adb_select == 2: #Add column.
						gui.add_column()
					if adb_select == 3: #Remove table.
						gui.remove_table()
					if adb_select == 4: #Remove column.
						gui.remove_column()
					if adb_select == 5: #Close alter db.
						alt_db = False
			if dbm_select == 2: #DB list.
				gui.db_list()
			if dbm_select == 3: #Remove DB.
				gui.remove_db()
			if dbm_select == 4: #Create new DB_Menu.
				gui.new_db_name()
			if dbm_select == 5: #Close DB_Menu.
				db_m = False
	if mm_select == 2: #Create new DB.
		gui.ask_mysql_server()
		gui.new_db_name()
	if mm_select == 3: #DB List.
		gui.db_list()
	if mm_select == 4: #Remove DB.
		gui.remove_db()
	if mm_select == 5: #Close application.
		mm = False
