#Creando un diccionario con dict()

diccionario = dict(nombre = 'John', apellido = 'Navarro')

#Crear un diccionario con fromkeys
#De esta manera el valor por defecto de cada key es "none"
diccionario_fk = dict.fromkeys(["nombre", "apellido", "edad"])

print(diccionario_fk)