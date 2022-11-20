import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    #password="root",
    database="PES1UG20CS108_PROJECT"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS crime(crime_id int NOT NULL, crime_type varchar(100),crime_place varchar(100),crime_date DATE NOT NULL,PRIMARY KEY(crime_id));')


def add_crime_data(crime_id, crime_type,crime_place,crime_date):
    c.execute('INSERT INTO crime (crime_id,crime_type,crime_place,crime_date) VALUES (%s,%s,%s,%s);',
              (crime_id, crime_type,crime_place,crime_date))
    mydb.commit()

def add_criminal_data(crime_id, criminal_id,criminal_name,past_crimes,jail_name):
    c.execute('INSERT INTO criminal (crime_id, criminal_id,criminal_name,past_crimes,jail_name) VALUES (%s,%s,%s,%s,%s);',
              (crime_id, criminal_id,criminal_name,past_crimes,jail_name))
    mydb.commit()

def add_fir_data(crime_id,fir_id,fir_statement,fir_writer,date_of_fir):
    c.execute('INSERT INTO fir(crime_id,fir_id,fir_statement,fir_writer,date_of_fir) VALUES (%s,%s,%s,%s,%s);',
                (crime_id,fir_id,fir_statement,fir_writer,date_of_fir))
    mydb.commit()


