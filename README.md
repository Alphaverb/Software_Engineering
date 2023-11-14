# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнила:
- Плясунова Милена Юрьевна
- ПИЭ-21-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |

Работу проверил:
- к.э.н., доцент Панов М.А.

# Лабораторные работы
## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

```python
set_1 = {'White', 'Black', 'Red', 'Pink'}
set_2 = {'Red', 'Green', 'Blue', 'Red'}

print(set_1 - set_2)
```

#### Пример с разными видами повторений:
```python
set_1 = {'White', 'Black', 'Red', 'Pink'}
set_2 = {'Red', 'Green', 'Blue', 'Red'}
print('1', set_1 - set_2)

set_1 = {'White', 'Black', 'Red', 'Pink', 'Black', 'White'}
set_2 = {'Red', 'Green', 'Blue', 'Red'}
print('2', set_1 - set_2)

set_1 = {'White', 'Black', 'Red', 'Pink', 'Red', 'Red'}
set_2 = {'Red', 'Green', 'Blue', 'Red'}
print('3', set_1 - set_2)
```

### Результат.
#### Порядок элементов в результирующем множестве может меняться при каждом запуске программы. Это связано с тем, что множества в Python реализованы как хеш-таблицы, которые не сохраняют порядок элементов для оптимизации производительности:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L511.png)
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L512.png)

#### Пример с разными видами повторений:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L513.png)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

#### set():
```python
a = set('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)
```

#### frozenset():
```python
a = frozenset('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)
```

### Результат.
#### set():
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L521.png)

#### frozenset():
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L522.png)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
def replace(input_list):
    memory = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = memory

    return input_list

print(replace([1, 2, 3, 4, 5]))
```

#### 'Красивое' решение. Получено с использованием срезов списка и конкатенации в нужном порядке:
```python
input_list = [1, 2, 3, 4, 5]
print(input_list[-1:] + input_list[1:-1] + input_list[:1])
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L531.png)

#### 'Красивое' решение:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L532.png)

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
a = [12, 54, 32, 57, 843, 2346, 765, 75, 25, 234, 756, 23]
print(a[2:6])
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L54.png)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
def useless(lst):
    return max(lst) / len(lst)

print(useless([3,5,7,3,33]))
print(useless([-12.5, 54, 77.3, 0, -36, 98.2, -63, 21.7, 47, -89.6]))
print(useless([-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7]))
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L55.png)

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
superheroes = ['superman', 'spiderman', 'batman']

nikolay, vasiliy, ivan = superheroes

print('Николай - ', nikolay)
print('Василий - ', vasiliy)
print('Иван - ', ivan)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L56.png)

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить, что измененная вами информация сохранилась в файле.

```python
a = [-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7]
a.sort()
print('Отсортированный список:\n', a)
a.pop(0)
print('Отсортированный список без наименьшего элемента:\n', a)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L57.png)

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

#### Импорт модуля math целиком:
```python
from random import randint

def list_maker():
    a = [randint(1,100)] * randint(3,10)
    return a

if __name__ == '__main__':
    result = []
    for i in range(randint(1,5)):
        result.append(list_maker())

    print(result)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L58.png)

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст:
### Приветствие
### Спасибо
### Извините
### Пожалуйста
### До свидания
### Ты готов?
### Как дела?
### С днем рождения!
### Удача!
### Я тебя люблю.
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

