# Py-MySql-Tool APP
This makes you daily python mysql tasks x 10 times easier.
IN Progress!
--------------------------------------------------------------

MYSQL-Tool-0.8.9

Changes to do:
- Settings = In-progress. 3/4
- Error handling = need's to be reworked. (In-progress.)

-------------------------------------------------------------
  so far this module can do following MYSQL tasks:
  (more comming)

   - Ask MYSQL info (through cmd with input)
       - ip (localhost)
       - username
       - password
       - Databasename (and use it if it exsists all ready)
   - A Connet to MYSQL server with out databasename. function: db_connector_new(),  info: (new =  as a new connection without database yet)
   - Connect to MYSQL server with database name. function: db_connector()
   - Close MYSQL Connection. function: close_connection()
   - Generate database with name you want. | Function: gen_db("database_name")
   - Generate table in named database. Function: gen_table("table_name") + It automaticly add 1 column (called: dataID -> automated number for data added in future)
   - Add column: this allow you add named column -> in named table. Function: add_column("table_name", "column_name")
   - Show databases this prints a list of databases in MYSQL server you are connected. Function: show_databases()
   - Delete database with this function you can drop a named db from MYSQL server (! all data is deleted !). Function: delete_db(database_name)
   - Delete a named table from connected db. Function: delete_table("table_name")
   - Delete a named column from connected db. Function: delete_column("table_name", "column_name")
