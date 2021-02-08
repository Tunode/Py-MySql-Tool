#MYSQL_TOOL_TEXT_GUI.py

#-Import's-----------------------
from datetime import datetime
from mysqltool1 import mysql_tool
db_tool = mysql_tool()
#--------------------------------

class textgui: #OOP of text gui:

	def now_time_date(self):
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M")
		return dt_string 	

	def ask_if_local(self): #Ask from user if MYSQL server is hosted localy or in spesific IP.
		while True:
			print("-"*20)
			print("- MSQL Server is local? -")
			local = input("-| y or n?: ")
			if local == "y" or local == "yes":
				mysql_ip = "localhost"
				return mysql_ip
				break
			if local == "n" or local == "no":
				print("-"*20)
				mysql_ip = input("MSQL Server IP?: ")
				print("-"*20)
				return mysql_ip
				break
			else:
				print("-"*20)
				print("- Wrong input! -")
				print("- Please try again. -")
		
	def ask_if_new(self): #Ask's from user if contecting to exsisting database or dont have one yet. 
			while True: #(Dev comment: returns username,passwd (+database_name) in dictionary)
				print("-"*20)
				print("- Creating new db or connecting to existing one? -")
				new_or_old=input("-| new/old?: ")
				if new_or_old == "new" or new_or_old == "n":
					print("-"*20)
					print("- Please input: MSQL Server loggin details? -")
					mysql_username=input(" - Username: ")
					mysql_password=input(" - Password: ")
					#-Dictionary--
					mysql_loggin_data ={
						"sql_username": mysql_username,
						"sql_password": mysql_password,
						"sql_time_now": self.now_time_date()
					}
					return mysql_loggin_data
					break

				if new_or_old == "old" or new_or_old == "o":
					print("-"*20)
					print("- Please input: MSQL Server loggin details? -")
					mysql_username=input(" - Username: ")
					mysql_password=input(" - Password: ")
					print("-"*20)
					print("- Name of database you wish to connect: ")
					mysql_database_name=input(" - Database name: ")
					#-Dictionary--
					mysql_loggin_data ={
						"sql_username": mysql_username,
						"sql_password": mysql_password,
						"sql_database": mysql_database_name,
						"sql_time_now": self.now_time_date()
					}
					return mysql_loggin_data
					break
				else:
					print("-"*20)
					print("- Wrong input! -")
					print("- Please try again. -") 

 #- Note's to dev's ---
 # To acsess dictionary: 
 # example:
 # x=  mysql_loggin_data["sql_time_now"]
 # print(x)
 #---

#- The Code it self: ---
mstg = textgui()
#---
#print(mstg.ask_if_local())
mstg.ask_if_new()
