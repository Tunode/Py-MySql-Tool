#MYSQL_TOOL_TEXT_GUI.py
from mysqltool1 import mysql_tool
db_tool = mysql_tool()
#--------------------------------
class textgui: #OOP of text gui:
	def ask_if_local(self): #Ask from user if MYSQL server is hosted localy or in spesific IP.
		print("-"*20)
		print("- MSQL Server is local? -")
		local=input("-| y or n?: ")
		if local == "y" or "Y":
			mysql_ip = "localhost"
		else:
			mysql_ip = input("MSQL Server IP?: ")
		return mysql_ip

	def ask_mysql_info(self):
		pass

# The Code it self:
mstg = textgui()
#------------------
mstg.ask_if_local()
