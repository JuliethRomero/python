def cliente(informacion:dict)->dict:
    if informacion['edad'] > 18:
        atraccionV = 'X-Treme'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            valord= (20000*0.05)
            total_boleta= (20000- valord)
        else:
            total_boleta= 20000

    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccionV = 'Carroschocones'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            valord= (5000*0.07)
            total_boleta= (5000 - valord)
        else:
            total_boleta= 5000


    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccionV = 'Sillas voladoras'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            valord= (10000*0.05)
            total_boleta= (10000- valord)
        else:
            total_boleta= 10000


    else:
        atraccionV = 'N/A'
        aptoV = False
        total_boleta = 'N/A'



    dicSalida = {
        'nombre':informacion['nombre'],
        'edad':informacion['edad'],
        'atraccion': atraccionV,
        'apto': aptoV,
        'primer_ingreso':informacion['primer_ingreso'],
        'total_boleta' : total_boleta
       
    }
    return dicSalida


# Esto que esta de aquí en adelante NO se sube a imaster
informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez', 
    'edad': 20, 
    'primer_ingreso': True    
}
print(cliente(informacion)) 