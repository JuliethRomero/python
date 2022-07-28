#Diseñe un programa para calcular la hipotenusa de 
# un triangulo rectangulo
#DAtos de entrada: a y b (Cateto opuesto y cateto adyacente 
# Datos sa: H
#operadores aritmeticos 
# + - * / %(modulo) **(potencia) //(division entera)
# P  parentesis
# E  exponentes
# M  multiplicacion  
# D  division
# A  adicion
# S  sustracion
#Raiz cuadrada  se hace con exponentes 

def pitagoras(a,b):
    h = (a**2 + b**2)**0.5
    return  f"La hipotenusa es : {h}"

a = int (input("Digite el cateto adyacente: "))
b = int (input("Digite el cateto opuesto: "))   

      
print(pitagoras(a,b))