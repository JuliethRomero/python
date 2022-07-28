import pandas as pd

df1 = pd.read_csv('surveys.csv')
print(df1.columns)
df2 = df1['month'] #aqui se crea un subconjunto de una columna
df3 = df1[['species_id','plot_id']]#aqui se crea un subconjunto de varias columnas es un datafram
print(df2)
print(df3)
print(type(df2),type(df3)) #serie y dataframe
#iloc usa dos parametros,para extraer rangos 
print(df1.iloc[5]) #imprime la linea N de un dataframe
print(df1[10:21]) #formas distintas de obtener sectores del dataframe
print(df1.iloc[0:4,1:3]) #rangos, no lee el ultimo o sea 4 filas/columnas
print(df1.iloc[[0,5,8],:])
print(df1.iloc[8,2]) #extraes informacion sectorizada 
#print(df1.iloc[[2,5],['year','species_id']])

#filtros/ 

print(df1[df1.year == 1977])#sacar toda la info del a;o 19777
print(df1[(df1.year>=1985) & (df1.year<=1995) ])  #and  &, or:  not: C