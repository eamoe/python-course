# python-course

# Python Course

## Lesson 1

Высокоуровневый интерпретируемый язык программирования. Впервые упомянут в 1991 году.

кросплатформенный язык, который подходит для:
- Веб-сервисов
- ML, Data Science, Аналитики, игр (не лучший выбор)
- Написания софта.

Переменные:
В python есть несколько базовых типов: int, float, boolean, str, list и др.

Python - язык с динамической типизацией.

## Lesson 2

### Как работать с файлами

Связать файловую переменную с файлом, определив модификатор работы:
a - открытие для добавления данных.
r - открытие для чтения данных.
w - открытие для записи данных.
w+ и r+.

### Запись данных с закрытием файла
```python
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)
data.close()
```

### Запись данных без необходимости закрывать файл
```python
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
```

### Чтение данных из файла
```python
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
```

### Функции
```python
def fib(n):
    if n in [1, 2]:
        return 1
    else:
    return fib(n - 1) + fib(n - 2)
```

### Кортежи, или неизменяемые списки
```python
a = (3, 4)
print(a)
print(a[0])
```

```python
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{}, g:{}, b:{}'.format(red, green, blue))
```

### Словари
Словари - неупорядоченные коллекции произвольных объектов с достпуом по ключу.
```python
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

## Lesson 3
Lambda-функции

```python
#def sum(x, y):
#    return x + y

sum = lambda x, y: x + y

def multiply(x, y):
    return x * y

def calc(operation, x, y):
    print(operation(x, y))

calc(sum, 4, 5)
```

List Comprehension
```python
list = [i for i in range(1, 20) if i % 2 == 0]
print(list)
```

Map
```python
li = [x for x in range(1, 20)]
i = list(map(lambda x: x + 10 li))
print(li)
```

Filter
```python
data = [x for x in range(1, 20)]

result = list(filter(lambda x: not x % 2, data))

print(result)
```

Zip
```python
users = ['user_1', 'user_2', 'user_3']
ids = [1, 2, 3]

data = list(zip(users, ids))

print(data)
```