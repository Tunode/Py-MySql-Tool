import os
import time
import mysqltool1
import json
from mysqltool1 import mysql_tool
from getpass import getpass

class gui:

	def __init__(self,version,color):
		self.version = version
		self.color = color
		self.sql = mysql_tool()

	def ask_loggin_details(self):
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		password = getpass(prompt="-| Password: ")
		print("")
		self.os_fix()
		return password

	def os_fix(self): #Changes terminal color to green, Changes terminal title + Clear's Terminal.
		if self.color == "0":
			self.status = "color "
		else:
			self.status = f"color {self.color}"
		os.system(f"{self.status}")
		os.system(f"title MYSQL_TOOL_{self.version}")
		os.system('cls')

	def main_menu(self): #Prints Main Menu.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		print("- 1 -| Connect to MySQL server ")
		print("- 2 -| Settings ")
		print("- 3 -| Close ")
		print("")
		mm_select = input("-| Select: ")
		self.os_fix()
		return mm_select

	def message(self,message): #Prints inputted: message.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		print(f" {message} ")
		print("")
		input("-| Continue: ")
		#time.sleep(3)
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
			"sql_database": "db"
		}
		self.os_fix()
		return mysql_loggin_data
		
	def db_menu(self): # Prints submenu when connected to database.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		print("- 1 -| Select database to altter. ")
		print("- 2 -| Remove database ")
		print("- 3 -| Create new database ")
		print("- 4 -| Close ")
		print("")
		mm_select = input("-| Select: ")
		self.os_fix()
		return mm_select

	def switch_color_menu(self):
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		headline=(f"-| Select color ")
		print(headline)
		print("")
		print("-| Warning if you change color, app will restart it self! ")
		print("")
		print(len(headline)*"-")
		print(f"- 0 -| White ")
		print(f"- 1 -| Dark blue ")
		print(f"- 2 -| Dark green (Default)")
		print(f"- 3 -| Light blue ")
		print(f"- 4 -| Red ")
		print(f"- 5 -| Purple ")
		print(f"- 6 -| Orange ")
		print(len(headline)*"-")
		print("")
		svm_select = input("-| Select: ")
		self.os_fix()
		return svm_select

	def settings_menu(self): # Prints settings.

		def option_status(option_s):
			if option_s == "on":
				status = "[X]"
			if option_s == "off":
				status = "[]"
			return status

		def color_status(color_s):
			if color_s == "0":
				status = "[White]"
			if color_s == "1":
				status = "[Dark blue]"
			if color_s == "2":
				status = "[Dark green]"
			if color_s == "3":
				status = "[Light blue]"
			if color_s == "4":
				status = "[Red]"
			if color_s == "5":
				status = "[Purple]"
			if color_s == "6":
				status = "[Orange]"
			return status

		self.os_fix()
		settings = json.load(open("settings.json"))
		setting_1 = settings.get("1")
		setting_2 = settings.get("2")
		setting_3 = settings.get("3")
		setting_4 = settings.get("4")
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		print(" [] = OFF | [X] = ON ")
		print("")
		print(f"- 1 -| Remember last session: {option_status(setting_1)} ")
		print(f"- 2 -| Confirm before leave current menu: {option_status(setting_2)} ")
		print(f"- 3 -| Change color: {color_status(setting_3)} ")
		print(f"- 4 -| Advanced mode: {option_status(setting_4)} ")
		print(f"- 5 -| Close ")
		print("")
		mm_select = input("-| Select: ")
		self.os_fix()
		return mm_select

	def alter_db_v2(self):
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]	
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		headline=(f"-| Current database: {current_database_name} |- ")
		print(headline)
		print("-| Select What to altter |- ")
		print(len(headline)*"-")
		print("- 1 -| Tables ")
		print("- 2 -| Columns ")
		print("- 3 -| Manual Query ")
		print("- 4 -| Close ")
		print(len(headline)*"-")
		mm_select = input("-| Select: ")
		self.os_fix()
		return mm_select

	def alter_db(self): #Show's all DB alltering settings.
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]	
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		headline=(f"- Current database: {current_database_name}")
		print(headline)
		print(len(headline)*"-")
		print("-| Table |- ")
		print("- 1 -| Add ")
		print("- 2 -| Remove ")
		print("- 3 -| List ")
		print(len(headline)*"-")
		print("-| Column |- ")
		print("- 4 -| Add ")
		print("- 5 -| Remove ")
		print("- 6 -| List ")
		print(len(headline)*"-")
		print("- 7 -| Close ")
		print(len(headline)*"-")
		mm_select = input("-| Select: ")
		self.os_fix()
		return mm_select

	def multiple_DB_menu(self, db_list): #Check's if MySQL server have multiple DB's.
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		message=(f"-| Select DB |-")
		print(message)
		print("-"*len(message))
		x = 0
		for idx, db in enumerate(db_list, start=1):
			print(f"- {idx} -|{db[x]}")
			x + 1
		print("-"*len(message))
		print("-| To return, leave selection blank ")	
		menu_selection = input("-| Select: ") 
		if menu_selection.isdigit():
			x = db_list[int(menu_selection)-1]
			y = len(str(x))
			z = y - 3
			return str(x)[2:z]
		else:
			return menu_selection

	def remove_db(self, db_list): #Ask from user what is name for database to remove.
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		headline=("-| List of current databases: ")
		print(headline)
		print(len(headline)*"-")
		for db in db_list:
			x = 0
			print(f"-|{db[x]}")
			x + 1
		print(len(headline)*"-")
		print("-| To return, leave selection blank ")
		self.remove_db_name = input("-| Name of database to remove: ")
		return self.remove_db_name
		self.os_fix()

	def altter_tables(self, table_list):
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]	
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		message=(f"-| Current tables in database: {current_database_name} |-")
		print(message)
		print("-"*len(message))
		x = 0
		for table in table_list:
			print(f"-| {table[x]} ")
			x + 1
		print("-"*len(message))
		print("-| Altter tables |- ")
		print("- 1 -| Add ")
		print("- 2 -| Remove ")
		alter_table_ms=input("-| Select: ")
		self.os_fix()
		return alter_table_ms

	def altter_columns(self, table_list):
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]	
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		message=(f"-| Current tables in database: {current_database_name} |-")
		print(message)
		print("-"*len(message))
		x = 0
		for table in table_list:
			print(f"-| {table[x]} ")
			x + 1
		print("-"*len(message))
		print("-| Altter Columns |- ")
		print("- 1 -| Add ")
		print("- 2 -| Remove ")
		alter_columns_ms=input("-| Select: ")
		self.os_fix()
		return alter_columns_ms

	def add_table(self,table_list): #Asks from user what name wanted to new table.
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]	
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		message=(f"-| Current tables in database: {current_database_name} |-")
		print(message)
		print("-"*len(message))
		x = 0
		for table in table_list:
			print(f"-| {table[x]} ")
			x + 1
		print("-"*len(message))
		print("-| To return, leave selection blank ")
		self.add_table_name = input("-| Name of table to add: ")
		self.os_fix()
		return self.add_table_name

	def remove_table(self,table_list): #Asks from user what name wanted to new table.
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]	
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		message=(f"-| Current tables in database: {current_database_name} |-")
		print(message)
		print("-"*len(message))
		x = 0
		for table in table_list:
			print(f"-| {table[x]} ")
			x + 1
		print("-"*len(message))
		print("-| To return, leave selection blank ")
		self.remove_table_name = input("-| Name of table to remove: ")
		self.os_fix()
		return self.remove_table_name

	def add_column(self,table_list): #Asks from user what name wanted to new column.
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]
		self.sql.db_connector_new(loggin_details)
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		message=(f"-| Current tables in database: {current_database_name} |-")
		print(message)
		print("-"*len(message))
		x = 0
		for table in table_list:
			print(f"-| {table[x]} ")
			x + 1
		print("-"*len(message))
		print("-| To return, leave selection blank ")
		table_to_conn = input("-| Name of table to add column: ")
		self.os_fix()
		if table_to_conn == "":
			return table_to_conn
		else:
			column_list = self.sql.show_columns(table_to_conn)
			print(f"-- MYSQL_TOOL_{self.version} --")
			print("")
			message=(f"-| Current columns in table: {table_to_conn} in current database of: {current_database_name} |-")
			print(message)
			print("-"*len(message))
			x = 0
			for column in column_list:
				print(f"-| {column[x]} ")
				x + 1
			print("-"*len(message))
			print("-| To return, leave selection blank ")
			self.sql.close_connection()
			add_column_name = input("-| Name of column to add: ")
			if add_column_name == "":
				return add_column_name
			else:
				add_column_data ={
					"sql_new_column": add_column_name,
					"sql_table_to_conn": table_to_conn
				}
				self.os_fix()
				return add_column_data

	def remove_column(self,table_list): #Asks from user what is name for column to remove.
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]
		self.sql.db_connector_new(loggin_details)
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		message=(f"-| Current tables in database: {current_database_name} |-")
		print(message)
		print("-"*len(message))
		x = 0
		for table in table_list:
			print(f"-| {table[x]} ")
			x + 1
		print("-"*len(message))
		print("-| To return, leave selection blank ")
		table_to_conn = input("-| Name of table from remove column: ")
		self.os_fix()
		if table_to_conn == "":
			return table_to_conn
		else:
			column_list = self.sql.show_columns(table_to_conn)
			print(f"-- MYSQL_TOOL_{self.version} --")
			print("")
			message=(f"-| Current columns in table: {table_to_conn} in current database of: {current_database_name} |-")
			print(message)
			print("-"*len(message))
			x = 0
			for column in column_list:
				print(f"-| {column[x]} ")
				x + 1
			print("-"*len(message))
			print("-| To return, leave selection blank ")
			self.sql.close_connection()
			remove_column_name = input("-| Name of column to remove: ")
			if remove_column_name == "":
				return remove_column_name
			else:
				remove_column_data ={
					"sql_remove_column": remove_column_name,
					"sql_table_to_conn": table_to_conn
				}
				self.os_fix()
				return remove_column_data

	def add_new_database(self,db_list): #Asks from user what name wanted for new database.
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		headline=("-| List of current databases: ")
		print(headline)
		print(len(headline)*"-")
		for db in db_list:
			x = 0
			print(f"-|{db[x]}")
			x + 1
		print(len(headline)*"-")
		print("-| To return, leave selection blank. ")
		add_database_name = input("-| Name of database to create: ")
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

'''
#Test Area:
sql = mysql_tool()
ui = gui("0.9.1.2")
sql.db_connector(ui.ask_mysql_server())
print(ui.multiple_DB_menu(sql.show_databases()))
'''