import mysql.connector

class mysql_tool:

	def ask_db_info(self):#Asks loggin details form user with: INPUT(CMD) -> Done
		host_ip = input("Host ip: ")
		db_user = input("DB Username: ")
		db_passwd = input("DB Password: ")
		db_name = input("DB_Name: ")
		self.db_info = {
			"host_ip": host_ip,
			"db_user": db_user,
			"db_passwd": db_passwd,
			"dbname": db_name
		}

	def db_connector_new(self):#Connects mysql without DB name: (this is for gen_db functionality) -> done
		self.DB = mysql.connector.connect(
			host = self.db_info["host_ip"],
			user = self.db_info["db_user"],
			passwd = self.db_info["db_passwd"]
			)

	def db_connector(self):#Connetcs with excisting DB -> Done
		self.DB = mysql.connector.connect(
			host = self.db_info["host_ip"],
			user = self.db_info["db_user"],
			passwd = self.db_info["db_passwd"],
			database = self.db_info["dbname"]
			)

	def close_connection(self):#Simply closes DB Connection -> Done
		self.DB.close()

	def gen_db(self, dbname): #Create Database -> Done
		self.db_connector_new()
		DBCursor = self.DB.cursor()
		DBCursor.execute("CREATE DATABASE "+dbname)
		self.close_connection()

	def gen_table(self, tablename): #Create Table with DataID column -> Done
		self.db_connector()
		DBCursor = self.DB.cursor()
		DBCursor.execute("CREATE TABLE IF NOT EXISTS "+ tablename +"(dataID int PRIMARY KEY AUTO_INCREMENT)")
		self.close_connection()

	def add_column(self, table_name, column_name): #Add Column in selected exsisting Table. -> Done
		self.db_connector()
		DBCursor = self.DB.cursor()
		#DBCursor.execute("CREATE TABLE users (name varchar(255)))")
		DBCursor.execute("ALTER TABLE " + " " + table_name + " ADD " "(" + column_name + " VARCHAR(255))")
		self.close_connection()

	def show_databases(self): #Prints list of databases in MYSQL server. -> Working.
		self.db_connector()
		DBCursor = self.DB.cursor()
		DBCursor.execute("SHOW DATABASES")
		l = DBCursor.fetchall()
		l = [ i[0] for i in l ]
		print(l)
		self.close_connection()

	def delete_db(self, database_name): #Simply removes DB from MYSQL server -> Done
		self.db_connector()
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
		self.close_connection()

DBTool = mysql_tool()
