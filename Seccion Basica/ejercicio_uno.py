#Ejercicio 1
other_courses_min = 2.5 
other_courses_max = 7
other_courses_prom = 4
course = 1.5

crudo_promedio = 5
crudo_course = 3.5

text = '.'

#Diferencias de duracion

#Esta es la diferencia del curso respecto al promedio maximo de tiempo usando la funcion round()
diferencia_max = 100 - course / other_courses_max * 100
print(f'Esta es la diferencia optima {round(diferencia_max, 1)}')

dif_min = 100 - course / other_courses_min * 100
dif_max = 100 - course * 1000 // other_courses_max / 10
dif_prom = 100 - course / other_courses_prom * 100

print(dif_min)
print(dif_max)
print(dif_prom)

print(f'{text:.^50}')

#Forma menos optima
tiempo_vacio_promedio = 100 - other_courses_prom * 1000 // crudo_promedio / 10
tiempo_vacio_curso = 100 - course * 1000 // crudo_course / 10

print(f'Elimino un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'El curso elimina un {tiempo_vacio_curso}% de tiempo vacio')

#Forma optima
vacio_prom = 100 - other_courses_prom / crudo_promedio * 100
vacio_curso = 100 - course / crudo_course * 100

print(f'El vacio promedio optimizado es: {round(vacio_prom, 1)}')
print(f'El curso elimina {round(vacio_curso, 1)} de tiempo vacio, optimizado')

#Otra manera
print(f'{other_courses_prom * 100 // course / 10}')
