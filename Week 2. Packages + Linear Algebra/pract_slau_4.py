# Задача 4 - система произвольного числа линейных уравнений

import numpy
n = int(input())
AL, bL = [], []
for i in range(n):
    inpt = list(map(float, input().split()))
    AL.append(inpt[:-1])
    bL.append(inpt[-1])
A = numpy.array(AL)  # Матрица (левая часть системы)
b = numpy.array(bL)  # Вектор (правая часть системы)
if not(numpy.linalg.det(A)):
    print("Система не имеет решений")
else:
    print(*numpy.linalg.solve(A, b))

'''
import numpy
n = int(input())
a = [[float(j) for j in input().split()] for i in range(n)]
M1 = numpy.array([[a[i][j] for j in range(n)] for i in range(n)])
v1 = numpy.array([a[i][n] for i in range(n)])
print('Система не имеет решений' if numpy.linalg.det(M1) == 0 else ' '.join(str(i) for i in numpy.linalg.solve(M1, v1)))
'''