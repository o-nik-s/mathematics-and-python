# Задача 1.2 - система 2 линейных уравнений
import numpy
a11, a12, b1 = map(float, input().split())  # a11, a12, b1 = [int(x) for x in input().split()]
a21, a22, b2 = map(float, input().split())
A = numpy.array([[a11, a12], [a21, a22]])  # Матрица (левая часть системы)
b = numpy.array([b1, b2])  # Вектор (правая часть системы)
if numpy.linalg.det(A) == 0:
    print("Система не имеет решений")
else:
    print(*numpy.linalg.solve(A, b))

'''
import numpy
inpt=[]
for i in input().split():
    inpt.append(int(i))
for i in input().split():
    inpt.append(int(i))
M1 = numpy.array([[inpt[0],inpt[1]],[inpt[3],inpt[4]]])
V1 = numpy.array([inpt[2],inpt[5]])
if numpy.linalg.det(M1) !=0:
    ans=numpy.linalg.solve(M1, V1)
    print(' '.join(map(str, ans)))
else: 
    print('Система не имеет решений')
'''