import psycopg2
#CONNECT
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=chris password=root")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

#CREATE DATABASE
try:
    cur.execute("create database myfirstdb")
except psycopg2.Error as e:
    print(e)

try:
    conn.close()
except psycopg2.Error as e:
    print(e)

#CONNECT
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=myfirstdb user=chris password=root")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

#CREATE TABLE
try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar, age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print ("Error: Issue creating table")
    print(e)

#INSERT FOLLOWING ROWS
try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
        VALUES (%s,%s,%s,%s,%s,%s)", \
        (1, "stevens", 23, "Male", "Python", 85 ))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print (e)
try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
        VALUES (%s,%s,%s,%s,%s,%s)", \
        (2, "chris", 22, "Female", "Python", 86 ))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print (e)

#QUERY
try:
    cur.execute("SELECT * FROM students;")
except psycopg2.Error as e:
    print("Error: select *")
    print (e)

#DISPLAY ROWS
row = cur.fetchone()
while row:
    print (row)
    row = cur.fetchone()

cur.close()
conn.close()
