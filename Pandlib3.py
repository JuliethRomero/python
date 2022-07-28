import pandas as pd
df1= pd.read_csv('surveys.csv')
print(df1.head(15))#imprimelas 15 lineas 
print(df1.tail(10))#imprime las ultimas lineas
print(df1.shape) #esto es una caracteristica del data frame
print(df1.columns) #esto es una caracteristica del data frame
print(pd.unique(df1['species_id'])) #imprime los datos unicos de una columna
print(df1['species_id'].value_counts()) #cuenta los datos unicos de  una columna

#metodo describe, muestra un resumen de ddatos de estadistica descriptiva, se le puede aplicar
#a una columna
print(df1['weight'].describe())
print(df1['weight'].mean())
print(df1.groupby('species_id')['record_id'].count()['AH'])
