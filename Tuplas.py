#coleccion de datos y se parece a las listas, se utilizan para almacenar varios datos
#las tuplas son ordenadas y son inmutables /
#son colecciones indexadas /
#se usan parentesis

frutas = ('Manzana','Piña', 'pera') #tupla =parentesis
nombres = ['Carlos', 'Pedro', 'Ana'] #lista =corchetes

datospersonales = ('Juan', 50, True, 250,[ 0,1,2]) #Se puede almacenar diferentes variables
print(frutas)
print(frutas[0])

# futas[1] = 'mango'  no se puede realizar esto, las tuplas son inmutables
print(type(frutas), type(nombres))
print(datospersonales)
print(datospersonales[4][2]) #imprime el 2

datospersonales[4][2]= 56
print(datospersonales)

#esta funcion es una tupla ya que, retorna varios valores a la vez
def operaciones(a,b):
    suma = a+b
    resta = a-b
    mul = a*b
    div = a/b
    return suma, resta, mul, div

resultados = operaciones( 85,5)
print(resultados)
print(type(resultados))

for i in datospersonales:
    print(i)