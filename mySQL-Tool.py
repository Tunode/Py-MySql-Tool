import mysql.connector

class mysql_tool:

	def gen_db(self,host_ip, db_user, db_passwd, dbname): #Create Database with name u wish :)
		#host_ip=input("Host ip: ")
		#db_user=input("DB Username: ")
		#db_passwd=input("DB Password: ")
		#dbname=input("DB_Name?: ")
		DB = mysql.connector.connect(
			host = host_ip,
			user = db_user,
			passwd = db_passwd
			)
		DBCursor = DB.cursor()
		DBCursor.execute("CREATE DATABASE "+ dbname)

	def gen_table(self, host_ip, db_user, db_passwd, dbname,tablename,columnname): #Create Table with name u wish in DB you want (only 1 column) (:
		#host_ip=input("Host ip: ")
		#db_user=input("DB Username: ")
		#db_passwd=input("DB Password: ")
		#dbname=input("DB_Name?: ")
		DB = mysql.connector.connect(
			host = host_ip,
			user = db_user,
			passwd = db_passwd,
			database = dbname
			)
		DBCursor = DB.cursor()
		DBCursor.execute("CREATE TABLE "+ tablename +"(dataID int PRIMARY KEY AUTO_INCREMENT)")

	def add_column(self):
		pass

DBTool = mysql_tool()

#DBTool.gen_db(localhost)
#DBTool.gen_table("localhost","root","root","newdb","newtable", "columnname")