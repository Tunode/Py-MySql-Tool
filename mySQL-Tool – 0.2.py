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

	def gen_db(self): #Create Database -> Done
		self.db_connector_new()
		DBCursor = self.DB.cursor()
		DBCursor.execute("CREATE DATABASE "+ self.db_info["dbname"])
		self.close_connection()

	def gen_table(self, tablename): #Create Table with DataID column -> Done
		self.db_connector()
		DBCursor = self.DB.cursor()
		DBCursor.execute("CREATE TABLE IF NOT EXISTS "+ tablename +"(dataID int PRIMARY KEY AUTO_INCREMENT)")
		self.close_connection()

	def add_column(self): #Add Column in selected exsisting Table.
		self.db_connector()
		DBCursor = self.DB.cursor()
		table_name = "users "
		column_name = "username "
		column_type = "VARCHAR(255) "
		DBCursor.execute("CREATE TABLE IF NOT EXISTS "+ table_name +(column_name + column_type))
		#DBCursor.execute("CREATE TABLE IF NOT EXISTS "+ tablename +(column_name + column_type))
		self.close_connection()

DBTool = mysql_tool()

DBTool.ask_db_info()
#DBTool.gen_db()
#DBTool.gen_table("user_data")
DBTool.add_column()