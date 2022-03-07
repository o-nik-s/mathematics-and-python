# Задача 2 - система 3 линейных уравнений
import numpy
n = 3
AL, bL = [], []
for i in range(n):
    inpt = list(map(int, input().split()))
    AL.append(inpt[:-1])
    bL.append(inpt[-1])
A = numpy.array(AL)  # Матрица (левая часть системы)
b = numpy.array(bL)  # Вектор (правая часть системы)
if numpy.linalg.det(A) == 0:
    print("Система не имеет решений")
else:
    print(*numpy.linalg.solve(A, b))
