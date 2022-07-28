datosPersonales = {
    "nombre" : "Carlos",
    "Edad" : 40,
    "ID" : 32124,
    "Telefono"  : 3224057730,
    "Direccion" : "calle 70  b sur",
    "PermisoAR" : True,
    "hijos" : {"Hijo1": "maria", "Hijo2": "sofia"}
}

for i in datosPersonales : #la variable i toma los valores de las llaves
    print(i)
    
for i in datosPersonales : #imprime los valores de cada llave.
    print(datosPersonales[i])

#metodos
#copy
datosPersonales2 = datosPersonales.copy()
print(datosPersonales2)
#clear
datosPersonales2.clear()
print(datosPersonales2)
#pop borra una llave y devuelve su valor
print(datosPersonales.pop("hijos"))
print(datosPersonales)
#print(datosPersonales[1]) , los indices no funcionan como llaves 