```python
def superset(set_1, set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1 == set_2:
        print(f'Множества равны')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    else:
        print(f'Супермножество не обнаружено')

if __name__ == '__main__':
    superset({1, 8, 3, 5}, {3, 5})
    superset({1, 8, 3, 5}, {5, 3, 8, 1})
    superset({3, 5}, {5, 3, 8, 1})
    superset({90, 100}, {3, 5})
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L59.png)

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
### • № - номер по порядку (от 1 до 300);
### • Секунда – текущая секунда на вашем ПК;
### • Микросекунда – текущая миллисекунда на часах.
### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
my_list = [2, 5, 8, 3]
print(my_list[::-1])
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/L510.png)

# Самостоятельные работы
## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
receipts = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
            1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
            5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
            5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
            3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

length = len(receipts)
print("Всего выдано чеков: ", length)

unique = len(set(receipts))
print("Количество разных людей, посетивших ресторан: ", unique)

most_frequent = max(receipts, key=receipts.count)
most_frequent_count = receipts.count(most_frequent)

print(f"Код работника, посетившего ресторан больше всего раз: {most_frequent} ({most_frequent_count} раз)")
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/S51.png)

## Выводы

1. Чтобы найти количество уникальных элементов списка, можно преобразовать его в множество с помощью метода set() (т.к. множество - неупорядоченная коллекция
уникальных элементов), а затем найти длину полученного множества с помощью метода len().
2. Метод count() возвращает количество вхождений элемента в списке.
3. Для функции max() можно использовать параметры. В данном случае максимальный элемент находится среди списка receipts, при этом поиск этого элемента осуществляется по количеству его вхождений (ключевая функция - key=receipts.count)).
 
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = sorted(results)
best = sorted_results[:3]
worst = sorted_results[-3:]
begin_with_10 = sorted_results[9:]
print("Список результатов по возрастанию:", sorted_results,
      "\nТри лучших результата: ", best,
      "\nТри худших результата: ", worst,
      "\nРезультаты, начиная с 10: ", begin_with_10)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/S52.png)

## Выводы

1. Функция sorted() возвращает новый отсортированный список итерируемого объекта (списка, словаря, кортежа). По умолчанию она сортирует его по возрастанию.
2. В Python срезы используются для извлечения подсписков из исходного списка. Срез имеет следующую структуру: 'список[начало:конец:шаг]'.
- Срез sorted_results[:3] (best) представляет подсписок списка sorted_results от начала списка (индекса 0) до индекса 3 (3 не включительно, т.е. индексы 0, 1, 2)
- Срез sorted_results[-3:] (worst) представляет подсписок списка sorted_results от индекса -3 до конца списка (индекса -1) (-3 и -1 включительно, т.е. индексы -3, -2, -1)
- Срез sorted_results[9:] (begin_with_10) представляет подсписок списка sorted_results от индекса 9 до конца списка (индекса 19) (9 не включительно, т.е. индексы 10, 11, 12 ... 19)

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
### • Текст в файле:
### Beautiful is better than ugly.
### Explicit is better than implicit.
### Simple is better than complex.
### Complex is better than complicated.
### • Ожидаемый результат:
### Input file contains:
### 108 letters
### 20 words
### 4 lines

```python
from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def min_triangle(list):
    min_element = min(list)
    return min_element

def max_triangle(list):
    max_element = max(list)
    return max_element

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

area_min = triangle_area(min_triangle(one), min_triangle(two), min_triangle(three))
area_max = triangle_area(max_triangle(one), max_triangle(two), max_triangle(three))
print("Площадь треугольника из минимальных значений:", area_min, "\nMin:", min_triangle(one), min_triangle(two), min_triangle(three),
      "\nПлощадь треугольника из максимальных значений:", area_max, "\nMax:", max_triangle(one), max_triangle(two), max_triangle(three))
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/S53.png)

## Выводы

В Python есть несколько способов передачи списка в функцию. Один из самых простых способов – это передача списка как аргумента функции. Для этого нужно указать имя списка в круглых скобках при определении функции и использовать это имя внутри функции для обращения к списку.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
### • Запрещенные слова:
### hello email python the exam wor is
### • Предложение для проверки:
### Hello, world! Python IS the programming language of thE future. My
### EMAIL is....
### PYTHON is awesome!!!!
### • Ожидаемый результат:
### *****, ***ld! ****** ** *** programming language of *** future. My
### ***** **....
### ****** ** awesome!!!!

```python
mark_list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
mark_list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
mark_list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def good_marks(list):
    updated_mark_list = [4 if mark == 3 else mark for mark in list if mark != 2]
    return updated_mark_list

print("Обновленный список оценок для первого варианта:", good_marks(mark_list1),
      "\nОбновленный список оценок для второго варианта:", good_marks(mark_list2),
      "\nОбновленный список оценок для третьего варианта:", good_marks(mark_list3))
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/S54.png)

## Выводы

Функция good_marks принимает исходный список с отметками и возвращает исправленный список, полученный с помощью генератора списков (позволяет создавать новые списки на основе существующих списков или других итерируемых объектов). В новом списке все оценки 3 заменены на 4 (иначе оценка остается без изменения), а оценки 2 исключены из рассмотрения (благодаря условию if grade != 2). В генераторе списка можно использовать любое имя переменной вместо mark (это временная переменная, которая представляет текущий элемент из списка на каждой итерации цикла).

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

### 

```python
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def generate_set(list):
    index = 0
    while index < len(list):
        num_count = list.count(list[index])
        if num_count > 1:
            list[index] = str(list[index]) * num_count
        index += 1
    return set(list)

print("1-ый список: ", generate_set(list_1),
      "\n2-ой список: ", generate_set(list_2),
      "\n3-ий список: ", generate_set(list_3))
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_5/pic/S55.png)

## Выводы

Функция generate_set принимает значение исходного множества, затем, начиная с индекса 0 и до последнего индекса (конца списка), она считает количество вхождений числа заданного индекса, и, если количество вхождений больше 1, то число становится строковой переменной и умножается на количество вхождений - после цикл переходит к следующей итерации.

