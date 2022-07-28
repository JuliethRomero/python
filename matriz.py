

import numpy as np
matriz = np.array([4,5,8])
print(matriz, matriz.shape, type(matriz), matriz[2]) #shape=forma del dato

#matriz(2,3)
matriz2 = np.array([[1,2,3],[4,5,6]])
print(matriz2,matriz2.shape,type(matriz2),matriz2[1,1])

#matriz3
print('_______')
matriz3 = np.array([[[1,2,3,50],[5,4,6,9]],
                    [[5,2,3,6],[5,5,6,2]],
                    [[4,5,6,7],[1,2,3,4]]])

print(matriz3,matriz3.shape, matriz3[1,1,3])

#matriz4

matriz4 = np.array([[1,2],[5,7]])
print(matriz4,matriz4.shape)

#suma
print( matriz + matriz2)
print(np.add( matriz, matriz2 ))

print( matriz * matriz2)
print(np.multiply( matriz, matriz2 ))