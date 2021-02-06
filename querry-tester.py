import mysql.connector

table_name = "users "
column_name = "username "
column_type = "VARCHAR(255) "

query = "CREATE TABLE IF NOT EXISTS" + table_name

print(query)

table_name = "users "
column_name = "username "
column_type = "VARCHAR(255) "
query2 = ("CREATE TABLE IF NOT EXISTS "+ table_name +(column_name + column_type))

print(query2)



("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
