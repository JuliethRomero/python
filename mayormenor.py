#realice un programa que lea n numeros enteros y nos diga cuale es mayor
#de ellos y cual es menor de ellos
#Datos de entrada: la cantidad de numeros y los n numeros 
#Datos de salida: el mayor y el menor


n = int(input("Digite la cantidad de numeros que desea ingresar \n"))
for i in range(n): #este for cuanta de 0 a n-1
    numero= int (input(f"Digite el numero {i+1}\n"))
    if i ==0:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero    
print(f"El mayor de los {n} numeros ingresados es {mayor}")   
print(f"El menor de los {n} numeros ingresados es {menor}") 

         
