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
"""
Метод инициализации (конструктор) класса.
Метод __init__ вызывается при создании нового объекта этого класса.
Параметры self, make и model представляют объект, производителя и модель автомобиля соответственно.
"""
        self.make = make
# Эта строка присваивает значение параметра make атрибуту make объекта self, который вызывает этот метод.
        self.model = model
# Эта строка присваивает значение параметра model атрибуту model объекта self, который вызывает этот метод.

my_car = Car("Toyota","Corolla")
# Создание объекта Car с именем my_car, в который передаются значения "Toyota" и "Corolla" для параметров make и model.
```

Таким образом, создается экземпляр класса Car с конкретным производителем и моделью.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota","Corolla")
my_car.drive()
```

### Результат.
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
"""
Метод класса, который выводит сообщение о том, в какой машине едут (использует значения атрибутов make и model).
"""
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota","Corolla")
my_car.drive()
# Вызов метода drive для объекта my_car.
# Выводится сообщение о том, в какой машине едут, используя значения атрибутов make (производитель) и model (модель).
```

![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/L82.png)

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
### Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota","Corolla")
my_car.drive()

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_elecic_car = ElectricCar("Tesla", "Model S", 75)
my_elecic_car.drive()
my_elecic_car.charge()
```

### Результат.
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota","Corolla")
my_car.drive()

class ElectricCar(Car):
# Определение класса ElectricCar, наследующегося от Car.
    def __init__(self, make, model, battery_capacity):
"""
Конструктор __init__, который вызывает конструктор родительского класса с помощью super().
Добавляет атрибут battery_capacity (емкость батареи).
"""
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
"""
Метод charge класса ElectricCar.
Выводит сообщение о том, что электромобиль определенной марки (make), модели (model) и емкости батареи (battery_capacity) заряжается.
"""
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
# Создание экземпляра класса ElectricCar с маркой "Tesla", моделью "Model S" и емкостью батареи 75.
my_electric_car.drive()
my_electric_car.charge()
# Вызов методов drive (наследуемый) и charge для объекта my_electric_car.
```

![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/L83.png)

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self._make = make
        self.__model = model

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")
print(my_car._make)
# print(my_car.__model)
my_car.drive()
```

### Результат.

```python
class Car:
    def __init__(self, make, model):
        self._make = make
# Защищенный атрибут.
# Имя начинается с одного нижнего подчеркивания, что обозначает его доступность внутри класса и его подклассов.
        self.__model = model
# Приватный атрибут.
# Имя начинается с двух подчеркиваний. Он доступен только внутри класса.

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")
print(my_car._make)
# Вывод значения защищенного атрибута _make с использованием print(my_car._make).
# print(my_car.__model)
# Вывод значения приватного атрибута __model с использованием print(my_car.__model).
# Это вызовет ошибку, так как приватные атрибуты не могут быть прямо доступны извне класса.
my_car.drive()
```

![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/L841.png)

### Попытка вызова приватного атрибута (print(my_car.__model)):
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/L842.png)

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(radius=3)
rectangle = Rectangle(width=4, height=5)
shapes = [rectangle, circle]

for shape in shapes:
    print(shape.area())
```

### Результат.
```python
class Shape:
# Базовый класс формы, который предоставляет метод area(). 
    def area(self):
"""
Абстрактный метод, так как онне имеет реализации (просто pass).
Он предполагает, что любой подкласс Shape должен предоставить собственную реализацию метода.
"""
        pass

class Rectangle(Shape):
# Подкласс Shape, представляет собой прямоугольник.
    def __init__(self, width, height):
"""
Конструктор __init__.
Имеет атрибуты width (ширина) и height (высота).
"""
        self.width = width
        self.height = height

    def area(self):
"""
Переопределенный метод нахождения площади.
"""
        return self.width * self.height

class Circle(Shape):
# Подкласс Shape, представляет собой круг.
    def __init__(self, radius):
"""
Конструктор __init__.
Имеет атрибут radius (радиус).
"""
        self.radius = radius

    def area(self):
"""
Переопределенный метод нахождения площади.
"""
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(width=4, height=5)
circle = Circle(radius=3)
# Создание объектов прямоугольника и круга.
shapes = [rectangle, circle]
# Добавление объектов в список.

for shape in shapes:
    print(shape.area())
