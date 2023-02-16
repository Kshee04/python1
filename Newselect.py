import sqlite3
conn=sqlite3.connect('emobilis.db')
data=conn.execute("select * from Employees")
for row in data:
    print("ID=",row[0])
    print("JINA=",row[1])
    print("MIAKA=",row[2])
    print("DEPARTMENT=",row[3],"\n")
conn.close()
