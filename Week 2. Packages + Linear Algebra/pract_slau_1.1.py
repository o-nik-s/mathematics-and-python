# Задача 1.1 - система 2 линейных уравнений
import numpy
a11, a12, b1 = map(float, input().split())  # a11, a12, b1 = [int(x) for x in input().split()]
a21, a22, b2 = map(float, input().split())
M1 = numpy.array([[a11, a12], [a21, a22]])  # Матрица (левая часть системы)
v1 = numpy.array([b1, b2])  # Вектор (правая часть системы)
r = numpy.linalg.solve(M1, v1)  # Находим решение системы
print (r[0], r[1])
