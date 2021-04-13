#Imports:
from getpass import getpass
import mysql.connector
from mysql.connector import errorcode
import json
import os

#Classes:

class mysql_tool: #MYSQL Handling class.

	def manual_query(self,manual_query):
		DBCursor = self.DB.cursor()
		DBCursor.execute(f"{manual_query}")

	def db_connector_new(self, conn_new_data):#Connects mysql without DB name: (this is for gen_db functionality) -> done
		host_ip = conn_new_data["sql_ip"]
		db_username = conn_new_data["sql_username"]
		db_passwd = conn_new_data["sql_password"]
		self.DB = mysql.connector.connect(
			host = host_ip,
			user = db_username,
			passwd = db_passwd
			)

	def db_connector(self, conn_to_db):#Connetcs with excisting DB -> Done
		host_ip = conn_to_db["sql_ip"]
		db_username = conn_to_db["sql_username"]
		db_passwd = conn_to_db["sql_password"]
		db_name = conn_to_db["sql_database"]
		self.DB = mysql.connector.connect(
			host = host_ip,
			user = db_username,
			passwd = db_passwd,
			database = db_name
			)

	def close_connection(self):#Simply closes DB Connection -> Done
		self.DB.close()

	def gen_db(self, dbname): #Create Database -> Done
		DBCursor = self.DB.cursor()
		DBCursor.execute("CREATE DATABASE "+dbname)

	def gen_table(self, tablename): #Create Table with DataID column -> Done
		DBCursor = self.DB.cursor()
		DBCursor.execute("CREATE TABLE IF NOT EXISTS "+ tablename +"(dataID int PRIMARY KEY AUTO_INCREMENT)")

	def add_column(self, add_column_data): #Add Column in selected exsisting Table. -> Done
		table_name = add_column_data["sql_table_to_conn"]
		column_name = add_column_data["sql_new_column"]
		DBCursor = self.DB.cursor()
		DBCursor.execute("ALTER TABLE " + " " + table_name + " ADD " "(" + column_name + " VARCHAR(255))")

	def show_databases(self): #Prints list of databases in MYSQL server. -> Done.
		DBCursor = self.DB.cursor()
		DBCursor.execute("SHOW DATABASES")
		l = DBCursor.fetchall()
		return l

	def show_tables(self,):
		loggin_details = json.load(open("logging_details.json"))
		current_database = loggin_details["sql_database"]
		DBCursor = self.DB.cursor()
		DBCursor.execute(f"USE {current_database}")
		DBCursor.execute("SHOW TABLES")
		tables = DBCursor.fetchall()
		return tables

	def show_columns(self,current_table):
		loggin_details = json.load(open("logging_details.json"))
		current_database = loggin_details["sql_database"]
		DBCursor = self.DB.cursor()
		DBCursor.execute(f"USE {current_database}")
		DBCursor.execute(f"SHOW COLUMNS FROM {current_table}")
		columns = DBCursor.fetchall()
		return columns

	def delete_db(self, database_name): #Simply removes DB from MYSQL server -> Done
		DBCursor = self.DB.cursor()
		DBCursor.execute("DROP DATABASE "+database_name)
		self.close_connection()

	def delete_table(self, table_name): #Delete's table from DB you wish. -> Done
		loggin_details = json.load(open("logging_details.json"))
		self.db_connector(loggin_details)
		DBCursor = self.DB.cursor()
		DBCursor.execute("DROP TABLE "+table_name)
		self.close_connection()

	def delete_column(self, delete_column_data): #Delete column from Table you name in DB of your wish. -> Done
		table_name = delete_column_data["sql_table_to_conn"]
		column_name = delete_column_data["sql_remove_column"]
		DBCursor = self.DB.cursor()
		DBCursor.execute("ALTER TABLE "+table_name+ " DROP COLUMN "+column_name) 

