#!/usr/bin/python
import psycopg2
from configparser import ConfigParser
import tkinter as tk
from tkinter import simpledialog

def make_connections():
	a=psycopg2.connect(
		host="ec2-54-147-93-73.compute-1.amazonaws.com",
		database="d5og6160bdalf5",
		user="oftjpgldqauges",
		password="9c0c8c7946daf4372e1188d21cff456e0c2e5ab3d06e934edb6e0fc54777c6f8")
	return a

def query(ident, codename=None):
	ident_string=str(ident)
	con = None
	try:
		print("open")
		con = make_connections()
		cur = con.cursor() #enables running sql
		sql_execute = 'select * from player where id='+ident_string
		cur.execute(sql_execute)
		player_ids = cur.fetchall()
		if (len(player_ids) != 0):
			codename = player_ids[0][3]
		elif (codename != None):
			cur.execute('insert into player(id,codename) values(%s,%s)',(ident,codename))
			cur.execute('commit')
		cur.close()
			
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()
			print('close')
	
	return codename
	

def connectTest():
	con = None
	try:
		# connect to the PostgreSQL server
		print('open')
		con = make_connections()
		
		# create a cursor
		cur = con.cursor()
		
		#display player table
		cur.execute('select * from player')
		display_table = cur.fetchall()
		print(display_table)
		# close the communication with the PostgreSQL
		cur.close()
		
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()
			print('close')


if __name__ == '__main__':
	#testing
	connectTest()
	
