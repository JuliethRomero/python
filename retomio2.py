
def cliente(informacion:dict)->dict:
    if informacion ['edad'] >18:
        atraccionV = 'X-Treme'
        aptoV = True
    elif informacion ['edad'] >= 15 and informacion['edad'] <= 18:
        atraccionV = 'Carroschocones'
        aptoV = True
    elif informacion['edad']>=7 and informacion ['edad'] < 15:
        atraccionV= 'Sillas voladoras'
        aptoV = True
    else:
        atraccionV = "N/A"
        aptoV = False
        totalBoleta = "No aplica"
        
dicSalida = {
    'nombre':informacion ['nombre'],
    'edad' :informacion ['edad'],
    
    
}

#esto no se pone en imaster
informacion = {
   'id_cliente' : 1,
   'nombre': 'Johana Fernandez',
   'edad' : 20,
   'primer_ingreso': True
}

print(cliente(informacion))

