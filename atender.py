#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  

import sqlite3
conn = sqlite3.connect('cEspera.db')

n = 66

def atender(tipo):	
	qry = f"select id, nombre, dni, tipo from espera where estado = 'e' and tipo = '{tipo}' order by id "
	
	cc = conn.execute(qry)
	
	fila = cc.fetchone()
	
	if fila != None:			
		print("%3d\t%s\t\t\t%2d\t%s" %  (fila[0], fila[1], fila[2], fila[3]))
	
		qry = f"update espera set estado = 'a' where id = {fila[0]}"
	
		conn.execute(qry)
	
		conn.commit() 
	
	
def listar():
	cc = conn.execute("SELECT id, nombre, dni, tipo, estado FROM espera order by estado DESC, id")
	
	for fila in cc:
		print("%3d\t%s\t\t\t%2d\t%s (%s)" %  (fila[0], fila[1], fila[2], fila[3], fila[4]))

	
def borrar():
	pass	

def menu():
	while True:
		opc = input("> ")
		if opc == "a":
			atender("a")
		elif opc == "b":
			borrar()			
		elif opc == "l":
			listar()
		elif opc == "x":
			break


def main():
	menu()
	return 0

if __name__ == '__main__':    
    main()
    conn.close()
