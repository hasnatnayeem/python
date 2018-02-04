import pymysql

host = "localhost"
port = 3306
user = "root"
password = "1"
db_name = "nayeem"
table_name = "Abc"

conn = pymysql.connect(host = host, port = port, user = user, passwd = password, db = db_name)
cur = conn.cursor()

sql = "SELECT * FROM " + table_name

cur.execute(sql)

for r in cur:
    print(r)

cur.close()
conn.close()
