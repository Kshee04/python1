import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db successfully")

conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(1,'Grace',18,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(2,'Emily',27,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(3,'Ken',30,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(4,'Winnie',23,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(5,'Edward',16,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(6,'Mark',14,'eMobilis')")


conn.commit()
print("records added sucesfully")
conn.close()