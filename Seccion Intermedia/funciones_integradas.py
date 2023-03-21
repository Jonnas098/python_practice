numeros = [4, 7, 1, 42, 15]

#Encontrando el numero mayor de una lista
numero_mayor = max(numeros)
print(numero_mayor)

#Entontrando el numero menor de una lista
numero_menor = min(numeros)
print(numero_menor)

#Redondeando a un decimal
redondeado = round(12.3456, 1)
print(redondeado)

#Retorna False si -> 0, vacio, False, ninguno(None) | True -> datos no vacios
resultado_bool = bool("")
print(resultado_bool)

#Retorna true si todos los valores son verdaderos, cualquier dato que sea falso nos devuelve un False
resultado_all = all([123, 'True', [3, 2, 1], True])
print(resultado_all)

#Suma de todos los valores iterables de una lista
suma_total = sum(numeros)
print(suma_total)

