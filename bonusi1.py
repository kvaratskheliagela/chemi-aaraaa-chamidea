import sqlite3
conn=sqlite3.connect("customers.sqlite")
cursor=conn.cursor()
# select_result=cursor.execute("SELECT * FROM users")
# for row in select_result:
#     print (row)
# age=25
# select_result = cursor.execute("SELECT * FROM users WHERE  age > ?", (age,))
# for row in select_result:
#     print (row)
# select_result = cursor.execute("SELECT * FROM users WHERE  age > 25")
# for row in select_result:
#         print (row)
# select_result = cursor.execute("SELECT * FROM users WHERE  age between 10 and 25")
# for row in select_result:
#          print (row)
# sql_query = "SELECT firstname, lastname FROM table_name WHERE age <> 20"
# cursor.execute(sql_query)
# result = cursor.fetchall()
#
# for row in result:
#     print(row[0], row[1])
# cursor.execute('SELECT COUNT(*) FROM table_name')
# result = cursor.fetchone()
# print('Number of records:', result[0])
# cursor.execute('SELECT * FROM table_name ORDER BY age')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# cursor.execute(f"SELECT DISTINCT {firstname} FROM {customers.sqlite} ORDER BY {users} ASC")
# unique_firstnames = [row[0] for row in cursor.fetchall()]
# cursor.execute("UPDATE mytable SET username = ?, column2 = ? WHERE age = ?", ('new_username', 'new_value', 20))
#conn.commit()
#conn.close()