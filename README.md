# Py-MySql-Tool
This makes you daily python mysql tasks x 10 times easier.
IN Progress!
--------------------------------------------------------------
Text in is just started -> 5% | Filename: MYSQL_TOOL_GUI.py

more info coming.

-------------------------------------------------------------
The basemodule is done about -> 85% |  filename: mysqltool1.py
  so far this module can do following MYSQL tasks:
  
    - Ask MYSQL info (through cmd with input)
       - ip (localhost)
       - username
       - password
       - Databasename (and use it if it exsists all ready)
    - A Connet to MYSQL server with out databasename. function: db_connector_new(),  info: (new =  as a new connection without database yet)
    - Connect to MYSQL server with database name. function: db_connector()
    - Close MYSQL Connection. function: close_connection()
    - Generate database with name you want. | Function: gen_db("database_name")
    - Generate table in named database. Function: gen_table("table_name")
