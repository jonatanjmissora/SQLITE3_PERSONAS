import sqlite3

# crear una tabla
def crear_tabla():
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()

	c.execute("""CREATE TABLE listado (
				nombre text,
				apellido text,
				edad text)
				""")
	conn.commit()
	conn.close()

def insert_one(nombre, apellido, edad):
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("INSERT INTO listado VALUES (?,?,?)", (nombre, apellido, edad))
	conn.commit()
	conn.close()

def insert_one_in(rowid, row):
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("INSERT INTO listado VALUES (?,?,?) ", (row))
	conn.commit()
	conn.close()

def insert_algunos(lista):
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.executemany("INSERT INTO listado VALUES (?,?,?)", lista)
	conn.commit()
	conn.close()

def show_all():
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("SELECT rowid, * FROM listado")
	[print(row) for row in c.fetchall()]
	conn.commit()
	conn.close()

def borrar_id(id):
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("DELETE FROM listado WHERE rowid=?", (id, ))
	conn.commit()
	conn.close()

def borrar_apellido(apell):
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("DELETE FROM listado WHERE apellido=?", (apell, ))
	conn.commit()
	conn.close()

def borrar_datos():
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("DELETE FROM listado")
	conn.commit()
	conn.close()

def borrar_tabla():
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("DROP TABLE listado")
	conn.commit()
	conn.close()

def buscar_apellido(apell):
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("SELECT rowid, * FROM listado WHERE apellido=?", (apell, ))
	[print(row) for row in c.fetchall()]
	conn.commit()
	conn.close()

def cambiar_nombre(viejo, nuevo):
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("UPDATE listado SET nombre=? WHERE nombre=?", (nuevo, viejo, ))
	[print(row) for row in c.fetchall()]
	conn.commit()
	conn.close()

def update_renglon(data):
	conn = sqlite3.connect("personas.db")
	c = conn.cursor()
	c.execute("UPDATE listado SET nombre=?, apellido=?, edad=? WHERE rowid=?", data)
	conn.commit()
	conn.close()

