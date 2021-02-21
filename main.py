#Imports:
from mysqltool1 import mysql_tool
from  mysqltool1_gui import  gui

#Variables--

gui = gui()
sql = mysql_tool()
mm=True

#Code--

while mm:
	mm_select = gui.main_menu()
	if mm_select == "1": #Connect to existing DB.
		sql.db_connector(gui.ask_mysql_server_and_db_name())
		db_m = True
		while db_m == True:
			dbm_select = gui.db_menu()
			if dbm_select == "1": #Alter DB
				alt_db = True
				while alt_db == True:
					adb_select = gui.alter_db()
					if adb_select == "1": #Add table.
						sql.gen_table(gui.add_table())
					if adb_select == "2": #Add column.
						sql.add_column(gui.add_column())
					if adb_select == "3": #Remove table.
						gui.remove_table()
					if adb_select == "4": #Remove column.
						gui.remove_column()
					if adb_select == "5": #Close alter db.
						alt_db = False
			if dbm_select == "2": #DB list.
				gui.db_list(sql.show_databases())
			if dbm_select == "3": #Remove DB.
				gui.remove_db()
			if dbm_select == "4": #Create new DB_Menu.
				gui.new_db_name()
			if dbm_select == "5": #Close DB_Menu.
				db_m = False
	if mm_select == "2": #Create new DB.
		sql.db_connector_new(gui.ask_mysql_server())
		sql.gen_db(gui.new_db_name())
	if mm_select == "3": #DB List.
		gui.db_list(sql.show_databases())
	if mm_select == "4": #Remove DB.
		gui.remove_db()
	if mm_select == "5": #Close application.
		sql.close_connection()
		mm = False
	else:
		pass
