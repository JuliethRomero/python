# Realice un programa que lea el código numérico de un producto como llave de un 
# diccionario y en dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario y debe permitir consultar un producto 
# por su llave.

#Aplicaciones CRUD, create, read, update, delete
#agrgar que podamos cambiar precio o cantidad de un producto y  que se pueda borrar productos
def crear(productos):
    codigo = int(input('Digite el código\n'))
    nombre = input('Digite el nombre del producto\n')
    precio = int(input('Digite el precio unitario del producto\n'))
    cantidad = int(input('Digite la cantidad del producto\n'))
    #productos.setdefault(codigo,[nombre, precio, cantidad]) Esta linea es los mismoque la 14
    #Son formas diferentes de a.adir llaves al diccionario
    productos[codigo] = [nombre, precio, cantidad]
    print('Producto creado')
    print(productos[codigo])
    return productos

def mostrar(productos):
    print('Listado de productos')
    print('Codigo', 'Nombre', 'Precio','Cantidad', sep = "\t\t")# es precionar tabulacion
    for i in productos:
        print(i, productos[i][0], productos[i][1], productos[i][2], sep="\t\t")
    

def consultar(productos):
    cod = int(input('Digite el codigo del producto que desea consultar'))
    if cod in productos:
        print('Codigo', 'Nombre', 'Precio','Cantidad', sep = "\t\t")
        print( cod, productos[cod][0], productos[cod][1], productos[cod][2], sep="\t\t")
    else:
        print('El codigo del producto no existe')
        
def actualizar(productos):
    cod = int(input('Digite el codigo del producto que desee actualizar'))
    if cod in productos:
        precio = int (input('Digite el precio unitario del producto\n'))    
        cantidad = int(input('Digite la cantidad que existe en el producto\n'))
        productos[cod][1]=precio
        productos[cod][2]= cantidad
        print("Producto actualizado")
    else:
        print("El codigo del producto no existe")
        
def borrar(productos):
    cod = int(input('Digite el codigo del producto que desee borrar\n'))
    if cod in productos:
       print("producto eliminado:", productos.pop(cod))   
    else:
        print('El codigo del producto no existe')  
          
continuar = 's'
productos = {
    1:['manzana', 2500, 80],
    2:['pera', 3000, 90],
    3:['banana', 500, 1500]
}
while continuar == 's' or continuar == 'S':
    try:
        print('MENU')
        print('1. Crear producto')
        print('2. Mostrar productos ')
        print('3. Consultar producto')
        print('4. Actualizar o cantidad')
        print('5. Borrar producto')
        opcion = int(input(f'Digite una de las tres opciones [1/2/3/4/5]:\n'))
        if opcion == 1:
            crear(productos)
        
        elif opcion == 2:
            mostrar(productos)
        elif opcion == 3:
            consultar(productos)
        elif opcion == 4:
            actualizar(productos)   
        elif opcion == 5:
            borrar(productos)
        else:
            print('Digite una opción valida')
    except:
        print("Digite una opcion valida de tipo numerica")
    continuar = input('Presione "s" para continuar o cualquier letra para salir\n') 
    