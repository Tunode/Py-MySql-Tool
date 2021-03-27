#Imports:
from mysqltool1 import mysql_tool
from  mysqltool1_gui import  gui
import mysql.connector
from mysql.connector import errorcode
import json

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
		logging_details = load_loggin_details()
		logging_details.update({"sql_database": f"{M_DB_Menu_Selection}"})
		save_loggin_details(logging_details)
		return logging_details
	else:
		pass

gui = gui("0.9.2")
sql = mysql_tool()

#----

mm=True
settings = {"1": "off", "2": "off", "3": "off", "4": "off"}
logging_details ={"sql_ip": "localhost", "sql_username": "root", "sql_password": "root", "sql_database": "db"}

#Code--
try: #Create loggin logging_details.jason and add default loggin details.(if not created allready.)
	logging_details_file=open("logging_details.json", "x")
	j = json.dumps(logging_details)
	with open("logging_details.json", "w") as f:
		f.write(j)
		f.close()
except:
	pass

try: #Create settings.jason and add default settings.(if not created allready.)
	settings_file=open("settings.json", "x")
	j = json.dumps(settings)
	with open("settings.json", "w") as f:
		f.write(j)
		f.close()
except:
	pass

password = gui.ask_loggin_details()
if password == "tuno":
	while mm == True:
		mm_select = gui.main_menu()
		if mm_select == "1": #Connect to MySql Server.
				try:
					if check_setting_status("1") == "off":
						log_details = gui.ask_mysql_server()
						save_loggin_details(log_details)
						sql.db_connector(log_details)
						db_m = True
					elif check_setting_status("1") == "on":
						sql.db_connector(load_loggin_details())
						db_m = True
				except mysql.connector.Error as err:
					gui.message(f"ERROR: {err}")
					db_m = False
				while db_m == True:
					dbm_select = gui.db_menu()
					if dbm_select == "1": #Open menu to Select database and then opens menu to altter selected database.						
						sql.db_connector(multiple_DB_slection(sql.show_databases()))
						alt_db = True
						while alt_db == True:
							adb_select = gui.alter_db()
							if adb_select == "1": #Add table.
								try:
									sql.gen_table(gui.add_table())
								except:
									gui.message("ERROR: Incorrect input.")
							if adb_select == "2": #Add column.
								try:
									sql.add_column(gui.add_column())
								except:
									gui.message("ERROR: Incorrect input.")
							if adb_select == "3": #Remove table.
								try:
									sql.delete_table(gui.remove_table())
								except:
									gui.message("ERROR: Incorrect input.")
							if adb_select == "4": #Remove column.
								try:
									sql.delete_column(gui.remove_column())
								except:
									gui.message("ERROR: Incorrect input")
							if adb_select == "5": #Close alter db.
								alt_db = False
					if dbm_select == "2": #Remove DB.
						try:
							sql.delete_db(gui.remove_db(sql.show_databases()))
						except:
							gui.message("ERROR: Incorrect input.")
					if dbm_select == "3": #Create new DB_Menu.
						try:
							sql.gen_db(gui.new_db_name())
						except:
							gui.message("ERROR: Incorrect input.")
					if dbm_select == "4": #Close DB_Menu.
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
						change_setting(sm_select)
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

