animales = {'perro', 'gato', 'loro', 'cocodrilo'}
numeros = {10, 52, 86, 98}

# Recorriendo la conjunto de animales
for animal in animales:
    print(animal)

# Recorriendo la conjunto de numeros y multiplicando su valor por 10
for numero in numeros:
    print(numero * 10)

# Manera de recorrer dos listas con la funcion zip(), las dos listas tienen que tener el mismo numero de datos
for numero, animal in zip(numeros, animales):
    print(f'Recorriendo el conjunto 1: {numero}')
    print(f'Recorriendo el conjunto 2: {animal}')

# Creando un bucle con un rango de numeros, el primer parametro es de donde arranca y el ultimo donde termina
# Si le ponemos un solo parametro, inicia desde 0 y termnina en el valor que le dimos
for num in range(5, 10):
    print(num)


# Forma correcta de recorrer un conjunto por su indice
# El tipo de "num" es una tupla, dato para tener en cuenta
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es {indice}, el valor es {valor}')
# En este caso, trabajando con "enumerate", si a num le pasamos
# un 0 nos da el indice solamente y si le pasamos un 1 nos da el valor

# Usando el else con for

for numero in numeros:
    print(f'Ejecutando un bucle con un else, valor actual: {numero}')
else:
    print('El bucle termino')

# Todo lo anterior funciona para tuplas
