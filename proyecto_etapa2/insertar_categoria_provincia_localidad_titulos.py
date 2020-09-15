import sqlite3

con = sqlite3.connect('db.sqlite3')

cursor = con.cursor()

reg1=("Reparar Hogar","Personas que se dediquen a la reparación o contruccion dentro del Hogar")
reg2=("Arreglar Jardin", "Personas que se dediquen al mantenimiento de patio, jardines, piletas, etc.")
reg3=("Educacion y Entrenamiento", "Personas dedicada a la educacion o entrenamiento de niños y adultos, de manera fisica o virtual")
reg4=("Profesional Medico y Estetico", "Profesionales dedicado al cuidado de la saludo y la estetica corporal")
reg5=("Otro", "Todos las personas que no se sienta representadas por algunas de las anterior categorias")
query="INSERT INTO bolsa_categoria(nombre_cat,descripcion) values(?,?)"
cursor.execute(query,reg1)
cursor.execute(query,reg2)
cursor.execute(query,reg3)
cursor.execute(query,reg4)
cursor.execute(query,reg5)
con.commit()
cursor.close()
con.close()