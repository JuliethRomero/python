import pandas as pd

lista1 = [1,2,3]
lista2 = [4,4,5]

lista3 = lista1+lista2
print(lista3)

print(lista3[0:3])
print(lista3[:3])
print(lista3[4:])
print(lista3[2:5])

a = 5 
a = a+1

#if en una sola linea,se puede si el interior de if es de una instruccion


#compresion de lista:
#metodo tradicional
cuadrados = []
lista = [2,3,6,4,8]
for i in lista:
    cuadrados.append(i**2)
print(cuadrados)
#otra forma
cuadrados2= [i**2  for i in lista]
print(cuadrados2)


a = 56236545.256
b = round(a,2)
print(f'el numero es  {b:,.2f}')

ventas1 = pd.Series([15,12,21]) # c/indice implicito
print(ventas1)
ventas = pd.Series([15,12,21], index = ["Ene", "Feb", "Mar"]) # c/indice explicito
print(ventas)

datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }
compras = pd.DataFrame( datos )
print(compras)

# Diccionario
datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }

compras = pd.DataFrame( datos , index = [ 'Luis' , 'Roberto' , 'Liliana' , 'David' ])   
print(compras)