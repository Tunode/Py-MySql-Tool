import os
import time
import mysqltool1
import json
from mysqltool1 import mysql_tool
from getpass import getpass

class gui:

	def __init__(self,version):
		self.version = version

	def ask_loggin_details(self):
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		password = getpass(prompt="- Password -:")
		print("")
		self.os_fix()
		return password


	def os_fix(self): #Changes terminal color to green, Changes terminal title + Clear's Terminal.
		os.system("color 2")
		os.system(f"title MYSQL_TOOL_{self.version}")
		os.system('cls')

	def main_menu(self): #Prints Main Menu.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		print("- 1 -| Connect to existing DB ")
		print("- 2 -| Create new DB ")
		print("- 3 -| Settings ")
		print("- 4 -| Close ")
		print("")
		mm_select = input("- Valinta - |")
		self.os_fix()
		return mm_select

	def message(self,message): #Prints inputted: message.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		print(f" {message} ")
		print("")
		time.sleep(3)
		self.os_fix()

	def ask_mysql_server(self): #Ask mysql server loggin details to connect.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		hostip = input("MySQL_IP: ")
		username = input("MySQL_Ùsername: ")
		passwd = input("MySQL_Password: ")
		mysql_loggin_data ={
			"sql_ip": hostip,
			"sql_username": username,
			"sql_password": passwd,
			"sql_database": "db_name"
		}
		self.os_fix()
		return mysql_loggin_data
		
	def ask_mysql_server_and_db_name(self): #Ask mysql server loggin details + db name to connect.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		hostip = input("MySQL_IP: ")
		username = input("MySQL_Ùsername: ")
		passwd = input("MySQL_Password: ")
		db_name = input("MySQL_DB_Name: ")
		mysql_loggin_data ={
			"sql_ip": hostip,
			"sql_username": username,
			"sql_password": passwd,
			"sql_database": db_name
		}
		self.os_fix()
		return mysql_loggin_data

	def db_menu(self): # Prints submenu when connected to database.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
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

	def settings_menu(self): # Prints settings.
		self.os_fix()

		def load_settings():
			settings = json.load(open("settings.json"))
			return settings

		def option_status(option_s):
			if option_s == "on":
				status = "[X]"
			if option_s == "off":
				status = "[]"
			return status

		settings = load_settings()
		setting_1 = settings.get("1")
		setting_2 = settings.get("2")
		setting_3 = settings.get("3")
		setting_4 = settings.get("4")

		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		print(" [] = OFF | [X] = ON ")
		print("")
		print(f"- 1 -| Remember last session: {option_status(setting_1)} ")
		print(f"- 2 -| Confirm before leave menu: {option_status(setting_2)} ")
		print(f"- 3 -| Change Color: {option_status(setting_3)} ")
		print(f"- 4 -| Advanced Mode: {option_status(setting_4)} ")
		print(f"- 5 -| Close ")
		print("")
		mm_select = input("- Valinta - |")
		self.os_fix()
		return mm_select

	def alter_db(self): #Show's all DB alltering settings.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
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

	def multiple_DB_menu(self, db_list): #Check's if MySQL server have multiple DB's.
		print(f"-| Select DB |-")
		print("")
		x = 0
		for idx, db in enumerate(db_list, start=1):
			print(f"- {idx} -|{db[x]}")
			x + 1
		print("")
		menu_selection= int(input("Choice: ")) - 1
		return db_list[menu_selection]

	def db_list(self, db_list):#Prints text wiew for lists of databases in mysql server.
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		print("-| DB List: ")
		print("------------")
		for db in db_list:
			x = 0
			print(f"-|{db[x]}")
			x + 1 
		time.sleep(5)
		self.os_fix()

	def remove_db(self): #Ask from user what is name for database to remove.
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		self.remove_db_name = input("Name of database to remove: ")
		return self.remove_db_name
		self.os_fix()

	def add_table(self): #Asks from user what name wanted to new table.
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		self.add_table_name = input("Name of table to add: ")
		return self.add_table_name
		self.os_fix()

	def add_column(self): #Asks from user what name wanted to new column.
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		add_column_name = input("Name of column to add: ")
		table_to_conn = input("Name of table to add column: ")
		add_column_data ={
			"sql_new_column": add_column_name,
			"sql_table_to_conn": table_to_conn
		}
		self.os_fix()
		return add_column_data

	def remove_table(self): #Asks from user what is name for table to remove.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		self.remove_table_name = input("Name of table to remove: ")
		self.os_fix()
		return self.remove_table_name

	def remove_column(self): #Asks from user what is name for column to remove.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		self.remove_column_name = input("Name of column to remove: ")
		self.os_fix()
		return self.remove_column_name

	def new_db_name(self): #Asks from user what name wanted for new database.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		add_database_name = input("Name of database to Create: ")
		self.os_fix()
		return add_database_name

	def ask_if_close(self, name_of_menu_to_close): #Asks form user if sure want to close menu.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print(f"-| You sure that you want to close {name_of_menu_to_close}? ")
		print(f"-| yes / no ")
		ask_if_close = input("-| Select: ")
		self.os_fix()
		return ask_if_close



#Test Area:
sql = mysql_tool()
ui = gui("0.9.1.2")
sql.db_connector(ui.ask_mysql_server_and_db_name())
print(ui.multiple_DB_menu(sql.show_databases()))