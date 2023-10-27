# Тема 4. Функции и модули
Отчет по Теме #4 выполнила:
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
### Напишите функцию, которая выполняет любые арифметические действия и выводит результат в консоль. Вызовите функцию используя “точку входа”.

```python
def main():
    print(2 + 2)
    
if __name__ == '__main__':
    main()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L41.png)

## Лабораторная работа №2
### Напишите функцию, которая выполняет любые арифметические действия, возвращает при помощи return значение в место, откуда вызывали функцию. Выведите результат в консоль. Вызовите функцию используя “точку входа”.

```python
def main():
    return 2 + 2

if __name__ == '__main__':
    print(main())
```

#### Развернутый вид:
```python
def main():
    result = 2 + 2
    return result

if __name__ == '__main__':
    answer = main()
    print(answer)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L421.png)

#### Развернутый вид:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L422.png)

## Лабораторная работа №3
### Напишите функцию, в которую передаются два аргумента, над ними производится арифметическое действие, результат возвращается туда, откуда эту функцию вызывали. Выведите результат в консоль. Вызовите функцию в любом небольшом цикле.

```python
def main(one, two):
    result = one + two
    return result

for i in range(5):
    x = 1
    y = 10
    answer = main(x, y)
```

#### Аргументы передаются в вызове функции:
```python
def main(one, two):
    return one + two

for i in range(5):
    answer = main(one=1, two=10)
    print(answer)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L431.png)

#### Аргументы передаются в вызове функции:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L432.png)

## Лабораторная работа №4
### Напишите функцию, на вход которой подается какое-то изначальное неизвестное количество аргументов, над которыми будет производится арифметические действия. Для выполнения задания необходимо использовать кортеж “*args”. Для закрепления понимания работы с кортежами настоятельно рекомендуем поменять аргументы вызова функции, вручную посчитать результат, только потом запустить программу с новыми значениями и проверить себя, насколько вы поняли данный аспект программирования.

```python
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"one={one}\ntwo={two}\nthree={three}")

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nresult={result}")
```

#### Пример со своими значениями:
```python
def main(x, y, z, *args):
    one = x
    two = len(args)
    three = y
    four = sum(args)
    five = z
    print(f"one = {one}\ntwo = {two}\nthree = {three}\nfour = {four}\nfive = {five}")

    return x + str(two/four) + three + five

if __name__ == '__main__':
    result = main('We are ', ' times more ', 'effective', 1701, 113, 1.618, 42)
    print(f"\nresult = {result}")
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L441.png)

#### Пример со своими значениями:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L442.png)

## Лабораторная работа №5
### Напишите функцию, которая на вход получает кортеж “**kwargs” и при помощи цикла выводит значения, поступившие в функцию. Вызовите функцию используя “точку входа”.

```python
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0], z=[2, 3, 0], q=[3, 3, 0], w=[3, 3, 0])
    print()
    main(**{'x': [1, 2, 3], 'y': [3, 3, 0]})
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L45.png)

## Лабораторная работа №6
### Напишите две функции. Первая – получает в виде параметра “**kwargs”. Вторая считает среднее арифметическое из значений первой функции. Вызовите первую функцию используя “точку входа” и минимум 4 аргумента.

```python
def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data)/float(len(data))

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0])
```

#### Пример с 4-мя аргументами:
```python
def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data)/float(len(data))

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0], z=[22, 44, 6], r=[11, 7, 3])
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L461.png)

#### Пример с 4-мя аргументами:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L462.png)

## Лабораторная работа №7
### Создайте дополнительный файл .py. Напишите в нем любую функцию, которая будет что угодно выводить в консоль, но не вызывайте ее в нем. Откройте файл main.py, импортируйте в него функцию из нового файла и при помощи “точки входа” вызовите эту функцию.

#### L471:
```python
def say_hello():
    print('Hello students!')
```

#### L472:
```python
from L471 import say_hello

if __name__ == '__main__':
    say_hello()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L47.png)

## Лабораторная работа №8
### Напишите программу, которая будет выводить корень, синус, косинус полученного от пользователя числа.

#### Импорт модуля math целиком:
```python
import math

def main():
    value = int(input('Введите значение: '))
    print(math.sqrt(value))
    print(math.sin(value))
    print(math.cos(value))

if __name__ == '__main__':
    main()
```

#### Импорт трех необходимых функций из модуля math:
```python
from math import sqrt, sin, cos

