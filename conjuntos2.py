#Operaciones de los conjuntos
#union , interseccion, diferencia, diferencia simetrica
# operdadores /      Metodos    /         descripcion 
# |  alt+124      union                     union 
# &               intersecction             interseccion 
# -               difference                Diferencia
# ^               symmetric_difference      diferencia simetrica

cultivoszonaA = {'papa', 'maiz', 'trigo'}
cultivozonaB = {'platano', 'maiz', 'caña'}

print(cultivoszonaA | cultivozonaB)
print(cultivoszonaA & cultivozonaB)
print(cultivoszonaA - cultivozonaB)
print(cultivoszonaA ^ cultivozonaB)
#imprime lo mismo
print(cultivoszonaA.union(cultivozonaB))
print(cultivoszonaA.intersection(cultivozonaB))
print(cultivoszonaA.difference(cultivozonaB))
print(cultivoszonaA.symmetric_difference(cultivozonaB))