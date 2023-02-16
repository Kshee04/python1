import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened database successfully")

conn.execute("INSERT INTO Employees(ID,JINA,MIAKA,DEPARTMENT) VALUES(20,'Andrew',30,'Science')")
conn.execute("INSERT INTO Employees(ID,JINA,MIAKA,DEPARTMENT) VALUES(21,'Veronica',35,'English')")
conn.execute("INSERT INTO Employees(ID,JINA,MIAKA,DEPARTMENT) VALUES(22,'Pius',40,'Mathematics')")
conn.execute("INSERT INTO Employees(ID,JINA,MIAKA,DEPARTMENT) VALUES(23,'Rose',45,'Technicals')")
conn.execute("INSERT INTO Employees(ID,JINA,MIAKA,DEPARTMENT) VALUES(24,'Ngila',50,'Languages')")
conn.execute("INSERT INTO Employees(ID,JINA,MIAKA,DEPARTMENT) VALUES(25,'Ruth',55,'Humanities')")

conn.commit()
print("records successfully added")
conn.close()