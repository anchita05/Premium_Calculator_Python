# Creating the mega sql table
import pymysql as pm
import csv
conn = pm.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql"
)
cursor = conn.cursor()
cursor.execute("use project2022")

cursor.execute("""create table premium50(
Days int(4),
3m_50y varchar(6),
51_60 varchar(6),
61_70 varchar(6));
""")

def insert_rec(rec):
    sql = "insert into premium50 values(%s,%s,%s,%s)"
    values = rec
    cursor.execute(sql,values)
    conn.commit()

f = open("rates1.csv","r")
readobj = csv.reader(f)
for i in readobj:
    if readobj.line_num == 1:
        continue
    if i[0] == "":
        break
    insert_rec(i)

f.close()
conn.close()