def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()
```

#### Импорт модуля math целиком (укороченный синтаксис):
```python
from math import *

def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()
```

### Результат.
#### Импорт модуля math целиком:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L481.png)

#### Импорт трех необходимых функций из модуля math:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L482.png)

#### Импорт модуля math целиком (укороченный синтаксис):
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L483.png)

## Лабораторная работа №9
### Напишите программу, которая будет рассчитывать какой день недели будет через n-нное количество дней, которые укажет пользователь.

```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input('Введите количество дней: '))
    today = dt.today()
    result = today + td(days=n)
    print (
        f"Через {n} дней будет {result.date()}. "
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L49.png)

## Лабораторная работа №10
### Напишите программу с использованием глобальных переменных, которая будет считать площадь треугольника или прямоугольника в зависимости от того, что выберет пользователь. Получение всей необходимой информации реализовать через input(), а подсчет площадей выполнить при помощи функций. Результатом программы будет число, равное площади, необходимой фигуры.

```python
global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def triangle():
    a = float(input("Основание: "))
    b = float(input("Высота: "))
    global result
    result = 0.5 * a * b

figure = input("1 - прямоугольник, 2 - треугольник: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/L410.png)

# Самостоятельные работы
## Самостоятельная работа №1
### Дайте подробный комментарий для кода, написанного ниже. Комментарий нужен для каждой строчки кода, нужно описать что она делает. Не забудьте, что функции комментируются по-особенному.

```python
from datetime import datetime
from math import sqrt

def main(**kwargs):
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        print(result)

if __name__ == '__main__':
    start_time = datetime.now()
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )

    time_costs = datetime.now() - start_time
    print(f"Время выполнения программы - {time_costs}")
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/S41.png)

## Выводы

```python
from datetime import datetime # импорт функции datetime из модуля datetime
from math import sqrt # импорт функции sqrt из модуля math

def main(**kwargs):
""" Функция нахождения квадратного корня от суммы квадратов значений (чисел списка) ключа из словаря kwargs """
    for key in kwargs.items(): # для ключа из элементов словаря kwargs
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        """
        Вычисляем значение result, которое является квадратным корнем от суммы квадратов двух чисел из списка. 
        key[1][0] - элемент ключа 1 (список) со значением индекса 0 (первое число из списка)
        key[1][1] - элемент ключа 1 (список) со значением индекса 1 (второе число из списка)
        Если взять значение key[0][0], то оно будет браться непосредственно из названия ключа (для аргумента one это было бы значение o, для аргумента two - t и т.д.)
        """
        print(result) # выводим результат вычислений в консоль

if __name__ == '__main__':
    start_time = datetime.now() # задаем переменную начала времени работы программы
    main( # передаем в функцию main именованные аргументы (ключ и список значений)
        one=[10, 3], # ключ one, значения 10 и 3
        two=[5, 4], # ключ two, значения 5 и 4
        three=[15, 13], # ключ three, значения 15 и 13
        four=[93, 53], # ключ four, значения 93 и 53
        five=[133, 15] # ключ five, значения 133 и 15
    )
    time_costs = datetime.now() - start_time # задаем переменную, в которой находим разницу текущего времени и времени начала работы программы (находим общее время работы программы)
    print(f"Время выполнения программы - {time_costs}") # выводим время работы программы
```

## Самостоятельная работа №2
### Напишите программу, которая будет заменять игральную кость с 6 гранями. Если значение равно 5 или 6, то в консоль выводится «Вы победили», если значения 3 или 4, то вы рекурсивно должны вызвать эту же функцию, если значение 1 или 2, то в консоль выводится «Вы проиграли». При этом каждый вызов функции необходимо выводить в консоль значение “кубика”. Для выполнения задания необходимо использовать стандартную библиотеку random. Программу нужно написать, используя одну функцию и “точку входа”.

```python
from random import *

def roll():
    num = randint(1, 6)
    print(f"Значение кубика: {num}")

    if num in [5, 6]:
        print("Вы победили")
    elif num in [3, 4]:
        print("Вы продолжаете игру...")
        roll()
    else:
        print("Вы проиграли")

if __name__ == "__main__":
    roll()
```

### Результат.
#### Проигрыш:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/S421.png)

#### Выигрыш:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/S422.png)

## Выводы

1. Метод randint() в Python возвращает случайное целочисленное значение между двумя нижними и верхними пределами (включая оба ограничения).
2. В программе используется рекурсия (вызов функции внутри самой себя), благодаря которой можно продолжать игру, если выпало нужное значение.

