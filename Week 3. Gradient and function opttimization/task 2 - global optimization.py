# Задача 2. Глобальная оптимизация
# 1. Теперь попробуем применить к той же функции f(x) метод глобальной оптимизации — дифференциальную эволюцию.
# 2. Изучите документацию и примеры использования функции scipy.optimize.differential_evolution.
# 3. Обратите внимание, что границы значений аргументов функции представляют собой список кортежей (list,
# в который помещены объекты типа tuple). Даже если у вас функция одного аргумента, возьмите границы его значений
# в квадратные скобки, чтобы передавать в этом параметре список из одного кортежа, т.к. в реализации
# scipy.optimize.differential_evolution длина этого списка используется чтобы определить количество аргументов функции.
# 4. Запустите поиск минимума функции f(x) с помощью дифференциальной эволюции на промежутке [1, 30].
# Полученное значение функции в точке минимума - ответ в задаче 2. Запишите его с точностью до второго знака после запятой.
# В этой задаче ответ - только одно число.
# 5. Заметьте, дифференциальная эволюция справилась с задачей поиска глобального минимума на отрезке, т.к. по своему устройству
# она предполагает борьбу с попаданием в локальные минимумы.
# 6. Сравните количество итераций, потребовавшихся BFGS для нахождения минимума при хорошем начальном приближении,
# с количеством итераций, потребовавшихся дифференциальной эволюции. При повторных запусках дифференциальной эволюции
# количество итераций будет меняться, но в этом примере, скорее всего, оно всегда будет сравнимым с количеством итераций BFGS.
# Однако в дифференциальной эволюции за одну итерацию требуется выполнить гораздо больше действий, чем в BFGS.
# Например, можно обратить внимание на количество вычислений значения функции (nfev) и увидеть, что у BFGS
# оно значительно меньше. Кроме того, время работы дифференциальной эволюции очень быстро растет
# с увеличением числа аргументов функции.


import math
from scipy.optimize import differential_evolution
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

def fn(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


min, max, step = 0, 30, 0.1
x = np.arange(min, max, step)  # Массив значений аргумента
y = fn(x)
# print(x, y, sep="\n")
plt.plot(x, y)  # Построение графика
plt.xlabel(r'$x$')  # Метка по оси x в формате TeX
plt.ylabel(r'$f(x)$')  # Метка по оси y в формате TeX
plt.grid(True)  # Сетка
# plt.show()  # Показать график


min, max, res, digit = 1, 30, [], 2
# print(differential_evolution(func=f, bounds=[(1, 30)]))
res.append(differential_evolution(func=f, bounds=[(min, max)]))
print(res[0])
print(round(res[0].fun, digit)) # Первый ответ на задание
with open("global_optimization.txt", "w") as outFile:
    outFile.write(str(round(res[0].fun, digit)))


'''
from scipy.optimize import differential_evolution
import numpy as np
def ackley(x):
    arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
    arg2 = 0.5 * (np.cos(2. * np.pi * x[0]) + np.cos(2. * np.pi * x[1]))
    return -20. * np.exp(arg1) - np.exp(arg2) + 20. + np.e
bounds = [(-5, 5), (-5, 5)]
result = differential_evolution(ackley, bounds)
print(result.x, result.fun)
'''

'''
from scipy.optimize import rosen, differential_evolution
bounds = [(0,2), (0, 2), (0, 2), (0, 2), (0, 2)]
result = differential_evolution(rosen, bounds)
print(result.x, result.fun)
'''