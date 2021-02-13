import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres",
                        password="zxczxc", host="192.168.6.15", port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("SELECT * from COMPANY;")
rows = cur.fetchall()
for row in rows:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
