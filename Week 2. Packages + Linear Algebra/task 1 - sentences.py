# Задача 1: сравнение предложений
#
# Дан набор предложений, скопированных с Википедии. Каждое из них имеет "кошачью тему" в одном из трех смыслов:
#
# кошки (животные)
# UNIX-утилита cat для вывода содержимого файлов
# версии операционной системы OS X, названные в честь семейства кошачьих
# Ваша задача — найти два предложения, которые ближе всего по смыслу к расположенному в самой первой строке.
# В качестве меры близости по смыслу мы будем использовать косинусное расстояние.
#
# Выполните следующие шаги:
# 1. Скачайте файл с предложениями (sentences.txt).
# 2. Каждая строка в файле соответствует одному предложению. Считайте их, приведите каждую к нижнему регистру
# с помощью строковой функции lower().
# 3. Произведите токенизацию, то есть разбиение текстов на слова. Для этого можно воспользоваться регулярным выражением,
# которое считает разделителем любой символ, не являющийся буквой: re.split('[^a-z]', t). Не забудьте удалить
# пустые слова после разделения.
# 4. Составьте список всех слов, встречающихся в предложениях. Сопоставьте каждому слову индекс от нуля до (d - 1),
# где d — число различных слов в предложениях. Для этого удобно воспользоваться структурой dict.
# 5. Создайте матрицу размера n * d, где n — число предложений. Заполните ее: элемент с индексом (i, j)
# в этой матрице должен быть равен количеству вхождений j-го слова в i-е предложение. У вас должна получиться матрица
# размера 22 * 254.
# 6. Найдите косинусное расстояние от предложения в самой первой строке (In comparison to dogs, cats have not undergone...)
# до всех остальных с помощью функции scipy.spatial.distance.cosine. Какие номера у двух предложений, ближайших к нему
# по этому расстоянию (строки нумеруются с нуля)? Эти два числа и будут ответами на задание. Само предложение
# (In comparison to dogs, cats have not undergone... ) имеет индекс 0.
# 7. Запишите полученные числа в файл, разделив пробелом. Обратите внимание, что файл должен состоять из одной строки,
# в конце которой не должно быть переноса. Пример файла с решением вы можете найти в конце задания (submission-1.txt).
# 8. Совпадают ли ближайшие два предложения по тематике с первым? Совпадают ли тематики у следующих по близости предложений?
#
# Разумеется, использованный вами метод крайне простой. Например, он не учитывает формы слов (так, cat и cats
# он считает разными словами, хотя по сути они означают одно и то же), не удаляет из текстов артикли и прочие ненужные слова.
# Позже мы будем подробно изучать анализ текстов, где выясним, как достичь высокого качества в задаче поиска похожих предложений.

#
# См. аналогичную задачу здесь: http://a92661qd.bget.ru/quests/mathematics_and_python/371/

# Все принты кроме вывода в файл перед сдачей работы удалить!!!

import re
import numpy as np
from scipy import spatial
import matplotlib

with open("sentences.txt") as file_obj:
# with open("anaconda.txt") as file_obj:
    sentenceList = list(map(lambda x: x.lower(), map(lambda x: x.strip(), file_obj.readlines())))
print(sentenceList)

sentenceWordList = list(map(lambda t: re.split('[^a-z]', t), sentenceList))  # регулярное выражение, считающее разделителем любой символ, не являющийся буквой
sentenceWordList = [list(filter(lambda word: word != "", sentence)) for sentence in sentenceWordList]
# print(sentenceWordList)
print()

words = dict()
for sentence in sentenceWordList:
     for word in sentence:
         words[word] = words.get(word, 0) + 1
print(words)
# print(len(words))

countOfInput = np.array([[sentenceWordList[i].count(word) for word in words] for i in range(len(sentenceWordList))])
print(countOfInput)
# print(spatial.distance.cosine.__doc__)
dist = [spatial.distance.cosine(countOfInput[0], countOfInput[i]) for i in range(0, len(countOfInput))]
print(dist)
sortDist = sorted(zip(dist, range(len(dist))))
print(sortDist)
print(sortDist[1][1], sortDist[2][1])
# Domestic cats are similar in size to the other members of the genus Felis, typically weighing between 4 and 5 kg (8.8 and 11.0 lb).
# In one, people deliberately tamed cats in a process of artificial selection, as they were useful predators of vermin.
with open("sentences_output.txt", "w") as outFile:
# with open("anaconda_output.txt", "w") as outFile:
    print(sortDist[1][1], sortDist[2][1], file=outFile)
print(sentenceList[sortDist[1][1]], "/n", sentenceList[sortDist[2][1]])
print(sortDist[3][1], sortDist[4][1])
print(sentenceList[sortDist[3][1]], "/n", sentenceList[sortDist[4][1]])


# Введение
# В этом задании вы познакомитесь с некоторыми базовыми методами из линейной алгебры, реализованными в пакете SciPy —
# в частности, с методами подсчета косинусного расстояния и решения систем линейных уравнений. Обе эти задачи
# еще много раз встретятся нам в специализации. Так, на решении систем линейных уравнений основана настройка
# линейных моделей — очень большого и важного класса алгоритмов машинного обучения. Косинусное расстояние же
# часто используется в анализе текстов для измерения сходства между ними.
#
#
# Материалы
# Справка по функциям пакета scipy.linalg: http://docs.scipy.org/doc/scipy/reference/linalg.html
# Справка по работе с файлами в Python: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# Справка по регулярным выражениям в Python (если вы захотите узнать про них чуть больше): https://docs.python.org/2/library/re.html
