import sqlite3

con = sqlite3.connect('db.sqlite3')

cursor = con.cursor()

#carga categorias
reg1=("Reparar Hogar","Personas que se dediquen a la reparación o contruccion dentro del Hogar")
reg2=("Arreglar Jardin", "Personas que se dediquen al mantenimiento de patio, jardines, piletas, etc.")
reg3=("Educacion y Entrenamiento", "Personas dedicada a la educacion o entrenamiento de niños y adultos, de manera fisica o virtual")
reg4=("Profesional Medico y Estetico", "Profesionales dedicado al cuidado de la saludo y la estetica corporal")
reg5=("Otro", "Todos las personas que no se sienta representadas por algunas de las anterior categorias")

query="INSERT INTO cuenta_categoria(nombre_cat,descripcion) values(?,?)"

cursor.execute(query,reg1)
cursor.execute(query,reg2)
cursor.execute(query,reg3)
cursor.execute(query,reg4)
cursor.execute(query,reg5)

#carga titulos
reg1=("Albañil",1)
reg2=("Plomero",1)
reg3=("Electricista",1)
reg4=("Tecnico Aire Acondicionado",1)
reg5=("Pintor",1)
reg51=("Cerrajero",1)
reg6=("Jardinero",2)
reg7=("Limpia Pileta",2)
reg8=("Fumigador",2)
reg9=("Maestra/o",3)
reg10=("Profesor/a",3)
reg11=("Personal Training",3)
reg12=("Niñera",3)
reg13=("Tutor",3)
reg14=("Cuidador domiciliario",4)
reg15=("Kinesiologo",4)
reg16=("Medico",4)
reg17=("Masajista",4)
reg18=("Peluqueria",4)
reg19=("Podologo, Pedicura",4)
reg20=("Manicura",4)
reg21=("Tratamiento faciales",4)
reg22=("Gomero",5)


lista=[reg1,reg2,reg3,reg4,reg5,reg51,reg6,reg7,reg8,reg9,reg10,reg11,reg12,reg13,reg14,reg15,reg16,reg17,reg18,reg19,reg20,reg21,reg22]
query="INSERT INTO cuenta_titulo(titulo,categoria_id) values(?,?)"
for argumento in lista:
    cursor.execute(query,argumento)

#carga provincia por ahora solo chaco
reg1=("Chaco",)
query="INSERT INTO cuenta_provincia(provincia) values(?)"
cursor.execute(query,reg1)

#cargar localidades
localidades={"220042":"Isla del Cerrito",
"220119":"Chorotis","220126":"Santa Sylvina","220308":"Coronel Du Graty",
"220112":"Hermoso Campo","220420":"Samuhú","220392":"Basail",
"220406":"Puerto Vilelas","220322":"Villa Ángela","220399":"Fontana",
"220385":"Barranqueras","220098":"General Capdevila","220462":"Cote Lai",
"220254":"Puerto Tirol","220231":"Colonia Popular","220350":"San Bernardo",
"220161":"Makallé","220182":"Juan José Castelli","220189":"Miraflores",
"220238":"Laguna Blanca","220147":"Lapachito","220336":"La Clotilde",
"220091":"Gancedo","220140":"La Escondida","220427":"Villa Berthet",
"220154":"La Verde","220343":"La Tigra","220056":"Las Palmas",
"220105":"General Pinedo","220434":"Capitán Solari","220063":"Puerto Bermejo",
"220357":"Presidencia de la Plaza","220217":"Campo Largo","220113":"Corzuela",
"220070":"Puerto Eva Perón","220224":"Napenay","220266":"La Eduvigis",
"220077":"Presidencia Roque Sáenz Peña","220455":"Las Garcitas","220280":"Pampa Almirón",
"220252":"Ciervo Petiso","220210":"Avia Terai","220273":"Laguna Limpia",
"220259":"Gral. San Martengeneral San Martín","220476":"Machagai",
"220007":"Concepción del Bermejo","220021":"Pampa del Infierno","220294":"Presidencia Roca",
"220287":"Pampa del Indio","220014":"Los Frentones","220301":"Tres Isletas",
"220203":"Villa Río Bermejito","220169":"Misión Nueva Pompeya","220175":"Fuerte Esperanza",
"220168":"El Sauzalito","220364":"Colonia Benitez","220441":"Colonias Elisa",
"220448":"Colonias Unidas","220035":"General Vedia","220413":"Resistencia",
"220315":"Enrique Urien","220469":"Charadai","220371":"Margarita Belén",
"220049":"La Leonesa","220084":"Charata","220329":"Las Breñas",
"220378":"Quitilipi","220028":"Taco Pozo"}

query="INSERT INTO cuenta_localidad(localidad,provincia_id) values(?,?)"

for x in localidades:
    reg=(localidades[x],1)
    cursor.execute(query,reg)

reg=("Es una vidriera de trabajadores donde poden ofercer sus servicios","Permitimos que el cliente y el trabajador se encuentren mediante las ofertas o perfiles de los trabajadores","Un lugar donde encontras a ese tecnico o profesional que necesitas de una manera rapida, sencilla y con recomendaciones de los clientes")

query="INSERT INTO cuenta_que_hacemos(que_es,que_permite,porque_nosotros) values(?,?,?)"

cursor.execute(query,reg)

con.commit()
cursor.close()
con.close()