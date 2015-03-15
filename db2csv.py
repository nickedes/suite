import csv
import psycopg2

conn = psycopg2.connect("dbname='test' user='nickedes' password=''")

cursor = conn.cursor()  # assuming you know how to connect to your oracle db

cursor.execute('select * from table_data')

with open('output_file.csv', 'wb') as fout:
    writer = csv.writer(fout)
    writer.writerow([i[0] for i in cursor.description])  # heading row
    writer.writerows(cursor.fetchall())
    