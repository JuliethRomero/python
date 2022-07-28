#Realizar un programa que indique si una persona debe presentar la declaracion de renta
#las condiciones para presentar impuestos son
#ser mayor de edad y tener ingresos anuales superiores o iguales a
#50.831.000
#operador logico or

edad = int(input("Digite su edad: \n")) #\n salto de linea
ingresos = int(input("Digite sus ingresos anuales sin puntos ni comas: \n"))

if edad < 18 or ingresos < 50831000:
    print("Usted no debe presentar declaracion de renta.")
else:
    print("Usted debe presentar la declaracion de renta.")
print("Programa finalizado")


    


