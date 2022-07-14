# python-course

Lesson #1

Высокоуровневый интерпретируемый язык программирования. Впервые упомянут в 1991 году.

кросплатформенный язык, который подходит для:
- Веб-сервисов
- ML, Data Science, Аналитики, игр (не лучший выбор)
- Написания софта.

Переменные:
В python есть несколько базовых типов: int, float, boolean, str, list и др.

Python - язык с динамической типизацией.

Lesson #2

Как работать с файлами
Связать файловую переменную с файлом, определив модификатор работы:
a - открытие для добавления данных.
r - открытие для чтения данных.
w - открытие для записи данных.
w+ и r+.

запись данных с закрытием файла
```
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)
data.close()
```

Запись данных без необходимости закрывать файл
```
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
```

Чтение данных из файла
```
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
```

Функции
```
def fib(n):
    if n in [1, 2]:
        return 1
    else:
    return fib(n - 1) + fib(n - 2)
```

Кортежи, или неизменяемые списки
```
a = (3, 4)
print(a)
print(a[0])
```
```
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{}, g:{}, b:{}'.format(red, green, blue))
```

Словари - неупорядоченные коллекции произвольных объектов с достпуом по ключу.
```
dictionary = {}
dictionary = \
    {
        'up': '^',
        'left': '<',
        'right': '>',
        'down': 'v'
    }

    print(dictionary)
    print(dictionary['left'])

    for k in dictionary.keys():
        print(k)
```