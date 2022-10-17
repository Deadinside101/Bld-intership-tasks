#! python3
import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="school",
    user="sparrow",
    password="password"
    )


#cursor
cur = con.cursor()
#execute cursor
cur.execute("insert into student (id, first_name, last_name, age) values (%s, %s, %s,%s) ", (8, 'Khalid', 'Ali',18))
cur.execute("select id, first_name from student")


rows = cur.fetchall()

for i in rows:
    print(f"id {i[0]} name {i[1]}")
 
#NOTE you have to commit the transaction and refresh database to see the changes in the table
#TODO - con.commit()
cur.close()
#close
con.close()