class gui: #UI Handling class.

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
		self.os_fix()

	def manual_query(self):
		loggin_details = json.load(open("logging_details.json"))
		current_database_name = loggin_details["sql_database"]	
		self.os_fix()
		print(f"-- MYSQL_TOOL_{self.version} --")
		print("")
		headline=(f"-| Current database: {current_database_name} |- ")
		print(headline)
		print("")
		print("-| Manual query |- ")
		manual_query = input("-: ")
		#time.sleep(3)
		self.os_fix()
		return(manual_query)

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

		settings = json.load(open("settings.json"))
		if "4" in settings.keys():
			advanced_mode_status = settings.get("4")
		else:
			pass
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
		if advanced_mode_status == "on":
			print("- 3 -| Manual Query ")
			print("- 4 -| Close ")
		else:
			print("- 3 -| Close ")
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
			message2=(f"-| Current database of: {current_database_name} ")
			message=(f"-| Current columns in table: {table_to_conn} |-")
			print(message2)
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

#Variables/Functions--
def check_setting_status(setting_to_check): #Check inputted settings status and returns on/off.
	settings=load_settings()
	if setting_to_check in settings.keys():
		return settings.get(setting_to_check)

def change_setting(setting_to_change): #Changes inputted settings state from "off" to "on" or otherwise.
	settings = load_settings()
	if check_setting_status(setting_to_change) == "on":
		settings.update({f"{setting_to_change}": "off"})
		save_settings(settings)
	elif check_setting_status(setting_to_change) == "off":
		settings.update({f"{setting_to_change}": "on"})
		save_settings(settings)

def change_color_setting(new_color):
	settings=load_settings()
	settings.update({"3": f"{new_color}"})
	save_settings(settings)

def save_settings(settings): #saves settings.jason
	j = json.dumps(settings)
	with open("settings.json", "w") as f:
		f.write(j)
		f.close()

def load_settings(): #loads settings from settings.jason
	settings = json.load(open("settings.json"))
	return settings

def load_loggin_details(): #Loads MySQL server loggin details from loggin_details.jason
	loggin_details = json.load(open("logging_details.json"))
	return loggin_details

def save_loggin_details(logging_details): #Save alttered logging details to loggin_detail.jason
	j = json.dumps(logging_details)
	with open("logging_details.json", "w") as f:
		f.write(j)
		f.close()	

def change_logging_details(new_ip, new_sql_username, new_sql_password, new_sql_database): #Loads logging details from jason and replacese's them with new ones and then saves it.
	logging_details = load_loggin_details()
	logging_details.update({"sql_ip": f"{new_ip}"})
	logging_details.update({"sql_username": f"{new_sql_username}"})
	logging_details.update({"sql_password": f"{new_sql_password}"})
	logging_details.update({"sql_database": f"{new_sql_database}"})
	save_(logging_details)

def multiple_DB_slection(db_list):
	if len(db_list) > 1:
		M_DB_Menu_Selection = gui.multiple_DB_menu(db_list)
		if M_DB_Menu_Selection == "" or M_DB_Menu_Selection == "c" or M_DB_Menu_Selection == "C":
			return M_DB_Menu_Selection
		else:
			logging_details = load_loggin_details()
			logging_details.update({"sql_database": f"{M_DB_Menu_Selection}"})
			save_loggin_details(logging_details)
			return logging_details
	else:
		pass

#----
change_color = False
mm=True
settings = {
"1": "off",
"2": "off",
"3": "2",
"4": "off"
   }
logging_details = {
"sql_ip": "localhost",
"sql_username": "root",
"sql_password": "root",
"sql_database": "db"
   }

#Code--

try: #Create loggin logging_details.jason and add default loggin details.(if not created all ready.)
	logging_details_file=open("logging_details.json", "x")
	j = json.dumps(logging_details)
	with open("logging_details.json", "w") as f:
		f.write(j)
		f.close()
except:
	pass

try: #Create settings.jason and add default settings.(if not created all ready.)
	settings_file=open("settings.json", "x")
	j = json.dumps(settings)
	with open("settings.json", "w") as f:
		f.write(j)
		f.close()
except:
	pass

