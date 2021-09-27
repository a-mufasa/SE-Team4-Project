#!/usr/bin/python
import psycopg2
from configparser import ConfigParser
import tkinter as tk
from tkinter import simpledialog

#conn = psycopg2.connect(
#    host="ec2-54-147-93-73.compute-1.amazonaws.com",
#    database="d5og6160bdalf5",
#    user="oftjpgldqauges",
#    password="9c0c8c7946daf4372e1188d21cff456e0c2e5ab3d06e934edb6e0fc54777c6f8")
    
def query(ident):
	ident_string=str(ident)
	codename=''
	con = None
	try:
		print("open")
		conn = psycopg2.connect(
			host="ec2-54-147-93-73.compute-1.amazonaws.com",
			database="d5og6160bdalf5",
			user="oftjpgldqauges",
			password="9c0c8c7946daf4372e1188d21cff456e0c2e5ab3d06e934edb6e0fc54777c6f8")
		cur = con.cursor() #enables running sql
		sql_execute = 'select * from player where id='+ident_string
		cur.execute(sql_execute)
		player_ids = cur.fetchall()
		if (len(player_ids) == 0):
			codename = get_new_codename() #get code name and upload to database
			cur.execute("insert into player (id, codename) values (%s,%s)",(ident,codename))
			
		else:
			codename = player_ids[0][3]
			
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			cur.execute('commit')
			con.close()
			print('close')
	
	return codename
	
def get_new_codename():
	root = tk.Tk()
	root.withdraw()
	input_codename=None
	while input_codename == None or input_codename == '':
		input_codename=simpledialog.askstring(title="Please enter a codename",prompt="hi")
	return str(input_codename)
    
def connectTest():
    conn = None
    try:

        # connect to the PostgreSQL server
        print('open')
        conn = psycopg2.connect(
			host="ec2-54-147-93-73.compute-1.amazonaws.com",
			database="d5og6160bdalf5",
			user="oftjpgldqauges",
			password="9c0c8c7946daf4372e1188d21cff456e0c2e5ab3d06e934edb6e0fc54777c6f8")
		
        # create a cursor
        cur = conn.cursor()
        
        #display player table
        cur.execute('select * from player')
        display_table = cur.fetchall()
        print(display_table)
		# close the communication with the PostgreSQL
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('close')


if __name__ == '__main__':
	#testing
	connectTest()