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

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L71.png)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L72.png)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L73.png)

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L74.png)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L75.png)

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L76.png)

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить, что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.
#### До:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L771.png)

#### После:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L772.png)

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)

print_docs('/Users/Alphaverb/Desktop/Учеба/Ресурсы/Скрины')
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L78.png)

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
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L791.png)

#### Свой пример:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L792.png)

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
### • № - номер по порядку (от 1 до 300);
### • Секунда – текущая секунда на вашем ПК;
### • Микросекунда – текущая миллисекунда на часах.
### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                        datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.
#### Использован плагин ExcelReader:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L710.png)

# Самостоятельные работы
## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

#### Подсчет слов с учетом предлогов, союзов и символов:
```python
with open('article.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    words = content.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)
count = word_count[most_common_word]

print("Наиболее часто встречающееся слово:", most_common_word)
print("Количество:", count)
```

#### Подсчет слов с исключением некоторых предлогов, союзов и символов (можно дополнить):
```python
with open('article.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    words = content.split()
    word_count = {}
    excluded_words = ['и', 'или', 'в', 'на', 'с', 'к', 'от', 'до', 'что', '—']

    for word in words:
        if word not in excluded_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)
count = word_count[most_common_word]

print("Наиболее часто встречающееся слово:", most_common_word)
print("Количество:", count)

```

### Результат.
#### Статья:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S711.png)
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S712.png)

#### Предлоги, союзы и символы учитываются:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S713.png)

#### Предлоги, союзы и символы исключены:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S714.png)

## Выводы

1. Контекстный менеджер with гарантирует правильное закрытие файла после его использования.
2. Метод split() разбивает строку на части, используя как разделитель какой-то символ (или символы) и возвращает список строк. По умолчанию в качестве разделителя используются пробельные символы (пробелы, табы, перевод строки), но в скобках можно указать любой разделитель. Содержимое файла article.txt разбивается на отдельные слова, результат сохраняется в списке words.
3. В цикле проверяется, есть ли слово в полученном списке (если не нужно учитывать предлоги, союзы и символы, то перед этим идет проверка на отсутствие слова в списке исключенных слов (excluded_words)), если слово уже встречалось, то к счетчику прибавляется 1, иначе счетчик равен 1. Затем конечным переменным присваивается значение слова, которое повторилось максимальное количество раз и само количество повторений.
 
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
import csv

def load_data():
    with open('expenses.csv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def save_data(data):
    fieldnames = ['№', 'Дата', 'Категория', 'Содержание операции', 'Расходы']
    with open('expenses.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_expense(data):
    if data:
        num = len(data) + 1
    else:
        num = 1

    date = input("Введите дату: ")
    category = input("Введите категорию: ")
    detail = input("Введите содержание операции: ")
    spent = input("Введите потраченную сумму: ")

    expense = {'№': num, 'Дата': date, 'Категория':  category, 'Содержание операции':  detail, 'Расходы': spent}
    return expense

def delete_expense(data, expense_num):
    for expense in data:
        if int(expense['№']) == expense_num:
            data.remove(expense)
            return True
    return False

def show_expenses(data):
    if not data:
        print("Нет сохраненных расходов.")
    else:
        print("Список расходов:")
        for expense in data:
            print(f"{expense['№']} | {expense['Дата']}: \n {expense['Категория']} — {expense['Содержание операции']} \n ({expense['Расходы']})")

if __name__ == "__main__":
    expenses = load_data()

    while True:
        print("\n1. Добавить расходы")
        print("2. Удалить расходы")
        print("3. Показать расходы")
        print("4. Выход")

        choice = input("\nВыберите действие (1/2/3/4): ")

        if choice == '1':
            expense = add_expense(expenses)
            expenses.append(expense)
            save_data(expenses)
            print("Расход успешно добавлен.")

        elif choice == '2':
            show_expenses(expenses)
            del_num = input("\nВведите номер расхода для удаления: ")
            if delete_expense(expenses, int(del_num)):
                save_data(expenses)
                print("Расход успешно удален.")
            else:
                print("Расход с указанным номером не найден.")

        elif choice == '3':
            show_expenses(expenses)

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")
```

### Результат.
#### Добавление расходов:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S721.png)
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S722.png)

#### Удаление расходов:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S723.png)
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S724.png)

#### Показ расходов:
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S725.png)

#### Файл csv (без плагина ExcelReader):
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S726.png)

#### Файл csv (c плагином ExcelReader):
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S727.png)


## Выводы

1. Функция load_data() открывает файл для записи расходов (expenses.csv), читает его содержимое с использованием метода DictReader (используется для вывода данных из файла в виде словаря), при этом возвращается список словарей, представляющих данные из файла.
2. Функция save_data() записывает данные из списка словарей в файл расходов с использованием метода DictWriter (в качестве данных для записи используется словарь, требуется строгое указание параметра fieldnames), сначала записывается заголовок (header) с заданными именами полей (fieldnames), а затем строки данных.
3. Функция add_expense() запрашивает у пользователя информацию о новом расходе (дату, категорию, содержание операции и саму потраченную сумму), после создает словарь, представляющий новый расход с его порядковым номером (длина len(data) + 1 или 1, если еще не было введено расходов). Возвращает этот словарь.
4. Функция delete_expense() удаляет расход с указанным номером из списка данных. Возвращает True, если расход был успешно удален, и False, если расход с указанным номером не найден.
5. Функция show_expenses() выводит список расходов на экран. Если данных нет, выводит сообщение об отсутствии сохраненных расходов.

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
with open('input.txt', encoding='utf-8') as f:
    data = f.read()

    excluded = [' ', '\n', '.']
    count = 0
    for letter in data:
        if letter not in excluded:
            count += 1
    letters = count

    words = len(data.split())
    lines = len(data.split('\n'))

print(f"Input file contains:\n{letters} letters\n{words} words\n{lines} lines")
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S73.png)

## Выводы

1. Чтобы найти количество букв в текстовом файле, необходимо составить список исключенных символов (пробел, перенос на следующую строку, точка) и проверить каждую букву (символ) на отсутствие в нем. Если буква не исключена, то к счетчику прибавляется 1.
2. Чтобы найти количество слов, данные из текста делятся на слова методом split (по умолчанию разделитель - пробел), а затем вычисляется длина получившегося списка.
3. Чтобы найти количество строк, нужно использовать метод split с разделителем \n и вычислить длину получившегося списка.

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

