objeto = {
    'nombre' : "John Navarro",
    'emocion' : True,
    'altura' : 1.85,
    'dato_duplicado' : "John Navarro"
}

#print(objeto['altura'])

edad = 20

if edad >= 18:
    print('Podes pasar')
else:
    print('No puedes pasar')
    
salario = 100000

if salario >= 10000:
     print('Prueba 1')
elif salario > 1000 :
     print('Prueba 2')
else :
     print('Prueba 3')
    
#Metodos de cadenas
cadena1 = 'Prueba de cadena'
cadena2 = 'Otra prueba de cadena'

resultado = cadena1.replace('cadena', 'reemplazo')

#print(resultado)

split_test = cadena2.split(' ')
print(split_test)


x = 0 
while x < 20:
    x = x + 3
    #print(x)
    
