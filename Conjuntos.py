#Son colecciones de datos  que se utilizan para almacenar varios elementos
# No estan ordenados, son inmutables, no permiten valores duplicados 
# Set = conjunto
#

ciudades =  {'Barranquilla','Cali','Medellin'}
print(ciudades)
print(type(ciudades))
ciudades.add('Bogota') #se puede agregar
ciudades.remove('Cali') #eliminar
#sale desordenado
for i in ciudades:
    print(i)
    
#eliminar numeros duplicados
lista = [0,5,1,2,1,5,5,5,4,5,4,5,7,8,7,8,4,5,1,2,3,9,56,4,26,89,-8]
conjunto = set (lista)
print(conjunto)