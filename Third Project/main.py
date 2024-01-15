from matriz import Matrix
from vector import Vector

# Ejemplo de uso
matriz1 = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
matriz2 = Matrix(2, 3, [7, 8, 9, 10, 11, 12])

print("Matriz 1:")
print(matriz1)

print("Matriz 2:")
print(matriz2)

matriz_suma = matriz1.sum(matriz2)
print("Suma:")
print(matriz_suma)

matriz_resta = matriz1.difference(matriz2)
print("Resta:")
print(matriz_resta)

matriz_multiplicacion = matriz1.multiplication(2)
print("Multiplicación por escalar:")
print(matriz_multiplicacion)

matriz_transpuesta = matriz1.transpuesta()
print("Transpuesta:")
print(matriz_transpuesta)

# Uso de la clase Vector
vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])

print("Vector 1:")
print(vector1)

print("Vector 2:")
print(vector2)