# Цикл, который проходится по каждой фигуре в списке shapes.
# Выводит площадь фигуры с помощью методов area.
```

![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/L85.png)

# Самостоятельные работы
## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Tank:
    def __init__(self, model):
        self.model = model

kv2 = Tank("КВ-2")
print(kv2.model)
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/S81.png)

## Выводы
Этот код определяет класс Tank, который имеет конструктор __init__, принимающий параметр model. Внутри конструктора значение model присваивается атрибуту self.model, который является членом данного экземпляра класса. Затем создается экземпляр класса Tank с именем kv2. После этого выводится значение атрибута model созданного экземпляра на экран с помощью print.
 
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Tank:
    def __init__(self, model, country,
                 gun_caliber, firing_rate,
                 weight, engine_power, speed):
        self.model = model
        self.country = country
        self.gun_caliber = gun_caliber
        self.firing_rate = firing_rate
        self.weight = weight
        self.engine_power = engine_power
        self.speed = speed

    def shoot(self):
        print(f"Танк {self.model} ({self.country}) стреляет из орудия калибра {self.gun_caliber} мм")

    def shots_per_minute(self, minutes):
        result = self.firing_rate * minutes
        return result

kv2 = Tank("КВ-2","СССР",
           152, 2.5,
           60.8, 640, 35)
kv2.shoot()
minutes = 5
print(f"Танк {kv2.model} выстрелил {kv2.shots_per_minute(minutes)} раз(а) за {minutes} минут")
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/S82.png)

## Выводы
Этот код представляет собой определение класса Tank (танк), который имеет различные характеристики, такие как модель, страна производитель, калибр орудия, скорострельность, вес, мощность двигателя и скорость. У класса также есть два метода:

1. shoot() - выводит сообщение о том, что танк стреляет, указывая модель, страну и калибр орудия.
2. shots_per_minute() - принимает аргумент minutes (количество минут) и возвращает общее количество выстрелов, которые танк сможет сделать за указанное количество минут, основываясь на его скорострельности.

После определения класса создается экземпляр танка с именем kv2, затем для созданного объекта вызываются методы shoot() и shots_per_minute().

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
import random

class Tank:
    def __init__(self, model, country,
                 gun_caliber, firing_rate,
                 weight, engine_power, speed):
        self.model = model
        self.country = country
        self.gun_caliber = gun_caliber
        self.firing_rate = firing_rate
        self.weight = weight
        self.engine_power = engine_power
        self.speed = speed

    def shoot(self):
        print(f"Танк {self.model} ({self.country}) стреляет из орудия калибра {self.gun_caliber} мм")

    def shots_per_minute(self, minutes):
        result = self.firing_rate * minutes
        return result

kv2 = Tank("КВ-2","СССР",
           152, 2.5,
           60.8, 640, 35)
kv2.shoot()
minutes = 5
print(f"Танк {kv2.model} выстрелил {kv2.shots_per_minute(minutes)} раз(а) за {minutes} минут")

class LightTank(Tank):
    def __init__(self, model, country,
                 gun_caliber, firing_rate,
                 weight, engine_power, speed,
                 view_range):
        self.model = model
        self.country = country
        self.gun_caliber = gun_caliber
        self.firing_rate = firing_rate
        self.weight = weight
        self.engine_power = engine_power
        self.speed = speed
        self.view_range = view_range

    def scout(self):
        chance = random.randint(1, 2)
        if chance == 1:
            print(f"Танк {self.model} ({self.country}) обнаружен и едет со скоростью {self.speed} км/ч")
        else:
            print(f"Танк {self.model} ({self.country}) разведывает территорию в диапазоне {self.view_range} м")

pz1c = LightTank("Pz.Kpfw. I Ausf. C", "Германия",
                 7.92, 165,
                 8, 150, 79,
                 320)
pz1c.shoot()
pz1c.scout()
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/S831.png)
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/S832.png)

## Выводы

Класс LightTank является подклассом (или дочерним классом) класса Tank. Он наследует атрибуты и методы от родительского класса Tank, но имеет и свои собственные атрибуты и методы, такие как view_range и scout(). Он также может использовать методы из родительского класса, такие как shoot и shots_per_minute.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Tank:
    def __init__(self, model, country,
                 gun_caliber, firing_rate,
                 weight, engine_power, speed):
        self.__model = model
        self.country = country
        self.gun_caliber = gun_caliber
        self.firing_rate = firing_rate
        self.weight = weight
        self.engine_power = engine_power
        self.speed = speed

    def shoot(self):
        print(f"Танк {self.__model} ({self.country}) стреляет из орудия калибра {self.gun_caliber} мм")

    def shots_per_minute(self, minutes):
        result = self.firing_rate * minutes
        return result

kv2 = Tank("КВ-2","СССР",
           152, 2.5,
           60.8, 640, 35)
kv2.shoot()
minutes = 5
print(f"Танк {kv2.__model} выстрелил {kv2.shots_per_minute(minutes)} раз(а) за {minutes} минут")
```

### Результат.
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/S84.png)

## Выводы

В данном коде переменная model объявлена с использованием двойного подчеркивания в начале имени (__model). Это означает, что переменная доступна только внутри класса Tank и не может быть прямо доступна извне (последняя строка кода).

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
![Меню](https://github.com/Alphaverb/Software_Engineering/blob/Tema_8/pic/S85.png)

## Выводы

Метод sound объявлен в родительском классе Tank, а затем переопределен в дочерних классах HeavyTank и LightTank. Это означает, что объекты разных типов (тяжелый танк и легкий танк) могут использовать один и тот же метод sound, но предоставлять различную реализацию для этого метода.
