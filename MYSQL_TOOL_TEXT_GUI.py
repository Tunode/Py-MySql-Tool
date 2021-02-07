#MYSQL_TOOL_TEXT_GUI.py
import mysqltool1
DBtool = mysqltool1.mysql_tool()

class textgui:
	def ask_if_local(self):
		print("MSQL Server is local?")
		local=input("y or n?: ")
		if local == "y" or "Y":
			mysql_ip = "localhost"
		else:
			mysql_ip = input("MSQL Server IP?: ")
		return mysql_i#Ask from user if MYSQL server is hosted localy or in spesific IP.