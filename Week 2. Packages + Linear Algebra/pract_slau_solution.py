# Задача 5 - Найти коэффициенты многочлена
#
# Напишите программу, находящую коэффициенты многочлена n-й степени, проходящего через n+1 точку:
# c0+c1x1+c2x2+⋯+cnxn
#
# Программа должна принимать на вход в 1й строке натуральное число M (M=n+1) после этого в цикле M строк.
# Каждая из M строк содержит 2 действительных числа: xi, yi - координаты M точек,
# через которые проходит график многочлена.
# На выходе программа должна выдавать через пробел n+1 (n+1=M) коэффициент многочлена:
# c0,c1,c2…cn
#
# Подсказка. Для этого необходимо решить систему n+1 линейных уравнений:
# f(x1)=c0+c1x1^1+c2x1^2+....+cnx1^n
# f(x2)=c0+c1x2^1+c2x2^2+....+cnx2^n
# ...
# f(xn)=c0+c1xn^1+c2xn^2+....+cnxn^n
# f(xn+1)=c0+c1xn+1^1+c2xn+1^2+....+cnxn+1^n

import numpy

m = int(input())  # n + 1
rangem = range(m)
xy = [tuple(map(float, input().split())) for i in rangem]
print(xy)
x = [xy[i][0] for i in rangem]
y = [xy[i][1] for i in rangem]
print(x, y)
X0n = [[x[i]**j for j in rangem] for i in rangem]
print(X0n)
A = numpy.array(X0n)
b = numpy.array(y)
print(A, b)
print(numpy.linalg.det(A))
if not(numpy.linalg.det(A)):
    print("Система не имеет решений")
else:
    c = numpy.linalg.solve(A, b)
    print(c)
    print(*map(str, c))
