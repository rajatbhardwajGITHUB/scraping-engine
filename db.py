import mysql.connector
from mysql.connector import Error

def convert_file(file):
	with open(file, 'rb') as File:
		bin_data = File.read()
	return bin_data

def insert(file):
	try:
		conn = mysql.connector.connect(host = 'localhost', database = 'flaskapp', user = 'rajat', password = 'pass')
		cursor = conn.cursor()
		
		sql_query = """ INSERT INTO geeks(file) VALUES(%s) """
		blob_file = convert_file(file) 
		
		
		cursor.execute(sql_query, blob_file,)
		conn.commit()
	except mysql.connector.Error as error:
		print('failed')
	
	finally:	
		cursor.close()
		conn.close()
		print("db is closed")
insert('/root/Desktop/docs/SE2/geeks/crawled.txt')
		
