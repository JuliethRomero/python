from re import A
import tkinter as tk
 #crear una clase
class APLICACION:
    def __init__(self) :
        self.ventana1 = tk.Tk()
        self.ventana1.title('Mini Calculadora')
        self.etiqueta1= tk.Label(self.ventana1, text= "Ingrese Numero 1")
        self.etiqueta1.grid(row=0, column=0)
        self.etiqueta2 = tk.Label(self.ventana1, text= "Ingrese Numero 2")
        self.etiqueta2.grid(row=0, column=1)
        #entradas, capturar datos/string para texto
        self.num1 = tk.StringVar() #definir
        self.num2 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana1, textvariable = self.num1 )
        self.entrada1.grid(row=1, column=0)
        self.entrada2 = tk.Entry(self.ventana1, textvariable = self.num2 )
        self.entrada2.grid(row=1, column=1)
        #radiumbotton/int var para numeros/solo deja escoger 1 opcion
        self.opcion = tk.IntVar() #definir variable
        self.opcion1 = tk.Radiobutton(self.ventana1, text="Suma", value=1, variable= self.opcion)
        self.opcion1.grid(row=2, column=0)
        
        self.opcion2 = tk.Radiobutton(self.ventana1, text="Resta", value=2, variable= self.opcion)
        self.opcion2.grid(row=3, column=0)
        
        self.opcion3 = tk.Radiobutton(self.ventana1, text="Multiplicacion", value=3, variable= self.opcion)
        self.opcion3.grid(row=4, column=0)
        
        self.opcion4 = tk.Radiobutton(self.ventana1, text="Division", value=4, variable= self.opcion)
        self.opcion4.grid(row=5, column=0)
        
        self.boton1 = tk.Button(self.ventana1, text="Calcular", command=self.Calcular)
        self.boton1.grid(row=6,column=0)
        self.etiqueta3 = tk.Label(self.ventana1, text='---', foreground='red')
        self.etiqueta3.grid(row=6, column=1)
        self.ventana1.mainloop() #para q retorne 
    def Calcular(self):
        if self.opcion.get()==1:
            op= float(self.num1.get()) + float(self.num2.get())
            self.etiqueta3['text'] = op #para que aparezca el resultado en la etiqueta 3
        if self.opcion.get() ==2:
            op= float(self.num1.get()) - float(self.num2.get())
            self.etiqueta3['text'] = op
        if self.opcion.get() ==3:
            op= float(self.num1.get()) * float(self.num2.get())
            self.etiqueta3['text'] = op
        if self.opcion.get() ==4:
            op= float(self.num1.get()) / float(self.num2.get())
            self.etiqueta3['text'] = op
#crear un objeto
x = APLICACION()