#sintaxis
#reduce(funcion,objeto iterable)

from functools import reduce

lista = [1,2,3,4,5,6]
acumulador = 0
for i in lista:
    acumulador +=i
print(acumulador)

#otra forma
resultado = reduce(lambda acumulador, numero: acumulador+numero,lista )
print(resultado)

