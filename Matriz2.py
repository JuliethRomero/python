#matriz de solo ceros
#siempre se debe importar numpy as np

import numpy as np
matriz = np.zeros((4,4), dtype=np.int8)
print(matriz)

#matriz de solo unos
matriz2 = np.ones((2,2), dtype=np.int8)
print(matriz2)

#matriz de un valor
matriz3 = np.full((2,2),8)
print(matriz3)

matriz = np.full((2,2),'Julieth')
print(matriz)

#matriz numeros aleatorio
matriz = np.random.random((3,3))
print(matriz)

#matriz identidad
matriz = np.eye(3)
print(matriz)

#rebanadas
matriz4 = np.array([[5,6,8],[6,5,4],[5,6,3]])
print(matriz4)
matriz5 = matriz4[:3,:1]
print(matriz5)