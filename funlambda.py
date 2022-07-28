#Es anonima, no tiene nombre
#es una funcion peque;a de una sola linea
#sintaxis->> labda arguments : expression


suma= lambda a,b : a+b
print(suma(8,7))

def acumulador(n):
    return lambda a: a+n

tempo = acumulador(2)

print(tempo(4))
print(tempo(7))
print(tempo(6))

#a toma el valor de tempo 
#n tome el valor de 2