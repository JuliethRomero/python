print("inicio")
def saludo(): #sin parametros
    print("Hola mundo")

for i in range(3):
    saludo()

def suma(a,b):#funcion con parametros/cuando define la funcion 
    resultado= a+b
    print("La suma es: ",resultado)
a= int(input("Digite el numero 1: "))
b= int(input("Digite el numero 2:  "))

suma(a,b)
#suma(20,10)  #funcion con argumentos/datos cuanto llama la  funcion

def resta(a,b):
    return a-b

print("la resta es: ",resta(a,b))

#format
#otra forma de mostrar el resultado.
totales = "La resta1 es: {} y la resta2 es: {}"
print(totales.format(resta(a,b),resta(a,b)))

#f-strings
edad=20
nacionalidad= "colombiana"
print(f"La persona tiene{edad}  anos y es {nacionalidad}")
