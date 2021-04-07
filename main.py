#Imports:
from mysqltool1 import mysql_tool
from  mysqltool1_gui import  gui
import mysql.connector
from mysql.connector import errorcode
import json
import os

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

ui_color = check_setting_status("3")
gui = gui("0.9.5", ui_color)
sql = mysql_tool()

#----
change_color = False
mm=True
settings = {"1": "off", "2": "off", "3": "2", "4": "off"}
logging_details = {"sql_ip": "localhost", "sql_username": "root", "sql_password": "root", "sql_database": "db"}

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
