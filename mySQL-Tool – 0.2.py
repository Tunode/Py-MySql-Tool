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

	def close_connet(self):
		self.DB.close()

	def gen_db(self): #Create Database -> 50%?
		self.db_connector_new()
		DBCursor = self.DB.cursor()
		DBCursor.execute("CREATE DATABASE "+ self.db_info["dbname"])
		self.close_connet()

	def gen_table(self, tablename): #Create Table with DataID column -> 50%?
		DBCursor = self.DB.cursor()
		DBCursor.execute("CREATE TABLE "+ tablename +"(dataID int PRIMARY KEY AUTO_INCREMENT)")

	def add_column(self): #Add Column in selected exsisting Table.
		pass

DBTool = mysql_tool()

#DBTool.gen_db(localhost)
#DBTool.gen_table("localhost","root","root","newdb","newtable", "columnname")
DBTool.ask_db_info()
DBTool.gen_db()