# r= leer, es elparametro por defecto, si el archivo no existe sale error
# w= escribir,abre el archivo para escribir desde la primera line,
#si el archivo no existe lo crea
# a= agrega, llll

#lectura
from encodings import utf_8


archivo1 = open('archivotxt.txt', 'r')
print(archivo1.readlines())
print(archivo1)
print(archivo1.readline())
print(archivo1.read(4))
print(archivo1.read())
archivo1.close()

#Escribir
archivo2 = open("archivotxt.txt", 'w')
archivo2.write("Hola mundo2 \n")
archivo2.write("Hola mundo2 \n")
archivo2.close()

lista = ["cali", "popayan", "Medellin"]
#Agregar
archivo3 = open("archivotxt.txt", 'a', encoding='utf_8')
archivo3.write("Esta es una prueba\n")
for i in lista:
    archivo3.write(i)
    archivo3.write("\n")
archivo3.close()

