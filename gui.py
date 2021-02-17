import os

class gui:

	def os_fix(self): #Changes terminal color to green, Changes terminal title + Clear's Terminal.
		os.system("color 2")
		os.system("title MYSQL_TOOL_0.2")
		os.system('cls')

	def main_menu(self): #Prints Main Menu.
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

	def ask_mysql_server(self): #Ask mysql server loggin details to connect.
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.hostip = input("MySQL_IP: ")
		self.username = input("MySQL_Ùsername: ")
		self.passwd = input("MySQL_Password: ")
		#ADD Functionality here.
		self.os_fix()
		
	def ask_mysql_server_and_db_name(self): #Ask mysql server loggin details + db name to connect.
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.hostip = input("MySQL_IP: ")
		self.username = input("MySQL_Ùsername: ")
		self.passwd = input("MySQL_Password: ")
		self.db_name = input("MySQL_DB_Name: ")
		#ADD Functionality here.
		self.os_fix()

	def db_menu(self): # Prints submenu when connected to database.
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
		return mm_select

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
		return mm_select

	def db_list(self, db_list):#Prints text wiew for lists of databases in mysql server.
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		print("DB List:"+db_list)
		self.os_fix() 

	def remove_db(self): #Ask from user what is name for database to remove.
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.remove_db_name = input("Name of database to remove: ")
		self.os_fix()
		return remove_db_name 

	def add_table(self): #Asks from user what name wanted to new table.
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.add_table_name = input("Name of table to add: ")
		#ADD Functionality here.
		self.os_fix()
		return add_table_name

	def add_column(self): #Asks from user what name wanted to new column.
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.add_column_name = input("Name of column to add: ")
		self.os_fix()
		return add_column_name

	def remove_table(self): #Asks from user what is name for table to remove.
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.remove_table_name = input("Name of table to remove: ")
		self.os_fix()
		return remove_table_name

	def remove_column(self): #Asks from user what is name for column to remove.
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.remove_column_name = input("Name of column to remove: ")
		self.os_fix()
		return remove_column_name

	def new_db_name(self): #Asks from user what name wanted for new database.
		self.os_fix()
		print("-- MYSQL_TOOL_0.2 --")
		print("")
		self.add_database_name = input("Name of database to Create: ")
		self.os_fix()
		return add_database_name

#Test Area:
