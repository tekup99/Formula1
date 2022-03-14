import psycopg2

def connection():
    return psycopg2.connect(
   database="formula1", user='postgres', password='123', host='127.0.0.1', port= '5432'
)
#Establishing the connection
conn = connection()
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS RACE")

#Creating table as per requirement
sql ='''CREATE TABLE CIRCUIT1(
   MAP_NO INT NOT NULL,
   LAP_NO INT NOT NULL,
   SESSION_NO INT NOT NULL,
   DRIVER_NO INT NOT NULL,
   LAP_TIME TEXT NOT NULL,
   PIT_LAP BOOLEAN NOT NULL,
   PRIMARY KEY (MAP_NO, LAP_NO, SESSION_NO, DRIVER_NO)
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()