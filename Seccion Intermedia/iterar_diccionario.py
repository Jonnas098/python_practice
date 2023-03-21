diccionario = {
    'nombre' : "John",
    'apellido' : "Navarro",
    'edad' : 24
}

#Iterando con .items() nos devuelve una tupa clave valor para cada elemento del diccionario
for key in diccionario.items():
    print(key)

#Aqui mostramos la clave y el valor en un string
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key} y el valor es: {value}')