import pandas as pd
import numpy as np

inventario = {
    'impresoras': ['canon', 'hp', 'epson'],
    'cantidad': [10, 8, 15]
}
print(inventario,'\n')
df1 = pd.DataFrame(inventario, index=['p1','p2','p3'])
print(df1, '\n')
print(df1.iloc[1])
print(df1.loc['p1'])

#crear matriz de datos con numpy 3*3

arreglo = np.array([[4,5,6],[4,5,3],[7,8,9]])
print(arreglo, '\n')

df2 = pd.DataFrame(arreglo, columns = ['Juan','Ana','Lia'], index=['Enero', 'Febrero', 'Marzo'])
print(df2,'\n')
print(df2.loc['Enero'])
print(df2.columns)
print(df2.iloc[1])