ui_color = check_setting_status("3")
gui = gui("0.9.5", ui_color)
sql = mysql_tool()


password = gui.ask_loggin_details()
if password == "":
	while mm == True:
		mm_select = gui.main_menu()
		if mm_select == "1": #Connect to MySql Server.
				try:
					if check_setting_status("1") == "off":
						log_details = gui.ask_mysql_server()
						save_loggin_details(log_details)
						sql.db_connector_new(log_details)
						db_m = True
					elif check_setting_status("1") == "on":
						sql.db_connector_new(load_loggin_details())
						db_m = True
				except mysql.connector.Error as err:
					gui.message(f"ERROR: {err}")
					db_m = False
				while db_m == True:
					dbm_select = gui.db_menu()
					if dbm_select == "1": #Open menu to Select database and then opens menu to altter selected database.						
						multiple_database_menu_selection = multiple_DB_slection(sql.show_databases())
						if multiple_database_menu_selection == "":
							alt_db = False
						else:
							try:
								sql.db_connector(multiple_database_menu_selection)
								alt_db = True
							except mysql.connector.Error as err:
								gui.message(f"ERROR: {err}")
								alt_db = False
							while alt_db == True:
								adb_select = gui.alter_db_v2()
								advance_mode_status = check_setting_status("4")
								if advance_mode_status == "on":
									if adb_select == "1": #Table list + options to alter it.
										try: 
											alter_tables_selection = gui.altter_tables(sql.show_tables())
											if alter_tables_selection == "": #Close alter
												pass
											if alter_tables_selection == "1": #Add Table
												add_table_selectino = gui.add_table(sql.show_tables())
												if add_table_selectino == "":
													pass
												else:
													sql.gen_table(add_table_selectino)
											if alter_tables_selection == "2": #Remove Table
													remvoe_table_selection = gui.remove_table(sql.show_tables())
													if remvoe_table_selection == "":
														pass
													else:
														sql.delete_table(remvoe_table_selection)
														sql.close_connection()
														sql.db_connector(load_loggin_details())
										except mysql.connector.Error as err:
												gui.message(f"ERROR: {err}")
									if adb_select == "2": #Column list + options to alter it.
										try:
											alter_columns_selection = gui.altter_columns(sql.show_tables())
											if alter_columns_selection == "": #Clos alttering columns.
												pass
											if alter_columns_selection == "1": #Add Column.
												add_column_selection = gui.add_column(sql.show_tables())
												if add_column_selection == "":
													pass
												else:
													sql.add_column(add_column_selection)
											if alter_columns_selection == "2": #Remove Column.
												remvoe_column_selection = gui.remove_column(sql.show_tables())
												if remvoe_column_selection == "":
													pass
												else:
													sql.delete_column(remvoe_column_selection)
										except mysql.connector.Error as err:
											gui.message(f"ERROR: {err}")
									if adb_select == "3": #Manual sql (Advanced)
										try:
											manual_query_input = gui.manual_query()
											if manual_query_input == "":
												pass
											else:
												gui.message(sql.manual_query(manual_query_input))
										except mysql.connector.Error as err:
											gui.message(f"ERROR: {err}")
									if adb_select == "4": #Close alter database menu.
										if check_setting_status("2") == "on":
											close_altter_db_menu = gui.ask_if_close("Altter database menu")
											if close_altter_db_menu == "y" or close_altter_db_menu == "Y" or close_altter_db_menu == "yes":
												alt_db = False
											else:
												alt_db = True
										else:	
											alt_db = False
								else:
									if adb_select == "1": #Table list + options to alter it.
										try: 
											alter_tables_selection = gui.altter_tables(sql.show_tables())
											if alter_tables_selection == "": #Close alter
												pass
											if alter_tables_selection == "1": #Add Table
												add_table_selectino = gui.add_table(sql.show_tables())
												if add_table_selectino == "":
													pass
												else:
													sql.gen_table(add_table_selectino)
											if alter_tables_selection == "2": #Remove Table
													remvoe_table_selection = gui.remove_table(sql.show_tables())
													if remvoe_table_selection == "":
														pass
													else:
														sql.delete_table(remvoe_table_selection)
														sql.close_connection()
														sql.db_connector(load_loggin_details())
										except mysql.connector.Error as err:
												gui.message(f"ERROR: {err}")
									if adb_select == "2": #Column list + options to alter it.
										try:
											alter_columns_selection = gui.altter_columns(sql.show_tables())
											if alter_columns_selection == "": #Clos alttering columns.
												pass
											if alter_columns_selection == "1": #Add Column.
												add_column_selection = gui.add_column(sql.show_tables())
												if add_column_selection == "":
													pass
												else:
													sql.add_column(add_column_selection)
											if alter_columns_selection == "2": #Remove Column.
												remvoe_column_selection = gui.remove_column(sql.show_tables())
												if remvoe_column_selection == "":
													pass
												else:
													sql.delete_column(remvoe_column_selection)
										except mysql.connector.Error as err:
											gui.message(f"ERROR: {err}")
									if adb_select == "3": #Close alter database menu.
										if check_setting_status("2") == "on":
											close_altter_db_menu = gui.ask_if_close("Altter database menu")
											if close_altter_db_menu == "y" or close_altter_db_menu == "Y" or close_altter_db_menu == "yes":
												alt_db = False
											else:
												alt_db = True
										else:	
											alt_db = False
					if dbm_select == "2": #Remove DB.
						remove_database_selection = gui.remove_db(sql.show_databases())
						if remove_database_selection == "":
							pass
						else:
							try:
								sql.delete_db(remove_database_selection)
								sql.close_connection()
								sql.db_connector_new(load_loggin_details())
							except mysql.connector.Error as err:
								gui.message(f"ERROR: {err}")
					if dbm_select == "3": #Create new DB_Menu.
						create_database_selection = gui.add_new_database(sql.show_databases())
						if create_database_selection == "":
							pass
						else:
							try:
								sql.gen_db(create_database_selection)
							except mysql.connector.Error as err:
								gui.message(f"ERROR: {err}")
					if dbm_select == "4": #Close DB_Menu.
						if check_setting_status("2") == "on":
							close_database_menu = gui.ask_if_close("Database menu")
							if close_database_menu == "y" or close_database_menu == "Y" or close_database_menu == "yes":
								db_m = False
							else:
								db_m = True
						db_m = False
		if mm_select == "2": #Open Settings menu.
				close_sm = True
				while close_sm:
					sm_select = gui.settings_menu() #Runs: SettingsMenu UI
					if sm_select == "1":#Remember last session. (Mysql Server loggin deails)
						change_setting(sm_select)
					elif sm_select == "2":#Confim if wish to leave, before close menu.
						change_setting(sm_select)
					elif sm_select == "3":#Change color for app ui.
						new_color = gui.switch_color_menu()
						if new_color == "":
							pass
						else:
							change_color_setting(new_color)
							close_sm = False
							mm = False
							change_color = True
					elif sm_select == "4":#Opens an advanced options menu.
						change_setting(sm_select)
					elif sm_select == "5":#Close SettingsMenu
						if check_setting_status("2") == "on":
							close_settings = gui.ask_if_close("Settings")
							if close_settings == "y" or close_settings == "Y" or close_settings == "yes":
								close_sm = False
							else:
								close_sm = True
						else:
							close_sm = False
		if mm_select == "3": #Close application.
				if check_setting_status("2") == "off":
					try:
						sql.close_connection()
						mm = False
					except:
						mm = False
				elif check_setting_status("2") == "on":
					close_app = gui.ask_if_close("App")
					if close_app == "y" or close_app == "Y" or close_app == "yes":
						try:
							sql.close_connection()
							mm = False
						except:
							mm = False
					else:
						mm = True
		else:
			pass
else:
	gui.message("Incorrect Password.")
if change_color == True:
	os.system("python main.py")
else:
	pass
