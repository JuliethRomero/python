#conversion de cadenas
cadena ='ventana'
lista = list (cadena)
tupla = tuple(cadena)
conjunto = set (cadena)
print(lista, tupla, conjunto)

#conversion de listas a cadena

listas = ['M','A','R']
cadena = ''.join(listas) #se puede poner un caracter si quiero
print(cadena)

#conversion de tuplas

tupla = ( 'a', 'b','c')
cadena = ''.join(tupla)
print(cadena)

#conversion de diccionarios a /// hola 
#zip = funcion de python tiene dos argumentos, elemntos iterables= que se puede recorrer / crea una tupla (0,h)
#range = rango o numero de letras

#diccionario a cadena
cadena ='colombia'
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)
#diccionario a conjunto
conjunto = {3,6,9}
diccionario2 = dict(zip(range(len(conjunto)), conjunto))
print(conjunto)


#DE  DICCCIONARIO HACIA OTROS ELEMENTOS
Diccionaro = {
    0:'h',
    1:'o',
    2:'l',
    3:'a'
}
cadenadevalores = ''.join(Diccionaro.values()) #esto saca los valores de las llaves
print(cadenadevalores)

#tupla
#.items= crea una tupla de llave y valor

#
lista1 = ['enero', 'febrero', 'marzo']
lista2= [200, 300, 280]

diccionario3 = dict(zip(lista1,lista2))
print(diccionario3)
