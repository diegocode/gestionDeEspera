#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  

import sqlite3
conn = sqlite3.connect('cEspera.db')

conn.execute('''CREATE TABLE if not exists espera
	 (id       INT PRIMARY KEY  NOT NULL,
	  nombre   TEXT                NOT NULL,
	  dni      INT                 NOT NULL,
	  tipo	   TEXT				   NOT NULL,
	  estado   TEXT				
	 );''')

def ingresar():
	ntu = input("id > ")
	nombre = input("nombre > ")
	dni = input("dni > ")
	tipo = input("tipo > ")	
	
	qry = f"INSERT INTO espera (id, nombre, dni, tipo, estado) VALUES ({ntu}, '{nombre}', {dni}, '{tipo}', 'e')"
	
	print(qry) 
	
	conn.execute(qry)

	conn.commit()
	
def listar():
	cc = conn.execute("SELECT id, nombre, dni, tipo FROM espera where estado = 'e'")
	
	for fila in cc:
		print("%3d\t%s\t\t\t%2d\t%s" %  (fila[0], fila[1], fila[2], fila[3]))

	cc.close()
	
def borrar():
	pass	

def menu():
	while True:
		opc = input("> ")
		if opc == "i":
			ingresar()
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
