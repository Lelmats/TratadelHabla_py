import numpy as np
#Formas de crear arreglos de numpy (ndarray)#

#Con una lista de python
datos = np.array([1, 2, 3])
print(datos)

print()

print("------Con una lista multidimensional-------")

print()

#Con una lista multidimensional de python
datos = np.array([[1, 2], [3, 4]])
print(datos)

print()

#Con constantes#
print()
print("------Con constantes-------")
print()
print("------Con Ceros-------")
print()

#Ceros
datos = np.zeros((5, 3))
print(datos)

print()

print("------Con Unos-------")

print()

#Unos
datos = np.ones(4)
print(datos)

print()

print("-------Matriz------^")

print()

#Matriz
datos = np.ones((4, 3), dtype = np.int64) 
print(datos)
print(datos.dtype)

print()

print("-------------")

print()

print("------Constantes arbitrarias-------")

print()

#Constantes arbitrarias
datos = np.ones((4, 3)) * 3.5
datos = np.full((4, 3), 3.5)
print(datos)

print()

datos = np.empty((4, 3))
datos.fill(7.4)
print(datos)

print()

print("------Secuencias Incrementales-------")

print()

#Secuencias Incrementales
#Arange excluye el stop y siempre incluye el start
#Si no se especifica start es 0 y step es 1
datos = np.arange(15)
#Start, Stop, Step
datos = np.arange(3, 15, 4)

print()
print(datos)
print()

datos = np.linspace(0,10,11)

print(datos)
print()
print(datos.shape)

print()
print("------Secuencias Logarimicas-------")
print()

#Secuencias logaritmicas
# 10**0 10**2 5 elementos
# 1     100   5

datos = np.logspace(0,2,5)
print(datos)
print()
print(datos.shape)

print()
print("------Meshgrid-------")
print()

x = np.array([1,2,3,4,5])
y= np.array([6,7,8])

XX, YY = np.meshgrid(x,y)

print(XX)
print()
print(XX.shape)
print()
print(YY)
print()
print(YY.shape)

print()
print("------Arreglos Crea Array 0 y 1-------")
print()

#Crea Array 0 y 1
#shape y dtype
datos = np.ones_like(XX)
datos = np.zeros_like(XX)
datos = np.full_like(XX,3.5)

print()
print(datos)

print()
print("------Matrices-------")
print()

#Matrices
#Crea Array diagonalmente
datos = np.identity(4)
print(datos)

print()
print("------Matriz Eye-------")
#Offset de fila k
print()

datos = np.eye(4, k=0)
print(datos)

print()
print("------Matriz Diagonal Custom-------")
#Matriz diagonal custom
print()

datos = np.diag(np.array([0,1,2,3]))
print(datos)

