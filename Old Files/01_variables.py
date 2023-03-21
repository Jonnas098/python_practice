#Voy a trabajar variables

mi_variable = 'Mi variable en python'
#print(mi_variable)

my_int_variable = 3
#print(my_int_variable)

my_bool_variable = False
#print(my_bool_variable)

convertir_dato = str(my_int_variable)
#print(convertir_dato)
#print(type(convertir_dato))
#print(len(convertir_dato))
#print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

#Variables en una sola linea

name, surname, alias, age = 'John', 'Navarro', 'Jonnas', 24
#print(name, surname, 'Me dicen:', alias, 'Y mi edad es:', age)

#nombre = input('Cual es tu nombre: ')
#edad = input('Cual es tu edad: ')

#print('Mi nombre es', nombre, 'y mi edad es:', age)

#Forzamos el tipo?

address: str = 'Mi direccion'
address = 32
print(type(address))