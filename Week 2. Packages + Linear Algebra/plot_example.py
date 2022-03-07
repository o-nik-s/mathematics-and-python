# Пример построения графика многочлена

import numpy
import matplotlib.pyplot as plt
# %matplotlib inline
c = [1., -2., 3., -4., 5.]

def f(x, c):
    return c[0]+c[1]*x+c[2]*x**2+c[3]*x**3+c[4]*x**4

x = numpy.arange(0,5.01,0.1) #Массив значений аргумента
plt.plot(x, f(x, c)) #Построение графика
plt.xlabel(r'$x$') #Метка по оси x в формате TeX
plt.ylabel(r'$f(x)$') #Метка по оси y в формате TeX
plt.grid(True) #Сетка
plt.show() #Показать график

# Учитывайте интервал на котором строится график!