#CDT

def CDT(usuario:str, capital:int, tiempo:int):
    if tiempo <=2:
        valorap= (capital*0.02)
        valortotal1=  (capital - valorap)
        
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valortotal1}"
    else :
      Valorin= (capital * 0.03 *tiempo)/12
      valortotal= Valorin + capital
      return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valortotal}"
  
  
print(CDT("AB1012", 1000000,3))
print(CDT("ER3366", 650000,2))

            
