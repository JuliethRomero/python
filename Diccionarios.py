#variables que almacena tipo de dato compuesto/ es una estructura de datos
#se utiliza para almacenar datos o valores en pares llamados clave-valor
#o llave-valor
# clave : valor, ejemplo->> "nombre" : 'Marina', "ciudad": "barranquilla"
#Son mutables y no permite llaves duplicadas
datosPersonales = {
    "nombre" : "Carlos",
    "Edad" : 40,
    "ID" : 32124,
    "Telefono"  : 3224057730,
    "Direccion" : "calle 70  b sur",
    "PermisoAR" : True,
    "hijos" : {"Hijo1": "maria", "Hijo2": "sofia"}
    
}

dic = { "a": "c", "d": 4}
'''
print(datosPersonales["Telefono"])
print(datosPersonales)
datosPersonales["Direccion"] = "carrera 75"
print(datosPersonales)
'''
print(type(datosPersonales),type(datosPersonales["PermisoAR"]),type (datosPersonales["Edad"]))

