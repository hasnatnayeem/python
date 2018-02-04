import pymysql

host = "localhost"
port = 3306
user = "root"
password = "1"
db_name = "nayeem"
table_name = "Abc"

# Creating connection and cursor object
conn = pymysql.connect(host = host, port = port, user = user, passwd = password, db = db_name)
cur = conn.cursor()

sql = "SELECT * FROM " + table_name

# Executing query using cursor object
cur.execute(sql)

# Iterating over the results
for row in cur:
    print(row)

# Closing cursor and connection
cur.close()
conn.close()
