#panel data
#2008
#siempre se debe importar
#sepuede hacer operacion con las series

import pandas as pd
diccionario = {
    'a':1,
    'b':2,
    'c':3
}
print (diccionario)

#forma con panda
serie = pd.Series(data=diccionario, index=list(diccionario.keys()))#se pasa el  dic alista
#encoding = "" para tildes y enes
print(serie)
print(serie[1])

