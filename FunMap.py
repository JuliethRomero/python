#sintaxis
#map recorre como for
# map(funcion,objeto iterable)
#toma una fucnion y se lo aplica a todo oi
#no se puede imprimir directamente

from functools import reduce
from math import pow 

def cuadrado(numero):
    return numero**2

lista = [4,4,5,5,8,6,7,8,9]


cuadrados = list(map(cuadrado,lista))
print(cuadrados)

#forma mas corta con funcion lambda
lista = [4,4,5,5,8,6,7,8,9]
cuadrados2 = list(map(lambda numero: numero**2 , lista))
print(cuadrados2)

#otra forma con la funcion pow
bases = [2,3,4,5,6,7,8,9]
potencias = [2,1,3,4,5,6,7,8]

resultados = list(map(pow, bases, potencias))
print(resultados)

#Ejemplo
lista = [
    [1525, [4, 2500],[3,8500],[5,12600]], #[No. factura, [cantidad. precio unidad]...]
    [1520, [3, 2500],[8,12600]],
    [1622, [1, 2500],[5,8500],[2,12600]]    
]

#Generar una lista de listas: [[no.factura, total1, total2,.. totaln]]
total = list(map(lambda x: [x[0]]+list(map(lambda Y: Y[0]*Y[1],x[1:])),lista))
print(total)

#crear una lista de listas: [[Nfactura, total factura], ...]
total = list(map(lambda x:[x[0]] + [reduce (lambda y,z:  y+z,x[1:])] , total ))
print(total)