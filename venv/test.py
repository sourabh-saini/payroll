import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='test'
)

mycursor = mydb.cursor()

sql = "insert into test_tbl values(%s,%s)"
val = [('null')]
mycursor.executemany(sql, val)

mydb.commit()
#logging.warn("%d", affected_count)
#logging.info("inserted values %d, %s", id, filename)
print(mycursor.rowcount)