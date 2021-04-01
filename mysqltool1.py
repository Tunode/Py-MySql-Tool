import mysql.connector
import json

class mysql_tool:

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
		self.db_connector()
		DBCursor = self.DB.cursor()
		DBCursor.execute("DROP TABLE "+table_name)
		self.close_connection()

	def delete_column(self, table_name, column_name): #Delete column from Table you name in DB of your wish. -> Done
		self.db_connector()
		DBCursor = self.DB.cursor()
		DBCursor.execute("ALTER TABLE "+table_name+ " DROP COLUMN "+column_name)
		self.close_connection()#Simple MYSQL module to make daily MYSQL Tasks easier.

#Testing area:
DBTool = mysql_tool()
#DBTool.gen_db()