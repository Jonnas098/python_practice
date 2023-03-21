frutas = ['manzana', 'pera', 'banana', 'fresa', 'ciruela', 'durazno']
cadena = 'Hola John'
numeros = [2, 5, 8, 10]

#Saltarse un dato de una lista pasandole su valor
for fruta in frutas:
    if fruta == 'ciruela':
        continue
    print(f'Me voy a comer una {fruta}')

print('---------------------')

#Aqui no se ejecuta el else porque el break cancela todo eso
#tendriamos que poner el ultimo print sin else para poder verlo en consola
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break
else:
    print('Ya no como mas frutas porque me duele la panza')

#Recorrer una cadena de texto

for letra in cadena:
    print(letra)

#For en una sola linea de codigo
#Tenemos la operacion matematica que multiplica *2 cada valor y luego el for que itera la lista
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
