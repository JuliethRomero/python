#importar datos
from re import A
import pandas as pd
import json

#df = pd.read_json('archivojson.json')
#print(df)

dicstring = '{"nombre": "Juan", "edad": 25, "profesion":"contados"}'
ajson = json.loads(dicstring)
print(ajson['nombre'])
A=json.loads(dicstring)
print(A)

#
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "profesion":"contados",
    "hijos": ["ana","Julían"],
    "mascotas" : None,
    "divorciado":False
}
B = json.dumps(diccionario,indent=4, separators= ("," , "="), ensure_ascii=False)
print(B)
#ident= es los espacios que deja el programa a la izquierda
#ensure_ascii es para que valide las tildes 

#c = json.dumps("Colombia")
#print(c)