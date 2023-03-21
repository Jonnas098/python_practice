lista = list(['Hola', 'John', 34])
print(lista)

prueba = len(lista)

#Agregar un elemento a una lista con "append", lo agrega al final de la lista 
lista.append('nuevo')

#Agregar un elemento a una lista en un indice especifico
lista.insert(2, 'Otra Prueba')

#Agregar varios elementos a una lista con "extend", de igual manera los agrega al final y los datos deben de ir dentro de corchetes
lista.extend(['Dato1', 22, 'Dato3'])

#Eliminar elementos con "pop", por su indice

lista.pop(2) #-1 para eliminar el ultimo elemento de la lista

#Eliminar elementos con "remove", se busca con su valor

lista.remove('Dato1')

#Eliminar todos los elementos de una lista
#lista.clear()

#Ordena los elementos de una lista de manera acendente, no funciona si hay strings en la lista

#lista.sort() #Si le agregamos un "reverse = True" lo ordena de manera invertida 

#El metodo reverse devuelve los elementos de la cadena el ultimo al primero

#lista.reverse()

#Buscar el indice de un elemento

search_index = lista.index("John")
print(search_index)

print(lista)