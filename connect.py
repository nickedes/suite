import psycopg2
import MySQLdb

# Try to connect

try:
    conn = psycopg2.connect("dbname='test' user='nickedes' password=''")
except:
    print("Can't connect to the database.")

try:
    db = MySQLdb.connect(host="localhost",  user="nickedes", passwd="",
                         db="test")
except:
    print("Can't connect to the database.")
