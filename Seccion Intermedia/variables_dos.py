#Desempaquetado
#Funciona con tuplas y listas

datos = ('John', 'Navarro', 24)

nombre,apellido,edad = datos

#print(apellido)

#Seccion de tuplas

tupla = tuple(['Dato1', 'Dato2', 'Dato3'])
#Una tupla se puede crear sin parentesis, solo hay que separar los datos con 'coma'
tupla_dos = 'Dato1', 'Dato2'
print(type(tupla_dos))

#Conjuntos

#Los datos creados con set no se pueden modificar
conjunto = set(['Dato1', 'Dato2', ('Dato3', 'Dato4')])
conjunto_dos = frozenset({'dato1', 'dato2'})
conjunto_tres = {conjunto_dos, 'Otro Dato', 24}

print(conjunto_tres)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Aqui verificamos si el conjunto2 es un subconjunto de conjunto1
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
print(resultado)

#Verificando si conjunto1 es un superconjunto de conjunto2
resultado_dos = conjunto1.issuperset(conjunto2)
resultado_dos = conjunto2 >= conjunto2
print(resultado_dos)

#Verificando si hay algun nnumero en comun

resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)