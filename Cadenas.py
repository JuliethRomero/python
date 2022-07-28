#son inmutables
animal = "Cocodrilo"
print(animal [4])
print(len(animal)) # len es una funcion q nos devuleve la longitud
#animal[5]= "L" no se puede porque las cadenas son inmutables
animal = "leon"
print(animal)
#print(animal.isnumeric()) #/ METODOS -- # es una funcion con el 
# objeto (animal) 

#Rebanadas 
animal= "elefante"
print(animal [2:4])
print(animal[:5])
print(animal[5:])
print(animal[-2]) #las posiciones negativas de derecha a izquierda

#for de python
for i in animal: #toma los valores de cada posicion de la cadena o string
    print (i)
  
  #for en otros lenguajes.  
for i in range(len(animal)):
    print(animal[i]) 
    