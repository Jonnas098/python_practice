#Muestra la el nombre del mes en consola de manera larga ya abreviada
from datetime import date

today = date(2022, 10, 7)
print('Nombre del mes: ', today.strftime("%B"))
print('Nombre del mes acortado: ', today.strftime("%b"))


#Facturacion, areas y cotizaciones por John Navarro Ramirez

"""En esta parte voy a definir las variables donde abrán dos medidas standart de tablilla, ademas del area que cubica cada accesorío y estructura para la instalación del material"""

#Furring
furr = float (0.6)

#Angular
ang = float (0.5)

#Canal
canl = float (0.19)

#Tablilla de 20x5.95
tabl20 = float (1.19)

#Tablilla de 25x5.95
tabl25 = float (1.48)

#Cornisa
cor = float (5.95)

#Uniones
uni = float (5.95)

#Jotas
jot = float (5.95)

#Esquinero externo
ext = float (5.95)

#Esquinero interno
int = float (5.95)


#Espacio para las funciones

def artab():
     tot20 = (peri / tabl20)
     print ("La cantidad necesaria de tablilla es:", tot20, "piezas.")

def artab25():
    tot25 = (peri / tabl25)
    print ("Necesitará un total de", tot25, "piezas.")

def arcor():
    totcor = (peri / cor)
    print ("El area requiere un total de", totcor, "cornisas.")

def aruni():
    totuni = (peri / uni)
    print ("Su proyecto requiere un total de", totuni, "uniones.")

def arjot():
    totjot = (peri / jot)
    print ("Necesitará", totjot,"jotas.")

def arext():
    totext = (peri / ext)
    print ("Necesita", totext, "esquineros externos.")

def arint():
    totint = (peri / int)
    print ("Necesita", totint, "esquineros internos.")

def arfurr():
    totfur = (peri * furr)
    print ("Requiere", totfur, "furing.")

def arang():
    totang = (peri * ang)
    print ("Requiere", totang, "angulares.")

def arcanl():
    totcanl = (peri * canl)
    print ("Requiere", totcanl, "canales.")

#Momento de pedir la info del usuario tipo menu y desarrollo del app como tal

print ("______________________________________________________________________________")
print ("Bienvenido, nuestro programa le brindará una rápida solución a sus nececidades para determinar la cantidad de material necesário para su proyecto")
print ("______________________________________________________________________________")

peri = float (input("Ingrese la cantidad de metros cuadrados que posee el area a estudiar"))

print ("______________________________________________________________________________")

tab = input ("Desea saber el area de tablilla de 20 o 25 centimetros de ancho?")

print ("______________________________________________________________________________")

if tab == "20":
    print (artab())
elif tab == "25":
    print (artab25())

corni = input ("Necesita cornisa?")
if corni == "Si":
    print (arcor())
elif corni == "No":
    pass

perf = input ("Necesita perfilería?")
if perf == "Si":
    print (arext(), arint(), arjot(), aruni())
elif perf == "No":
    pass

estru = input ("Necesita estructura metálica?")
if estru == "Si":
    print (arfurr(), arang(), arcanl())
    print ("______________________________________________________________________________")
    print ("Muchas gracias por su consulta, estamos para servirle")
    print ("______________________________________________________________________________")
elif estru == "No":
    print ("______________________________________________________________________________")
    print ("Muchas gracias por su consulta, estamos para servirle")
    print ("______________________________________________________________________________")