## Самостоятельная работа №3
### Напишите программу, которая будет выводить текущее время, с точностью до секунд на протяжении 5 секунд. Программу нужно написать с использованием цикла. Подсказка: необходимо использовать модуль datetime и time, а также вам необходимо как-то “усыплять” программу на 1 секунду.

```python
from datetime import *
from time import *

def time():
    start_time = datetime.now()
    while datetime.now() - start_time < timedelta(seconds=5):
        current_time = datetime.now()
        print(current_time.strftime('%X'))
        sleep(1)

if __name__ == "__main__":
    time()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_4/pic/S43.png)

## Выводы

1. Объект timedelta (часть модуля datetime) в Python используется для выполнения манипуляций с датой и временем, представляет собой продолжительность времени.
2. Метод strftime() (часть модуля datetime) преобразует объект типа datetime в строку. %X обозначает время в формате 'HH:MM:SS'.
3. Метод Python sleep() (часть модуля time) используется для приостановки (задержки) выполнения текущего потока на заданное количество секунд.

## Самостоятельная работа №4
### Напишите программу, которая считает среднее арифметическое от аргументов вызываемое функции, с условием того, что изначальное количество этих аргументов неизвестно. Программу необходимо реализовать используя одну функцию и “точку входа”.

```python
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
countV = 0

string = (input('Введите предложение на английском: '))
print('Длина предложения: ', len(string))
print('Предложение в нижнем регистре: ', string.lower())

for i in range(0, len(string)-1, 1):
    for j in range(0, len(vowels)-1, 1):
        if vowels[j] == string[i]:
            countV += 1
print(f"Количество гласных в предложении: {countV}")

if "ugly" in string:
    noUgly = string.replace("ugly", "beauty")
    print('Замена ugly на beauty: ', noUgly)

if string.startswith('The'):
    print('Строка начинается на The')
else:
    print('Строка не начинается на The')

if string.endswith('end'):
    print('Строка заканчивается на end')
else:
    print('Строка не заканчивается на end')
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_3/pic/S341.png)
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_3/pic/S342.png)
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_3/pic/S343.png)

## Выводы

1. Для нахождения всех гласных в предложении был использован вложенный цикл. Задача решена полным перебором букв введенного предложения и букв списка с гласными vowels. 
- Сначала запускается внешний цикл, который отвечает за перебор букв введенной строки. Внешний цикл фиксирует очередное значение итерируемой переменной i, с каждым шагом цикла будет смещение по индексу на следующую букву.
- Далее запускается внутренний цикл, отвечающий за перебор букв из списка vowels и изменяющий значение итерируемой переменной j. Она обозначает смещение по элементу списка. Таким образом, проверяется соответсвие буквы из предложения и буквы из списка гласных.
2. Функция replace() в Python возвращает копию строки, в которой все вхождения подстроки заменяются другой подстрокой.
3. Метод startswith() возвращает True, если строка начинается с указанного префикса (строки). Если нет, возвращается False.
4. Метод endwith() возвращает True, если строка заканчивается указанным суффиксом. Если нет, возвращается False.

## Самостоятельная работа №5
### Создайте два Python файла, в одном будет выполняться вычисление площади треугольника при помощи формулы Герона (необходимо реализовать через функцию), а во втором будет происходить взаимодействие с пользователем (получение всей необходимой информации и вывод результатов). Напишите эту программу и выведите в консоль полученную площадь.


```python
values = [0, 2, 4, 6, 8, 10]
counter = 0
string = 'hello'
memory = ' world'

while counter != 10:
    if counter in values:
        print(string + memory)
        print(string)
    counter += 1
string = string + ' world'
memory = string
print(memory)

```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_3/pic/S35.png)

## Выводы

Пока счетчик (counter) не равен 10, выполняется цикл while. Если значение счетчика равняется какому-либо числу из списка values, то происходит вывод строк 'hello world' и 'hello'. На каждом шаге цикла значение counter увеличивается на 1. Условие 'if counter in values' проходит по всем элементам values, кроме 10, значит всего будет выведено 5 строк 'hello world' и 'hello'. После окончания цикла while для переменной string определяется новое значение - 'string + ' world''. После переменной memory присваиваем значение string и выводим ее в консоль. Программа завершена, итог - всего вывелось 5 строк 'hello' и 6 строк 'hello world'.
