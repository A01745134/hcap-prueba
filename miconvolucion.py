import numpy as np

#Función que calcula la matriz resultante C después de aplicar la operación convolución de A*B
def convolucion(A,B):
	for row in range(len(A)-2):
		for column in range(len(A[0])-2):
			suma = 0
			for i_row in range(len(B)):
				for j_column in range(len(B[0])):
					suma = suma + A[row+i_row][column+j_column]*B[i_row][j_column] 	
			C[row][column] = suma
	return C

#Matriz del ejemplo de la página
Matriz1 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
Filtro = [[1,1,1],[0,0,0],[2,10,3]]

#Matriz del ejercicio.
#Matriz1 =[[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
#Filtro = [[1,0,2],[5,0,9],[6,2,1]]

A = np.array(Matriz1) #Me da una mejor representación al hacer el print.
B = np.array(Filtro)

C = np.zeros((len(A)-2,len(A[0])-2)) #Genera una matriz de ceros que me sirve para inicializar la matriz directamente.

print(np.array(C))
print(convolucion(A,B))

