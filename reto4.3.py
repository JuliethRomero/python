def ordenes(rutinaContable):
    from functools import reduce
    listaTotales=list(map(lambda x: [x[0]]+list(map(lambda z:z[1]*z[2] ,x[1:])),rutinaContable))# segun el pdf debe ser listatotales

    listaTotales=list(map(lambda x: [x[0]]+[reduce(lambda acumulador,elemento: round(acumulador+elemento,2),x[1:])],listaTotales))
    

    listaTotales=list(map(lambda x: x if x[1]>=600000 else[x[0], x[1]+25000],listaTotales))
    print('------------------------ Inicio Registro diario ---------------------------------')
    rango = range(0,len(listaTotales))
    for i in rango:
        print (f'La factura {listaTotales[i][0]} tiene un total en pesos de {listaTotales[i][1]}')
    print('-------------------------- Fin Registro diario ----------------------------------')