from YPHS.mydatabase import database

table_name = "HW107"

db = database("Homework.db")
db.create_table(table_name)