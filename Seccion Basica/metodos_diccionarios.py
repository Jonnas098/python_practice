#Diccionario == Objeto

diccionario = {
    'nombre' : "John",
    'apellido' : "Navarro",
    'edad' : 24
}

#Devuelve las keys del diccionario, los devuelve en formato de lista
show_keys = diccionario.keys()
print(show_keys)

#Con "get" podemos traer el valor correspondiente a la key que le pasemos
get_value = diccionario.get('nombre')
print(get_value)


#Eliminar todos los elementos de un diccionario
# diccionario.clear()
# print(diccionario)

#Eliminar algun elemento de un diccionario por su key

diccionario.pop('edad')
#print(diccionario)

#Iterar un diccionario con "items", devuelve cada elemento clave valor dentro de una lista
iterate_dictionary = diccionario.items()
print(iterate_dictionary)