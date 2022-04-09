import numpy as np
import sys
import time

arreglo = np.array([1,2,3,4,5,6,7,8,9])
print("Arreglo de una dimension")
print(arreglo)
print()

arreglob = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print("Arreglo de dos dimensiones")
print(arreglob)
print()

memoria = range(1000)
print("Memoria utilizada")
print(sys.getsizeof(5) * len(memoria))
print()

memoriab = np.arange(100)
print("Memoria utilizada con numpy")
print(memoriab.size * memoriab.itemsize) 
print()

SIZE = 1000
L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
resultado = [(x,y) for x,y in zip(L1, L2)]
print("Tiempo de ejecución")
print((time.time()-start)*1000)
print()

start = time.time()
resultado = A1 + A2
print("Tiempo de ejecucion con numpy")
print((time.time()-start)*1000)

matrizuno = np.ones((3,4))
print("Matriz de unos")
print(matrizuno)
print()

matrizceros = np.zeros((3,4))
print("Matriz de ceros")
print(matrizceros)
print()

matrizaleatorios = np.random.random((3,4))
print("Matriz de numeros aleatorios")
print(matrizaleatorios)
print()

