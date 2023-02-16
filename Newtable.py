import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened database successfully")
conn.execute("CREATE TABLE Employees"
             "(ID INT PRIMARY KEY NOT NULL,"
             "JINA TEXT NOT NULL,"
             "MIAKA INT NOT NULL,"
             "DEPARTMENT TEXT NOT NULL)")

print("Employees created succesfully")
conn.close()