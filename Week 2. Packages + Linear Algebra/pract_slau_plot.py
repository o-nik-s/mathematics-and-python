# Для следующего задания используйте 6 точек: (0,1), (1,1), (2,25), (-1,1), (-2,-23), (0.5,0.90625)

# После завершения задачи 5 вы получили список точек.
# Найдите многочлен, проходящий через все эти точки.
# Постройте график многочлена.
# Для построения графика используйте модуль matplotlib (документация: http://matplotlib.org/api/pyplot_api.html ).

# Учитывайте интервал, на котором строится график!

import numpy
import matplotlib.pyplot as plt
# %matplotlib inline

def f(x, c):
    # return c[0] + c[1] * x + c[2] * x**2 + c[3] * x**3 + c[4] * x**4 + c[5] * x**5
    return [sum(c[j] * x[i] ** j for j in range(len(c))) for i in range(len(x))]

xy = [(0, 1), (1, 1), (2, 25), (-1, 1), (-2, -23), (0.5, 0.90625)]
rangem = range(len(xy))
x = [xy[i][0] for i in rangem]
y = [xy[i][1] for i in rangem]
print(x, y)
X0n = [[x[i]**j for j in rangem] for i in rangem]
print(X0n)
A = numpy.array(X0n)
b = numpy.array(y)
print(A, b)
print(numpy.linalg.det(A))
c = numpy.linalg.solve(A, b)
print(c)
print(*map(str, c))
x = numpy.arange(-2, 2, 0.1) # Массив значений аргумента
y = f(x, c)
print(x, y, sep="\n")
plt.plot(x, y)  # Построение графика
plt.xlabel(r'$x$')  # Метка по оси x в формате TeX
plt.ylabel(r'$f(x)$')  # Метка по оси y в формате TeX
plt.grid(True)  # Сетка
plt.show() # Показать график
