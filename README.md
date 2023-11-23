# Тема 8. Введение в ООП
Отчет по Теме #8 выполнила:
- Плясунова Милена Юрьевна
- ПИЭ-21-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

Работу проверил:
- к.э.н., доцент Панов М.А.

# Лабораторные работы
## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car: 
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota","Corolla")
```

### Результат.

```python
class Car:
# Определение класса с именем Car.
    def __init__(self, make, model):
""" Метод инициализации (конструктор) класса.
Метод __init__ вызывается при создании нового объекта этого класса.
Параметры self, make и model представляют объект, производителя и модель автомобиля соответственно. """
        self.make = make
# Эта строка присваивает значение параметра make атрибуту make объекта self, который вызывает этот метод.
        self.model = model
# Эта строка присваивает значение параметра model атрибуту model объекта self, который вызывает этот метод.

my_car = Car("Toyota","Corolla")
""" Создание объекта Car с именем my_car, при его создании передаются значения "Toyota" и "Corolla" для параметров make и model.
Таким образом, создается экземпляр класса Car с конкретным производителем и моделью."""
```

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L72.png)

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
### Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L73.png)

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L74.png)

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/L75.png)

# Самостоятельные работы
## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

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
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

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
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

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
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
def censor_text(text, banned_words):
    for word in banned_words:
        block = "*" * len(word)
        text = text.replace(word, block)
    return text

with open('input.txt', encoding='utf-8') as f:
    data = f.read()
    banned_words = data.split()
    text = ("Hello, world! Python IS the programming language of thE future. My\nEMAIL is....\nPYTHON is awesome!!!!")
    text_low = text.lower()

censored_text = censor_text(text_low, banned_words)

index = 0
result = ''

for letter in censored_text:
    if letter == '*':
        result += letter
        index += 1
    else:
        result += text[index]
        index += 1

print(result)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S74.png)

## Выводы

1. Функция censor_text принимает на вход исходный текст в нижнем регистре и список запрещенных слов. Для каждого запрещенного слова вычисляется блок со звездочками, который соответствует длине слова ("*" * len(word)). Затем в полученном тексте все встреченные запрещенные слова заменяются на такие блоки.
2. Чтобы вернуть исходный регистр некоторым нетронутым словам, пришлось прибегнуть к замене. Проверялась каждая буква (символ) из полученного зацензуренного текста - если это звездочка, то она прибавляется к результирующему тексту, а индекс увеличивается на 1, если это иная буква (символ) то к результату прибавляется буква (символ) исходого текста и индекс снова увеличивается на 1.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
import random

def generate(words, sentences):
    new_sentence = []
    for sentence in sentences:
        generated = sentence.replace('_', random.choice(words), 1)
        generated_again = generated.replace('_', random.choice(words), 1)
        new_sentence.append(generated_again)
    return new_sentence


with open('input.txt', 'r', encoding='utf-8') as file:
    words = file.read().split(', ')

sentences = [
    "Если бы у меня тогда был _, жизнь стала бы чуточку проще.",
    "Я решил подарить ей на день рождения _. Она была в полном восторге, я уверен!",
    "Заказал тогда по скидке _, но пришел _. Наверное, это знак."
    ]

new_sentences = generate(words, sentences)

for sentence in new_sentences:
    print(sentence)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S751.png)
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_7/pic/S752.png)

## Выводы

Функция generate принимает на вход список слов для генерации и список предложений. На основе каждого предложения из списка предложений генерируется новое предложение, которое заменяет символ '_' на случайное слово из списка words. При этом операция замены происходит два раза (сначала для generated, потом для generated_again, каждый раз заменяется только один символ для того, чтобы в предложении с двумя повторами вставленные слова не повторялись).

