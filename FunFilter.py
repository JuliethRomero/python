#sintaxis
# filter(funcion, objeto iterable)

#obtener los pares de una lista

lista = [2,4,85,1,0,5,3]

def pares (numero):
    return numero%2==0
listadep = tuple(filter(pares,lista))
print(listadep)

#lambda
#sin terminar
listapares2 = tuple(filter(lambda numero: numero%2==0, lista))
print(listapares2)

