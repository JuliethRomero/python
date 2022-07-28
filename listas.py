#Son estructuras  de datos que se utilizan para guardar varios elementos en una sola variable/ a diferencia de dicionarios no tiene a misma estructura llave-valor
#las listas son mutables
#las listas son indexadas/cada elemento se encuentra en una posicion
#tambien tienen posiciones
#se usa corchetes.
#para añadir se usa  append

Marcascarros = ['Nissan', 'Audi', 'chevrolet', 'renault']
print(Marcascarros[1])
Marcascarros[1]= 'toyota'
print(Marcascarros[1])

datosP = [ 'carlos', 40, 'Medellin', [10,50,20]]
print(type(datosP), type(datosP[2]))

#imprimir cada elemento de la lista/recorrer estructuras de datos
for i in datosP:
    print(i)
    
    
#para agragar
datosP.append("contador")
print(datosP)

#qutar elementos
datosP.remove("contador")
print(datosP)

